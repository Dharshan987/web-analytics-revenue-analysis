# 🌐 Web Analytics Revenue Analysis

![Python](https://img.shields.io/badge/Python-Pandas-blue?logo=python)
![DuckDB](https://img.shields.io/badge/SQL-DuckDB-yellow?logo=duckdb)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi)
![License](https://img.shields.io/badge/License-MIT-green)

Exploratory analysis of a 50,000-row synthetic, session-level **web analytics dataset** to identify what actually drives revenue — traffic sources, device mix, user behaviour patterns — using Python for EDA and **DuckDB SQL** for fast segmentation, with results surfaced in a Power BI dashboard.

---

## 🎯 Questions This Analysis Answers

| Area | Example Questions |
|---|---|
| **Revenue drivers** | Which channels and traffic sources contribute the most revenue per session? |
| **User behaviour** | How do bounce rate, pages-per-session, and session duration relate to conversion? |
| **Segmentation** | Revenue by device, geography, and new vs returning visitors |
| **Conversion funnel** | Where sessions drop off between landing and transaction |

---

## 🧠 Approach

1. **EDA in Python (Pandas)** — distributions, missing-value profiling, outlier checks on session metrics
2. **SQL in DuckDB** — session-level segmentation queries run directly on large files without a database server; window functions for per-segment ranking
3. **Power BI** — cleaned aggregates exported to CSV and modelled into an interactive dashboard (channel, device, and geo views)

Why DuckDB: it runs analytical SQL straight on local Parquet/CSV at high speed — ideal for datasets too large for Excel but not worth a full warehouse.

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/Dharshan987/web-analytics-revenue-analysis.git
cd web-analytics-revenue-analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the EDA + SQL analysis
python scripts/eda.py
python scripts/segmentation_queries.py
```

---

## 📁 Project Structure

```
web-analytics-revenue-analysis/
├── data/
│   └── sessions.csv             # 50,000 sessions (channel, device, geo, engagement, revenue)
├── scripts/
│   ├── generate_data.py         # Reproducible data generator (seed=7)
│   ├── eda.py                   # Exploratory data analysis
│   └── segmentation_queries.py  # Runs the DuckDB SQL segmentation
├── sql/
│   └── analysis_queries.sql     # 6 segmentation queries (windows, bands, trends)
├── powerbi/
│   └── dashboard_guide.md       # Model + DAX measures for the dashboard
├── requirements.txt
└── README.md
```

## 👤 Author

**Dharshan R** — Data Analyst | Python · SQL · Power BI
📧 ramesh.r88442202@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/dharshan-r-42a881246) · [GitHub](https://github.com/Dharshan987)
