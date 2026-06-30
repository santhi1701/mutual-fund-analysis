# Data Dictionary

## fact_nav

| Column | Data Type | Description |
|--------|-----------|-------------|
| scheme_code | INTEGER | Unique AMFI scheme code |
| nav_date | DATE | Date of NAV |
| nav | REAL | Net Asset Value |

## dim_fund

| Column | Data Type | Description |
|--------|-----------|-------------|
| scheme_code | INTEGER | AMFI scheme code |
| scheme_name | TEXT | Mutual fund scheme name |
| fund_house | TEXT | Fund house |
| scheme_type | TEXT | Open-ended, etc. |
| scheme_category | TEXT | Equity, Debt, etc. |