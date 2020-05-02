import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("avocado.csv")
df = df.copy()[ df["type"] == "organic"]
df['Date'] = pd.to_datetime(df["Date"])

# print(df.head(10))
# print(df.tail(2))
# print(df["AveragePrice"].head())

# This - A value is trying to be set on a copy of a slice from a DataFrame.
# albany_df = df[ df['region'] == "Albany" ]
# or this
albany_df = df.copy()[ df['region'] == "Albany" ]
# print(albany_df.head(1))

# this
# albany_df = albany_df.set_index("Date")
# or this
albany_df.set_index("Date", inplace=True)

# print(albany_df.head(1))

albany_df.sort_index(inplace=True)

albany_df['AveragePrice'].plot()

albany_df['price25ma'] = albany_df['AveragePrice'].rolling(25).mean()

albany_df['price25ma'].plot()

albany_df.dropna().head(3)

# list(set(df['region'].values.tolist()))
uniqueRegion = df['region'].unique()

graph_df = pd.DataFrame()

for region in uniqueRegion:
    print(region)
    region_df = df.copy()[ df['region'] == region ]
    region_df.set_index("Date", inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f'{region}_price25ma'] = region_df['AveragePrice'].rolling(25).mean()

    if graph_df.empty:
        graph_df = region_df[[f'{region}_price25ma']]
    else:
        graph_df = graph_df.join(region_df[f'{region}_price25ma'])

graph_df.dropna().plot(figsize=(8,5), legend=False)
plt.show()