import pandas as pd
import seaborn as sns
df = sns.load_dataset("anscombe")
print(df)

df.to_csv("anscombe.csv")
g1 = df.groupby("dataset").y.mean()
g2 = df.groupby("dataset").x.mean()
g3 = df.groupby("dataset").y.sum()
g4 = df.groupby("dataset").x.sum()
# print(g1)
# print(g2)
# print(g3)
# print(g4)
