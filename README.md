# 📊 Data Analysis with Pandas & Visualization with Matplotlib

PROJECT STRUCTURE

Data_Analysis/
│── Data_Analysis.py      # Main analysis script
│── README.md             # Project documentation (this file)
│── iris.csv              # Dataset (auto-created if sklearn is available)
│── plots/                # Saved plots (generated after running script)
│    ├── line_chart.png
│    ├── bar_chart.png
│    ├── histogram.png
│    └── scatter_plot.png

📊 Features

Task 1: Load & Explore

Load dataset (from sklearn or CSV fallback)

Inspect first rows, data types, and missing values

Handle missing values (drop or fill)

Task 2: Basic Analysis

Descriptive statistics (.describe())

Group by categorical column and compute means

Print key observations

Task 3: Visualization

Line chart (trends over samples or time)

Bar chart (category comparisons)

Histogram (distribution of numerical data)

Scatter plot (relationship between two variables)

Customized titles, labels, and legends

Automatically saved into the plots/ folder

📌 Example Output
📈 Line Chart

📊 Bar Chart

📉 Histogram

🔵 Scatter Plot

🛠 Error Handling

If the dataset file is missing → prints a clear error message

If scikit-learn is not installed → falls back to iris.csv

Handles missing values by dropping or filling

🔄 Using Your Own Dataset

To analyze your own dataset instead of Iris:

Place your CSV in the project folder.

Modify the loading section in Data_Analysis.py:

import pandas as pd
df = pd.read_csv("your_dataset.csv")


Run the script again.


## 📌 Project Overview
This project demonstrates how to:
- Load and explore datasets using **pandas**
- Perform basic data analysis (summary statistics, groupings, observations)
- Create visualizations using **matplotlib** and **seaborn**
👨‍💻 Author
Developed by Ngoga Roy
Diploma in Electrical & Electronics Engineering (Power Option)

The default dataset is the **Iris dataset**.  
The script is designed to be **portable**:
- If `scikit-learn` is installed → dataset is loaded directly via `sklearn.datasets.load_iris`.  
- If not → the script falls back to a pre-saved **`iris.csv`** file.  
- On the first successful run with `scikit-learn`, `iris.csv` is automatically created for future use.  

---

## ⚙️ Requirements
Make sure you have Python **3.8+** installed.  
Install the required libraries:

```bash
pip install pandas matplotlib seaborn scikit-learn


Note: If you don’t want to install scikit-learn, you can still run the script using the iris.csv file included (or generated on first run).

▶️ How to Run

Clone or download this project to your local machine.

Open a terminal in the project folder.

Run the script:
    python Data_Analysis.py

If you prefer Jupyter Notebook, copy the code into a .ipynb file and run each cell step by step.



