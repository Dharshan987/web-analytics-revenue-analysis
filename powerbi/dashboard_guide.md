# Power BI Dashboard Guide — Web Analytics Revenue Analysis

## Data model
Import `data/sessions.csv` as the fact table (one row per session). Create a dedicated
Date table (`CALENDAR(MIN(sessions[session_date]), MAX(sessions[session_date]))`), mark it
as a Date table, and relate it to `sessions[session_date]` — star schema with one fact
and one date dimension (channel/device/country stay as fact attributes for slicing).

## Core DAX measures
```dax
Total Sessions   = COUNTROWS(sessions)
Total Revenue    = SUM(sessions[revenue])
Transactions     = SUM(sessions[transactions])
Conversion Rate  = DIVIDE([Transactions], [Total Sessions])
Revenue / Session = DIVIDE([Total Revenue], [Total Sessions])
Bounce Rate      = AVERAGE(sessions[bounce])
Revenue LM       = CALCULATE([Total Revenue], DATEADD('Date'[Date], -1, MONTH))
```

## Suggested pages
1. **Overview** — KPI cards (revenue, conversion, bounce), monthly trend line
2. **Acquisition** — revenue and conversion by channel (bar + table), channel slicer
3. **Audience** — device x visitor-type matrix, country map
4. **Engagement** — conversion rate by pageview band (column chart)
