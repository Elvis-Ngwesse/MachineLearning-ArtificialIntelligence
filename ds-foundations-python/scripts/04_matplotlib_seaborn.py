# matplotlib and seaborn plotting

# Matplotlib is a popular Python library for creating charts and visualizing data. 
# It supports plots like line graphs, bar charts, and histograms, and works well with 
# NumPy and Pandas. It's widely used in data science to explore and present data clearly.

# Seaborn is a Python library built on top of Matplotlib that makes it easier to create beautiful, 
# informative, and statistical visualizations. It works well with Pandas DataFrames and provides 
# high-level functions to create charts like bar plots, box plots, heatmaps, and scatter plots with 
# less code and better default styles. It's commonly used in data science for quick, attractive 
# insights into data.


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ds-foundations-python/data/titanic.csv')

# Histogram of Age
def plot_age_histogram():
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Age'].dropna(), bins=30, color='skyblue', edgecolor='black', kde=True)
    
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()  # prevent clipping of labels
    
    plt.savefig('age_distribution.png')  # saves the plot as a file
    plt.show()


# Countplot: Embarked Distribution
def plot_embarked_distribution():
    plt.figure(figsize=(6, 4))  # Set figure size
    sns.countplot(
    x='Embarked',
    data=df,
    palette='pastel',           # Nice soft colors
    order=df['Embarked'].value_counts().index  # Sort by count
    )
    plt.title('Passenger Count by Embarkation Port')
    plt.xlabel('Port of Embarkation')
    plt.ylabel('Number of Passengers')
    plt.grid(axis='y', linestyle='--', alpha=0.5)  # Add a light grid
    plt.tight_layout()  # Prevent label cutoff
    plt.show()


# Barplot: Survival Rate by Class
def plot_survival_by_class():
    plt.figure(figsize=(8, 5))
    ax = sns.barplot(x='Pclass', y='Survived', data=df, palette='pastel')

    plt.title('Survival Rate by Passenger Class')
    plt.xlabel('Passenger Class')
    plt.ylabel('Survival Rate')

    # Show percentages on top of each bar
    for p in ax.patches:
        height = p.get_height()
        ax.annotate(f'{height:.1%}',  # format as percentage with 1 decimal place
                    (p.get_x() + p.get_width() / 2, height),
                    ha='center', va='bottom',
                    fontsize=10, color='black')

    plt.ylim(0, 1)  # Survival rate is between 0 and 1
    plt.show()

if __name__ == "__main__":
    # plot_age_histogram()
    # plot_embarked_distribution()
    # plot_survival_by_class()



# python3 ds-foundations-python/scripts/04_matplotlib_seaborn.py
