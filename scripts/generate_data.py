import numpy as np, pandas as pd
rng = np.random.default_rng(7)
N = 50000
channels = ['Organic Search','Paid Search','Direct','Social','Referral','Email']
ch_p =      [0.34,            0.20,         0.18,    0.14,    0.08,      0.06]
devices = ['mobile','desktop','tablet']; dv_p = [0.58,0.36,0.06]
geos = ['India','United States','United Kingdom','Germany','Canada','Australia','Other']
geo_p = [0.30,0.25,0.10,0.08,0.07,0.05,0.15]

df = pd.DataFrame({
 'session_id': [f'S{i:07d}' for i in range(N)],
 'session_date': pd.to_datetime('2025-01-01') + pd.to_timedelta(rng.integers(0, 365, N), unit='D'),
 'channel': rng.choice(channels, N, p=ch_p),
 'device': rng.choice(devices, N, p=dv_p),
 'country': rng.choice(geos, N, p=geo_p),
 'visitor_type': rng.choice(['new','returning'], N, p=[0.65,0.35]),
 'pageviews': rng.geometric(0.35, N).clip(1, 40),
 'session_duration_sec': (rng.exponential(180, N)).round().astype(int).clip(1, 3600),
})
df['bounce'] = ((df.pageviews == 1) & (rng.random(N) < 0.8)).astype(int)
# conversion prob depends on channel/device/visitor type -> realistic drivers
base = 0.012
mult = (df.channel.map({'Email':2.6,'Paid Search':1.8,'Organic Search':1.4,'Referral':1.2,'Direct':1.0,'Social':0.5})
        * df.device.map({'desktop':1.6,'tablet':1.0,'mobile':0.7})
        * df.visitor_type.map({'returning':2.2,'new':1.0}))
p = (base * mult * (df.pageviews / 4).clip(0.3, 3)).clip(0, 0.5)
df['transactions'] = (rng.random(N) < p).astype(int)
df['revenue'] = (df.transactions * rng.lognormal(8.1, 0.6, N)).round(2)
df.loc[df.bounce == 1, ['transactions','revenue']] = 0

df.to_csv('data/sessions.csv', index=False)
print(len(df), 'sessions |', df.transactions.sum(), 'transactions | revenue', round(df.revenue.sum()))
