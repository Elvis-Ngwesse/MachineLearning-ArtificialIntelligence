# pandas Basics
# Pandas is a popular Python library designed to make working with structured data (like tables, 
# spreadsheets, or databases) easy and efficient.

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
# "Give me the rows of df where df['Age'] > 30 is True"
older = df[df['Age'] > 30]
print("\nOlder than 30:\n", older[['Name', 'Age']].head())


"""
Why use Pandas?
It helps you organize, manipulate, and analyze data in a simple way.
Provides powerful data structures:
    DataFrame — like a spreadsheet or SQL table (rows & columns).
    Series — like a single column or list with labels.
    Makes it easy to read/write data from files like CSV, Excel, SQL databases, and more.
    Supports filtering, grouping, merging, and reshaping data quickly.
    Widely used in data analysis, data science, and machine learning projects.
"""