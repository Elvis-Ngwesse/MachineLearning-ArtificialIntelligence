import pandas as pd

def main():
    df = pd.read_csv('../data/titanic.csv')
    print("Data Info:")
    print(df.info())

    print("\nSummary Statistics:")
    print(df.describe())

    # Filter passengers older than 30
    older = df[df['Age'] > 30]
    print(f"\nPassengers older than 30: {len(older)}")

    # Group by 'Pclass' and get survival rate
    survival_rate = df.groupby('Pclass')['Survived'].mean()
    print("\nSurvival rate by passenger class:")
    print(survival_rate)

if __name__ == "__main__":
    main()
