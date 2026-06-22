# data_ingestion.py
# Loads all CSV files, prints their shape/dtypes/head
# Explores fund data and checks data quality

import pandas as pd
import os

RAW_FOLDER = "data/raw"

print("=" * 60)
print("STEP 3: Loading and Profiling All CSV Datasets")
print("=" * 60)


# ── Helper function ─────────────────────────────────────────────
def profile_dataset(filename):
    """
    For each CSV file, prints:
    - Shape (rows × columns)
    - Data types of each column
    - First 5 rows
    - Any missing values or duplicates
    """
    filepath = os.path.join(RAW_FOLDER, filename)

    # Check if file exists
    if not os.path.exists(filepath):
        print(f"\nSKIPPED: {filename} not found")
        return None

    # Load the CSV
    df = pd.read_csv(filepath)

    print(f"\n{'─'*60}")
    print(f"FILE: {filename}")
    print(f"{'─'*60}")

    # 1. Shape
    print(f"\nShape: {df.shape[0]} rows × {df.shape[1]} columns")

    # 2. Data types
    print("\nColumn Data Types:")
    for col in df.columns:
        print(f"  {col:25} → {df[col].dtype}")

    # 3. First 5 rows
    print("\nFirst 5 rows:")
    print(df.head())

    # 4. Anomaly check
    nulls = df.isnull().sum().sum()
    dups  = df.duplicated().sum()

    print(f"\nNull values  : {nulls}")
    print(f"Duplicate rows: {dups}")

    if nulls > 0:
        print("  ⚠ WARNING: Null values found!")
        print(df.isnull().sum()[df.isnull().sum() > 0])

    if dups > 0:
        print(f"  ⚠ WARNING: {dups} duplicate rows found!")

    return df


# ── Load all CSV files created by live_nav_fetch.py ────────────
csv_files = [f for f in os.listdir(RAW_FOLDER) if f.endswith(".csv")]
print(f"\nFound {len(csv_files)} CSV files in {RAW_FOLDER}/")

datasets = {}
for fname in csv_files:
    key = fname.replace(".csv", "")
    datasets[key] = profile_dataset(fname)


# ── STEP 6: Explore the combined NAV data ──────────────────────
print("\n" + "=" * 60)
print("STEP 6: Exploring the Data")
print("=" * 60)

combined_key = "all_schemes_nav"
if combined_key in datasets and datasets[combined_key] is not None:
    df = datasets[combined_key]

    print(f"\nUnique Fund Houses: {df['fund_house'].nunique()}")
    for fh in df["fund_house"].unique():
        print(f"  • {fh}")

    print(f"\nUnique Schemes: {df['scheme_name'].nunique()}")
    for s in df["scheme_name"].unique():
        print(f"  • {s}")

    print(f"\nDate range: {df['date'].min()} to {df['date'].max()}")
    print(f"Total NAV records: {len(df)}")

    print("\nLatest NAV for each scheme:")
    latest = df.groupby("scheme_name").first()[["date", "nav"]]
    print(latest)


# ── STEP 7: Data Quality Summary ───────────────────────────────
print("\n" + "=" * 60)
print("STEP 7: Data Quality Summary")
print("=" * 60)

for name, df in datasets.items():
    if df is not None:
        nulls = df.isnull().sum().sum()
        dups  = df.duplicated().sum()
        flag  = "✓" if (nulls == 0 and dups == 0) else "⚠"
        print(f"  {flag} {name:40} nulls={nulls}  dups={dups}")

print("\n✅ data_ingestion.py completed!")