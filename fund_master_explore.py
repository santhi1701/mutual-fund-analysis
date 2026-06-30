import requests
import pandas as pd

schemes = {
    "HDFC Top 100": 125497,
    "SBI Bluechip": 119551,
    "ICICI Bluechip": 120503,
    "Nippon Large Cap": 118632,
    "Axis Bluechip": 119092,
    "Kotak Bluechip": 120841
}

fund_details = []

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        meta = data["meta"]

        fund_details.append({
            "Scheme Code": meta.get("scheme_code"),
            "Scheme Name": meta.get("scheme_name"),
            "Fund House": meta.get("fund_house"),
            "Scheme Type": meta.get("scheme_type"),
            "Scheme Category": meta.get("scheme_category")
        })

fund_df = pd.DataFrame(fund_details)

print("\nFund Details")
print(fund_df)

fund_df.to_csv("data/processed/fund_master.csv", index=False)

print("\nFund master saved successfully!")
print("\nUnique Fund Houses")
print(fund_df["Fund House"].unique())
print("\nUnique Categories")
print(fund_df["Scheme Category"].unique())
print("\nUnique Scheme Types")
print(fund_df["Scheme Type"].unique())