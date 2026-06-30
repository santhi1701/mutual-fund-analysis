import pandas as pd
from sqlalchemy import create_engine

# Connect to SQLite
engine = create_engine("sqlite:///bluestock_mf.db")

# Read the cleaned NAV data
df = pd.read_csv("data/processed/fund_master.csv")

# Load it into SQLite
df.to_sql(
    "fact_nav",
    con=engine,
    if_exists="replace",
    index=False
)
# Read back the data from SQLite
result = pd.read_sql("SELECT COUNT(*) AS total_rows FROM fact_nav", engine)

print(result)
print("NAV data loaded into SQLite successfully!")