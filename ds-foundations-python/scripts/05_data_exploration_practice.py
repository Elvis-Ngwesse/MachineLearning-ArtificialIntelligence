# Data Exploration Practice

import pandas as pd

df = pd.read_csv('data/netflix_movies.csv')

print("Data Info:")
print(df.info())

print("\nDescribe:")
print(df.describe(include='all'))

# Movies after 2015
recent = df[df['release_year'] > 2015]
print(f"\nMovies released after 2015: {len(recent)}")
print(recent[['title', 'release_year']].head())

# Group by country
count_by_country = df.groupby('country')['title'].count().sort_values(ascending=False)
print("\nTop 10 countries:\n", count_by_country.head(10))

# Group by type
avg_year = df.groupby('type')['release_year'].mean()
print("\nAverage release year by type:\n", avg_year)
