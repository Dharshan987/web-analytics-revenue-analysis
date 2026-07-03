"""Exploratory data analysis on session-level web analytics data."""
import pandas as pd

df = pd.read_csv('data/sessions.csv', parse_dates=['session_date'])

print('=== Shape & dtypes ===')
print(df.shape); print(df.dtypes)

print('\n=== Missing values ===')
print(df.isna().sum())

print('\n=== Session metrics ===')
print(df[['pageviews','session_duration_sec']].describe().round(1))

print('\n=== Headline KPIs ===')
sessions = len(df)
conv = df.transactions.sum() / sessions
print(f'Sessions: {sessions:,}')
print(f'Bounce rate: {df.bounce.mean():.1%}')
print(f'Conversion rate: {conv:.2%}')
print(f'Total revenue: {df.revenue.sum():,.0f}')
print(f'Revenue per session: {df.revenue.sum()/sessions:,.2f}')
print(f'Avg order value: {df.loc[df.transactions==1, "revenue"].mean():,.0f}')

print('\n=== Conversion by channel ===')
print(df.groupby('channel').agg(sessions=('session_id','count'),
                                conv_rate=('transactions','mean'),
                                revenue=('revenue','sum')).sort_values('revenue', ascending=False).round(4))

print('\n=== Conversion by device ===')
print(df.groupby('device').agg(sessions=('session_id','count'),
                               conv_rate=('transactions','mean'),
                               revenue=('revenue','sum')).round(4))
