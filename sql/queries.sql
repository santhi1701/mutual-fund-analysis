-- 1. Total NAV records
SELECT COUNT(*) FROM fact_nav;

-- 2. Latest NAV date
SELECT MAX(nav_date) FROM fact_nav;

-- 3. Earliest NAV date
SELECT MIN(nav_date) FROM fact_nav;

-- 4. Average NAV
SELECT AVG(nav) FROM fact_nav;

-- 5. Maximum NAV
SELECT MAX(nav) FROM fact_nav;

-- 6. Minimum NAV
SELECT MIN(nav) FROM fact_nav;

-- 7. Latest NAV by scheme
SELECT scheme_code, MAX(nav_date)
FROM fact_nav
GROUP BY scheme_code;

-- 8. Average NAV by scheme
SELECT scheme_code, AVG(nav)
FROM fact_nav
GROUP BY scheme_code;

-- 9. Number of records per scheme
SELECT scheme_code, COUNT(*)
FROM fact_nav
GROUP BY scheme_code;

-- 10. Top 5 schemes by latest NAV
SELECT scheme_code, nav
FROM fact_nav
ORDER BY nav DESC
LIMIT 5;