import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('../data/sales_data.csv')
    df.dropna(inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    df['Revenue'] = df['Quantity'] * df['Price']

    monthly_revenue = df.groupby('Month')['Revenue'].sum()

    plt.figure(figsize=(10,6))
    monthly_revenue.plot(kind='line', marker='o')
    plt.title('Monthly Revenue')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.grid(True)
    plt.show()

    top_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(10)
    print("Top 10 products by revenue:")
    print(top_products)

if __name__ == "__main__":
    main()
