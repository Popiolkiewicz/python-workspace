import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("avocado.csv")
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

plt.show()