import pandas as pd
import numpy as np

# df = pd.read_csv("minimum_wage_data.csv", encoding="latin")
# df.to_csv("minimum_wage_data.csv", encoding="utf-8")

df = pd.read_csv("minimum_wage_data.csv")
print(df.head())

gb = df.groupby("State")
print(gb.get_group("Alabama").set_index("Year").head())

act_min_wage = pd.DataFrame()

for name, group in df.groupby("State"):
    if act_min_wage.empty:
        act_min_wage = group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name})
    else:
        act_min_wage = act_min_wage.join(group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018": name}))

print(act_min_wage.head())

print(act_min_wage.describe())

print(act_min_wage.corr())

#get data with 0 in column Low.2018
issue_df = df[df['Low.2018']==0]
print(issue_df['State'].unique())

#switch 0 to NaN then drop columns with any NaN, then correlate
min_wage_corr = act_min_wage.replace(0, np.NaN).dropna(axis=1).corr()
print(min_wage_corr)

for problem in issue_df['State'].unique():
    if problem in min_wage_corr.columns:
        print("Missing something here....")


grouped_issues = issue_df.groupby("State")
print(grouped_issues.get_group("Alabama").head(3))
print(grouped_issues.get_group("Alabama")['Low.2018'].sum())

for state, data in grouped_issues:
    if data['Low.2018'].sum() != 0.0:
        print("Some data found for", state)

# Visualizing Correlation Table
import matplotlib.pyplot as plt

# plt.matshow(min_wage_corr)

labels = [c[:2] for c in min_wage_corr.columns]  # get abbv state names.

fig = plt.figure(figsize=(12,12))  # figure so we can add axis
ax = fig.add_subplot(111)  # define axis, so we can modify
ax.matshow(min_wage_corr, cmap=plt.cm.RdYlGn)  # display the matrix
ax.set_xticks(np.arange(len(labels)))  # show them all!
ax.set_yticks(np.arange(len(labels)))  # show them all!
ax.set_xticklabels(labels)  # set to be the abbv (vs useless #)
ax.set_yticklabels(labels)  # set to be the abbv (vs useless #)

plt.show()