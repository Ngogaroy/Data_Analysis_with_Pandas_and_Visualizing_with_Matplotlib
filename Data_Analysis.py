# =========================================================
# Analyzing Data with Pandas and Visualizing Results
# =========================================================
# Dataset: Iris dataset (from sklearn or CSV fallback)
# Libraries: pandas, matplotlib, seaborn
# =========================================================

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Setup
# -------------------------------
# Create folder for saving plots
os.makedirs("plots", exist_ok=True)

# -------------------------------
# Task 1: Load and Explore Dataset
# -------------------------------
try:
    # Try loading from sklearn
    from sklearn.datasets import load_iris
    iris = load_iris(as_frame=True)
    df = iris.frame  # Convert to pandas DataFrame

    # Save a CSV copy for fallback use
    df.to_csv("iris.csv", index=False)
    print("✅ Loaded Iris dataset from sklearn and saved as iris.csv")

except ModuleNotFoundError:
    print("⚠️ scikit-learn not found. Using iris.csv instead...")
    if os.path.exists("iris.csv"):
        df = pd.read_csv("iris.csv")
        print("✅ Loaded iris.csv successfully")
    else:
        raise FileNotFoundError("iris.csv not found. Please install scikit-learn or provide a CSV file.")

# Display first few rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Check structure
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Handle missing values if any
df = df.dropna()

# -------------------------------
# Task 2: Basic Data Analysis
# -------------------------------
print("\nDescriptive Statistics:")
print(df.describe())

# Group by species/target and compute mean of numerical columns
if "target" in df.columns:
    grouped = df.groupby("target").mean()
else:
    grouped = df.groupby(df.columns[-1]).mean()  # Assume last column is categorical

print("\nMean values grouped by Species/Target:")
print(grouped)

# Observations
print("\nObservations:")
print("- Sepal length & width vary by species.")
print("- Petal length is a clear differentiator between species.")

# -------------------------------
# Task 3: Data Visualization
# -------------------------------
sns.set(style="whitegrid")

# 1. Line Chart - Cumulative Petal Length
plt.figure(figsize=(8,5))
df["petal length (cm)"].cumsum().plot()
plt.title("Cumulative Petal Length Over Samples")
plt.xlabel("Sample Index")
plt.ylabel("Cumulative Petal Length")
plt.savefig("plots/line_chart.png")
plt.show()

# 2. Bar Chart - Average Petal Length per Species
plt.figure(figsize=(8,5))
sns.barplot(x="target", y="petal length (cm)", data=df, ci=None)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.savefig("plots/bar_chart.png")
plt.show()

# 3. Histogram - Distribution of Sepal Length
plt.figure(figsize=(8,5))
plt.hist(df["sepal length (cm)"], bins=20, color="skyblue", edgecolor="black")
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.savefig("plots/histogram.png")
plt.show()

# 4. Scatter Plot - Sepal vs Petal Length
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="target", data=df, palette="Set1")
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.savefig("plots/scatter_plot.png")
plt.show()
