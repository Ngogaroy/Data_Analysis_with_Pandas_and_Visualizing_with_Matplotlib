# =========================================================
# Analyzing Data with Pandas and Visualizing Results
# =========================================================
# Dataset: Iris dataset (from sklearn)
# Libraries: pandas, matplotlib, seaborn
# =========================================================

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# -------------------------------
# Task 1: Load and Explore Dataset
# -------------------------------
try:
    # Load Iris dataset from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame  # Convert to pandas DataFrame
    
    # Display first few rows
    print("First 5 rows of the dataset:")
    print(df.head())
    
    # Check structure
    print("\nDataset Info:")
    print(df.info())
    
    # Check for missing values
    print("\nMissing values per column:")
    print(df.isnull().sum())
    
    # No missing values in Iris, but if there were:
    df = df.dropna()  # or df.fillna(method='ffill')

except FileNotFoundError as e:
    print("Error: Dataset file not found!", e)
except Exception as e:
    print("An error occurred while loading the dataset:", e)

# -------------------------------
# Task 2: Basic Data Analysis
# -------------------------------
print("\nDescriptive Statistics:")
print(df.describe())

# Group by species and compute mean of numerical columns
grouped = df.groupby("target").mean()
print("\nMean values grouped by Species:")
print(grouped)

# Observations
print("\nObservations:")
print("- Sepal length & width vary by species.")
print("- Petal length is a clear differentiator between species.")

# -------------------------------
# Task 3: Data Visualization
# -------------------------------
sns.set(style="whitegrid")

# 1. Line Chart - Example: cumulative petal length over index
plt.figure(figsize=(8,5))
df["petal length (cm)"].cumsum().plot()
plt.title("Cumulative Petal Length Over Samples")
plt.xlabel("Sample Index")
plt.ylabel("Cumulative Petal Length")
plt.show()

# 2. Bar Chart - Average petal length per species
plt.figure(figsize=(8,5))
sns.barplot(x="target", y="petal length (cm)", data=df, ci=None)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram - Distribution of sepal length
plt.figure(figsize=(8,5))
plt.hist(df["sepal length (cm)"], bins=20, color="skyblue", edgecolor="black")
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot - Sepal length vs Petal length
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="target", data=df, palette="Set1")
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
