CREATE TABLE dim_fund (
    fund_id INTEGER PRIMARY KEY,
    scheme_code INTEGER,
    scheme_name TEXT,
    fund_house TEXT,
    scheme_type TEXT,
    scheme_category TEXT
);

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    nav_date DATE,
    year INTEGER,
    month INTEGER,
    day INTEGER
);

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY,
    scheme_code INTEGER,
    nav_date DATE,
    nav REAL,
    FOREIGN KEY (scheme_code) REFERENCES dim_fund(scheme_code)
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    scheme_code INTEGER,
    amount REAL,
    transaction_type TEXT
);

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY,
    scheme_code INTEGER,
    expense_ratio REAL,
    one_year_return REAL
);

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY,
    scheme_code INTEGER,
    aum REAL
);