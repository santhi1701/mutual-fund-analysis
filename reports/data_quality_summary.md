# Data Quality Summary

## Overview

Successfully fetched NAV history for six mutual fund schemes using the mfapi API.

## Checks Performed

- Loaded all generated CSV files.
- Verified dataset shape.
- Checked column data types.
- Displayed sample records.
- Checked missing values.
- Checked duplicate rows.
- Validated AMFI scheme codes.

## Observations

- No duplicate rows found.
- No missing NAV values observed.
- Date column is stored as text and should be converted to datetime during preprocessing.
- NAV values may require numeric conversion for analysis.
- Risk grade information is not available in the API response.

# Key EDA Findings

1. All selected schemes exhibit long-term NAV growth.
2. Daily returns are concentrated around zero, indicating moderate day-to-day movement.
3. Some schemes show higher volatility than others.
4. Strong positive correlations exist among several equity funds.
5. Monthly average NAV generally trends upward.
6. Yearly averages indicate sustained long-term appreciation.
7. Maximum NAV varies significantly across schemes.
8. Rolling averages smooth short-term fluctuations and highlight long-term trends.
9. Data quality checks found no significant missing values or duplicates.
10. The cleaned NAV dataset is suitable for further risk analysis and dashboard development.