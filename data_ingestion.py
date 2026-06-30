import os
import pandas as pd

DATA_FOLDER = "data/raw"

csv_files = [file for file in os.listdir(DATA_FOLDER) if file.endswith(".csv")]

if not csv_files:
    print("No CSV files found.")
    exit()

quality_report = []

for file in csv_files:

    file_path = os.path.join(DATA_FOLDER, file)

    df = pd.read_csv(file_path)

    print("=" * 70)
    print(f"Dataset : {file}")
    print("=" * 70)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    duplicates = df.duplicated().sum()
    print("\nDuplicate Rows:")
    print(duplicates)

    print("\nColumn Information:")
    df.info()

    print("\nSummary Statistics:")
    print(df.describe())

    quality_report.append({
        "Dataset": file,
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Rows": int(duplicates)
    })

summary_df = pd.DataFrame(quality_report)

print("\n" + "=" * 70)
print("DATA QUALITY SUMMARY")
print("=" * 70)
print(summary_df)

os.makedirs("reports", exist_ok=True)
summary_df.to_csv("reports/data_quality_summary.csv", index=False)

print("\nData quality summary saved to reports/data_quality_summary.csv")