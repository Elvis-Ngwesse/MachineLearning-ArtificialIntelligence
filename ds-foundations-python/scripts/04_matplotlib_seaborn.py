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
import os


PLOT_DIR = './ds-foundations-python'
os.makedirs(PLOT_DIR, exist_ok=True)

# Set a seaborn style
sns.set_theme(style="whitegrid")

# Load and Inspect the Data
df = pd.read_csv('ds-foundations-python/data/titanic.csv')

# Function to save plots
def save_plot(filename: str):
    """
    Save the current matplotlib plot to the global plot directory.
    Prints the absolute path after saving.
    """
    save_path = os.path.join(PLOT_DIR, filename)
    plt.savefig(save_path)
    print(f"Plot saved at: {os.path.abspath(save_path)}")


# Function to inspect data
def inspect_data():
    print("Data Info:")
    print(df.info())
    print("\nSummary Statistics:")
    print(df.describe())
    print("\nFirst 5 Rows of Data:")
    print(df.head())


# 📦 Box Plot: Age Distribution by Class
def box_plot_age_distribution_by_class():
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Pclass', y='Age', data=df, palette="Set2")
    plt.title('Age Distribution by Passenger Class')
    plt.xlabel('Passenger Class')
    plt.ylabel('Age')
    save_plot('age_distribution_box.png')
    plt.show()


# 🔥 Heatmap: Correlation Matrix
def plot_correlation_heatmap():
    plt.figure(figsize=(10, 8))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.title('Feature Correlation Heatmap')
    plt.tight_layout()
    save_plot('correlation_heatmap.png')
    plt.show()


# 🎯 Scatter Plot: Fare vs Age Colored by Survival
def scatter_plot_fare_vs_age():
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df, palette='Set1')
    plt.title('Fare vs Age Colored by Survival')
    plt.xlabel('Age')
    plt.ylabel('Fare')
    plt.legend(title='Survived')
    plt.grid(True)
    save_plot('fare_vs_age_scatter.png')
    plt.show()


# Histogram of Age
def histogram_plot_age_distribution():
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Age'].dropna(), bins=30, color='skyblue', edgecolor='black', kde=True)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout() 
    save_plot('age_distribution_histogram.png') 
    plt.show()


# Countplot: Embarked Distribution
def countplot_plot_embarked_distribution():
    plt.figure(figsize=(6, 4))
    sns.countplot(
    x='Embarked',
    data=df,
    palette='pastel',         
    order=df['Embarked'].value_counts().index 
    )
    plt.title('Passenger Count by Embarkation Port')
    plt.xlabel('Port of Embarkation')
    plt.ylabel('Number of Passengers')
    plt.grid(axis='y', linestyle='--', alpha=0.5) 
    plt.tight_layout() 
    save_plot('embarked_countplot.png') 
    plt.show()


# Barplot: Survival Rate by Class
def barplot_plot_survival_by_class():
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

    plt.ylim(0, 1)
    save_plot('survival_rate_by_class_barplot.png')
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    # inspect_data()
    # box_plot_age_distribution_by_class()
    # plot_correlation_heatmap()
    # scatter_plot_fare_vs_age()
    # histogram_plot_age_distribution()
    # countplot_plot_embarked_distribution()
    # barplot_plot_survival_by_class()



# python3 ds-foundations-python/scripts/04_matplotlib_seaborn.py