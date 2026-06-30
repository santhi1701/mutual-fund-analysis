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