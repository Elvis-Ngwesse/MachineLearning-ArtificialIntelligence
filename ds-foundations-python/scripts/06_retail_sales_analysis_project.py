# Retail Sales Analysis

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/sales_data.csv')
df.dropna(inplace=True)

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
df['Revenue'] = df['Quantity'] * df['Price']

# Monthly revenue plot
monthly = df.groupby('Month')['Revenue'].sum()
monthly.plot(kind='line', marker='o', title='Monthly Revenue')
plt.ylabel('Revenue')
plt.grid(True)
plt.show()

# Top products
top = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(10)
print("Top 10 Products:\n", top)
