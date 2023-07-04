import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

df = pd.read_csv("C:/Users/Admin/OneDrive/Desktop/HMsup.csv/")
df.set_index(df.columns[0], inplace=True)

# Arrange Suppliers number in descending order
df = df.sort_values(by='Suppliers', ascending=False)

#Add another column representing cumulative sum of Suppliers number
df["cumpercentage"] = df["Suppliers"].cumsum()/df["Suppliers"].sum()* 100

#Draw Pareto analysis
fig, ax1 = plt.subplots()
ax1.bar(df.index, df["Suppliers"], color="C0")
ax1.set_ylabel("Number of Suppliers", color="C0")
ax1.tick_params(axis="y", colors="C0")
ax1.set_xlabel("Country Name")
ax1.set_xticklabels(df.index, rotation=90)
ax1.set_ylim(ymin=0)

#Second vertical axis represent percentage of suppliers
ax2 = ax1.twinx()
ax2.plot(df.index, df["cumpercentage"], color="C1", marker="D", ms=7)
ax2.yaxis.set_major_formatter(PercentFormatter())
ax2.tick_params(axis="y", colors="C1")
ax2.set_ylim(ymin=0)

plt.show()