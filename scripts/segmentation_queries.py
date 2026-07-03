"""Runs the DuckDB segmentation queries against data/sessions.csv."""
import duckdb, pathlib, re

con = duckdb.connect()
con.execute("CREATE VIEW sessions AS SELECT * FROM read_csv_auto('data/sessions.csv')")
sql = pathlib.Path('sql/analysis_queries.sql').read_text()
for i, chunk in enumerate(sql.split(';'), 1):
    q = re.sub(r'^\s*--.*$', '', chunk, flags=re.M).strip()
    if not q:
        continue
    print(f'\n=== Query {i} ===')
    print(con.execute(q).df().to_string(index=False))
