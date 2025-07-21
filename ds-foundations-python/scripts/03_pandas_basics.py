# pandas Basics

import pandas as pd

# Sample Series
s = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
print("Series:\n", s)

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Titanic dataset
df = pd.read_csv('data/titanic.csv')
print("\nTitanic Head:\n", df.head())
print("\nInfo:\n", df.info())
print("\nDescribe:\n", df.describe())

# Filter
older = df[df['Age'] > 30]
print("\nOlder than 30:\n", older[['Name', 'Age']].head())
