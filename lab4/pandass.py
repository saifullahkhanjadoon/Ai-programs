import pandas as pd

ds=pd.read_csv("people-1000.csv")

df=pd.DataFrame(ds)
print("head funcion details")
print(df.head(5))

print("\ntail fun details")
print(df.tail(5))
print("\ndescribe fun details")

print(df.describe())
print("\ninfo fun details")

print(df.info())
# print(df)
print(df.value_counts())