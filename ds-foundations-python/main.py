import os

SCRIPTS = {
    "1": "01_python_basics.py",
    "2": "02_numpy_basics.py",
    "3": "03_pandas_basics.py",
    "4": "04_matplotlib_seaborn.py",
    "5": "05_data_exploration_practice.py",
    "6": "06_retail_sales_analysis_project.py",
    "7": "data_exploration.py",
    "8": "retail_sales_analysis.py"
}

def print_menu():
    print("\n📚 Data Science Practice Menu")
    print("1. Python Basics")
    print("2. NumPy Basics")
    print("3. pandas Basics")
    print("4. Matplotlib & Seaborn")
    print("5. Data Exploration Practice")
    print("6. Retail Sales Analysis Project")
    print("7. Practice: Data Exploration (script version)")
    print("8. Practice: Retail Sales (script version)")
    print("0. Exit")

def run_script(script_name):
    path = os.path.join("scripts", script_name)
    if os.path.exists(path):
        print(f"\n🚀 Running {script_name}...\n")
        os.system(f"python {path}")
    else:
        print(f"❌ Script {script_name} not found!")

if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("Enter your choice (0–8): ").strip()
        if choice == "0":
            print("👋 Exiting. Happy learning!")
            break
        elif choice in SCRIPTS:
            run_script(SCRIPTS[choice])
        else:
            print("❗ Invalid choice. Try again.")
# This script provides a menu-driven interface to run various data science practice scripts.
# It allows users to select a script by number and executes it, providing a simple way to practice Python and data science concepts.
# The scripts cover topics like Python basics, NumPy, pandas, data visualization, and data exploration.
# The user can exit the menu at any time by entering '0'.