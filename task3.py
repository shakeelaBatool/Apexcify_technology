import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("survey.csv")
counts = df["Satisfaction"].value_counts()
counts.plot(kind="bar")
plt.show()