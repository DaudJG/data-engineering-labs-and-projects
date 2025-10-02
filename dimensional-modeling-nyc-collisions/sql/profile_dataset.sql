-- Profile: Row count and time span
SELECT COUNT(*) AS total_rows,
       MIN(crash_date) AS earliest,
       MAX(crash_date) AS latest
FROM crashes_raw;

-- Profile: Missing boroughs
SELECT COUNT(*) - COUNT(borough) AS missing_boroughs
FROM crashes_raw;

-- Profile: Crashes per year
SELECT EXTRACT(YEAR FROM crash_date) AS year, COUNT(*) AS crashes
FROM crashes_raw
GROUP BY year
ORDER BY year;

-- Profile: Crashes per borough
SELECT borough, COUNT(*) AS crashes
FROM crashes_raw
GROUP BY borough
ORDER BY crashes DESC;

-- Profile: Top 10 streets
SELECT on_street_name, COUNT(*) AS crashes
FROM crashes_raw
WHERE on_street_name IS NOT NULL
GROUP BY on_street_name
ORDER BY crashes DESC
LIMIT 10;

-- Profile: % nulls for key modeling columns
SELECT
    ROUND(100.0 * (COUNT(*) - COUNT(crash_date)) / COUNT(*),6) AS crash_date_null_pct,
    ROUND(100.0 * (COUNT(*) - COUNT(borough)) / COUNT(*),6) AS borough_null_pct,
    ROUND(100.0 * (COUNT(*) - COUNT(on_street_name)) / COUNT(*),6) AS on_street_null_pct,
    ROUND(100.0 * (COUNT(*) - COUNT(number_of_persons_injured)) / COUNT(*),6) AS injured_null_pct,
    ROUND(100.0 * (COUNT(*) - COUNT(number_of_persons_killed)) / COUNT(*),6) AS killed_null_pct
FROM crashes_raw;
