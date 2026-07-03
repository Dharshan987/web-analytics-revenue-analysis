-- Web Analytics Revenue Analysis — DuckDB queries on data/sessions.csv
-- Run inside DuckDB: the table `sessions` is loaded by segmentation_queries.py

-- 1. Revenue and conversion by channel
SELECT channel,
       COUNT(*)                        AS sessions,
       SUM(transactions)               AS transactions,
       ROUND(AVG(transactions)*100, 2) AS conv_rate_pct,
       ROUND(SUM(revenue), 0)          AS revenue,
       ROUND(SUM(revenue)/COUNT(*), 2) AS revenue_per_session
FROM sessions
GROUP BY channel
ORDER BY revenue DESC;

-- 2. Device x visitor-type performance
SELECT device, visitor_type,
       COUNT(*) AS sessions,
       ROUND(AVG(transactions)*100, 2) AS conv_rate_pct,
       ROUND(SUM(revenue), 0) AS revenue
FROM sessions
GROUP BY device, visitor_type
ORDER BY revenue DESC;

-- 3. Bounce rate by channel vs conversion
SELECT channel,
       ROUND(AVG(bounce)*100, 1)       AS bounce_rate_pct,
       ROUND(AVG(transactions)*100, 2) AS conv_rate_pct
FROM sessions
GROUP BY channel
ORDER BY bounce_rate_pct;

-- 4. Engagement bands: does pageview depth drive conversion?
SELECT CASE WHEN pageviews = 1 THEN '1 (bounce-risk)'
            WHEN pageviews <= 3 THEN '2-3'
            WHEN pageviews <= 7 THEN '4-7'
            ELSE '8+' END AS pageview_band,
       COUNT(*) AS sessions,
       ROUND(AVG(transactions)*100, 2) AS conv_rate_pct,
       ROUND(SUM(revenue), 0) AS revenue
FROM sessions
GROUP BY pageview_band
ORDER BY MIN(pageviews);

-- 5. Top revenue country per channel (window function)
SELECT * FROM (
  SELECT channel, country, SUM(revenue) AS revenue,
         DENSE_RANK() OVER (PARTITION BY channel ORDER BY SUM(revenue) DESC) AS rnk
  FROM sessions
  GROUP BY channel, country
) WHERE rnk = 1
ORDER BY revenue DESC;

-- 6. Monthly revenue trend with running total
WITH m AS (
  SELECT strftime(session_date, '%Y-%m') AS month, SUM(revenue) AS revenue
  FROM sessions GROUP BY month
)
SELECT month, ROUND(revenue) AS revenue,
       ROUND(SUM(revenue) OVER (ORDER BY month)) AS running_revenue
FROM m ORDER BY month;
