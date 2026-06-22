# live_nav_fetch.py
# This file fetches live NAV data from mfapi.in API
# and saves it as CSV files in data/raw/ folder

import requests        # to call the internet API
import pandas as pd    # to work with data tables
import os              # to create folders
import time            # to add delay between API calls

# ── Folder where we save the CSV files ──
RAW_FOLDER = "data/raw"
os.makedirs(RAW_FOLDER, exist_ok=True)  # creates folder if not exists


# ── STEP 4: Fetch HDFC Top 100 Direct ──────────────────────────────
def fetch_single_scheme(scheme_code, scheme_name):
    """
    This function:
    1. Calls the API with the scheme code
    2. Gets back JSON data
    3. Converts JSON to a table (DataFrame)
    4. Saves as CSV
    """
    print(f"\nFetching: {scheme_name} (Code: {scheme_code})")

    # Build the URL
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    print(f"URL: {url}")

    # Call the API
    response = requests.get(url, timeout=60)

    # Check if successful (200 = success)
    if response.status_code != 200:
        print(f"ERROR: Could not fetch data. Status = {response.status_code}")
        return None

    # Convert response to Python dictionary
    data = response.json()

    # data looks like this:
    # {
    #   "meta": {"scheme_name": "HDFC Top 100...", "fund_house": "HDFC..."},
    #   "data": [{"date": "05-01-2024", "nav": "698.34"}, ...]
    # }

    meta       = data["meta"]         # fund information
    nav_list   = data["data"]         # list of date + NAV values

    print(f"Fund House : {meta['fund_house']}")
    print(f"Scheme     : {meta['scheme_name']}")
    print(f"Total NAV records fetched: {len(nav_list)}")
    print(f"Latest NAV : {nav_list[0]['nav']} on {nav_list[0]['date']}")

    # Convert list of dicts → pandas DataFrame (table)
    df = pd.DataFrame(nav_list)

    # Add extra info columns
    df["scheme_code"] = scheme_code
    df["scheme_name"] = meta["scheme_name"]
    df["fund_house"]  = meta["fund_house"]

    # Convert date format from DD-MM-YYYY to YYYY-MM-DD
    df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
    df["date"] = df["date"].dt.strftime("%Y-%m-%d")

    # Convert NAV from text to number
    df["nav"] = pd.to_numeric(df["nav"])

    # Reorder columns nicely
    df = df[["scheme_code", "scheme_name", "fund_house", "date", "nav"]]

    # Sort by date (newest first)
    df = df.sort_values("date", ascending=False).reset_index(drop=True)

    # Save as CSV
    filename = f"{RAW_FOLDER}/nav_{scheme_name.replace(' ', '_')}.csv"
    df.to_csv(filename, index=False)
    print(f"Saved to: {filename}")

    return df


# ── STEP 5: Fetch 5 Key Schemes ────────────────────────────────────
def fetch_all_schemes():
    # Dictionary of scheme name → AMFI code
    schemes = {
        "HDFC_Top100_Direct"     : 125497,   # Step 4
        "SBI_Bluechip_Direct"    : 119551,   # Step 5
        "ICICI_Bluechip_Direct"  : 120503,
        "Nippon_LargeCap_Direct" : 118632,
        "Axis_Bluechip_Direct"   : 119092,
        "Kotak_Bluechip_Direct"  : 120841,
    }

    all_data = []

    for name, code in schemes.items():
        df = fetch_single_scheme(code, name)
        if df is not None:
            all_data.append(df)
        time.sleep(1)   # wait 1 second between each API call (be polite)

    # Combine all 6 into one big CSV
    if all_data:
        combined = pd.concat(all_data, ignore_index=True)
        combined.to_csv(f"{RAW_FOLDER}/all_schemes_nav.csv", index=False)
        print(f"\nCombined CSV saved: {RAW_FOLDER}/all_schemes_nav.csv")
        print(f"Total rows: {len(combined)}")

    print("\nDone! All NAV data fetched and saved.")


# ── Run the program ─────────────────────────────────────────────────
if __name__ == "__main__":
    fetch_all_schemes()