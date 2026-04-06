import pandas as pd
df = pd.read_csv("students.csv")
df["Average"] = df[["Math","English","Science"]].mean(axis=1)
top_student = df.loc[df["Average"].idxmax()]
print(df)
print(top_student)