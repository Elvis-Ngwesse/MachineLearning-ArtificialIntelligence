# Python for Data Science - Week 1–2 Hands-on Learning

Welcome to the hands-on learning repo for **Python for Data Science (Weeks 1–2)**.

## What you will learn

- Python basics: syntax, control flow, functions  
- NumPy: arrays, broadcasting, vectorization  
- pandas: Series, DataFrames, indexing, filtering  
- matplotlib & seaborn: basic plotting  
- Exploratory Data Analysis (EDA) practice  
- Mini Project: Retail Sales Analysis

## Repo Structure
phase-1/
│
├── readme-phase-1.md
├── data/ # Store datasets here
├── notebooks/ # Jupyter notebooks for lessons & projects
├── scripts/ # Python scripts for practice and mini project
├── requirements.txt # Dependencies

## How to run

1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
pip install -r requirements.txt

3. Go to folder
cd ds-foundations-python/

4. Run files
python main.py
You'll get a menu like:
📚 Data Science Practice Menu
1. Python Basics
2. NumPy Basics
...
0. Exit


pip install kaggle
🔐 2. Get Your Kaggle API Key

    Go to: https://www.kaggle.com/account

    Scroll down to API

    Click “Create New API Token”

    This will download a file called kaggle.json

📁 3. Move API Key to the Right Place

Create the .kaggle/ folder and move the file:
chmod 600 .kaggle/kaggle.json

📌 Titanic Dataset
# Titanic dataset
export KAGGLE_CONFIG_DIR=/Users/elvisngwesse/Desktop/Repositories/MachineLearning-ArtificialIntelligence/ds-foundations-python

kaggle competitions download -c titanic -p /Users/elvisngwesse/Desktop/Repositories/MachineLearning-ArtificialIntelligence/ds-foundations-python/data
unzip /Users/elvisngwesse/Desktop/Repositories/MachineLearning-ArtificialIntelligence/ds-foundations-python/data/titanic.zip -d /Users/elvisngwesse/Desktop/Repositories/MachineLearning-ArtificialIntelligence/ds-foundations-python/data
mv /Users/elvisngwesse/Desktop/Repositories/MachineLearning-ArtificialIntelligence/ds-foundations-python/data/train.csv /Users/elvisngwesse/Desktop/Repositories/MachineLearning-ArtificialIntelligence/ds-foundations-python/data/titanic.csv
rm /Users/elvisngwesse/Desktop/Repositories/MachineLearning-ArtificialIntelligence/ds-foundations-python/data/titanic.zip


📌 Netflix Dataset
export KAGGLE_CONFIG_DIR=/Users/elvisngwesse/Desktop/Repositories/MachineLearning-ArtificialIntelligence/ds-foundations-python

kaggle datasets download -d shivamb/netflix-shows -p /Users/elvisngwesse/Desktop/Repositories/MachineLearning-ArtificialIntelligence/ds-foundations-python/data
unzip /Users/elvisngwesse/Desktop/Repositories/MachineLearning-ArtificialIntelligence/ds-foundations-python/data/netflix-shows.zip -d /Users/elvisngwesse/Desktop/Repositories/MachineLearning-ArtificialIntelligence/ds-foundations-python/data
mv /Users/elvisngwesse/Desktop/Repositories/MachineLearning-ArtificialIntelligence/ds-foundations-python/data/netflix_titles.csv /Users/elvisngwesse/Desktop/Repositories/MachineLearning-ArtificialIntelligence/ds-foundations-python/data/netflix_movies.csv
rm /Users/elvisngwesse/Desktop/Repositories/MachineLearning-ArtificialIntelligence/ds-foundations-python/data/netflix-shows.zip

📌 Retail Sales Dataset
export KAGGLE_CONFIG_DIR=/Users/elvisngwesse/Desktop/Repositories/MachineLearning-ArtificialIntelligence/ds-foundations-python

kaggle datasets download -d aslanahmedov/walmart-sales-forecast -p ds-foundations-python/data
unzip ds-foundations-python/data/walmart-sales-forecast.zip -d ds-foundations-python/data
rm ds-foundations-python/data/walmart-sales-forecast.zip


