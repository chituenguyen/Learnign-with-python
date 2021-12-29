import pandas as pd
import numpy as np

df = pd.read_csv('chipotle.tsv', sep="\t")
print(df.head(5))
print(df.shape)  # 4622 rows and 5 columns
print(df.info())
print(df.columns)
print(df.index)
print(df.describe(include="all"))

####### loc and iloc
print(df.loc[(df.quantity ==15) | (df.item_name=="Nantucket Nectar")],['order_id',"quantity"])
print(df.iloc[[9]])
print(df.iloc[3:11])
print(df.iloc[3:10, :-1])
### dtype
print(df.item_price.dtype)
### apply()
df.item_price=df.item_price.apply(lambda x : float(x.replace("$","")))
print(df.item_price.dtype)
### create new column
df["total_price"] = df.quantity * df.item_price
print(df.head())
print(sum(df.total_price))
## group by
print(df.groupby("item_name")["quantity"].sum())
print(df.groupby("item_name")["quantity"].sum().sort_values(ascending=False))
print(df.item_name.value_counts())
print(df.item_name.nunique())