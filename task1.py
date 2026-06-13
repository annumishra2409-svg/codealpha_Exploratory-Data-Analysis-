#TASK 2 - Titanic EDA

import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "titanic.csv")

# Read the CSV
df = pd.read_csv(csv_path)

print("="*50)
print("FIRST 5 ROWS")
print(df.head())

print("\n" + "="*50)
print("DATASET SHAPE")
print(df.shape)

print("\n" + "="*50)
print("DATA TYPES")
print(df.dtypes)

print("\n" + "="*50)
print("MISSING VALUES")
print(df.isnull().sum())

print("\n" + "="*50)
print("STATISTICAL SUMMARY")
print(df.describe())

# -------------------------------
# Meaningful Questions
# -------------------------------

print("\nEDA QUESTIONS")
print("1. What was the overall survival rate?")
print("2. Did gender affect survival?")
print("3. Did passenger class affect survival?")
print("4. Did age affect survival?")
print("5. Are there any missing values or anomalies?")

# -------------------------------
# Survival Rate
# -------------------------------

survival_rate = df["Survived"].mean() * 100
print(f"\nOverall Survival Rate: {survival_rate:.2f}%")

# -------------------------------
# Gender vs Survival
# -------------------------------

gender_survival = pd.crosstab(df["Sex"], df["Survived"])
print("\nGender vs Survival")
print(gender_survival)

# -------------------------------
# Passenger Class vs Survival
# -------------------------------

class_survival = pd.crosstab(df["Pclass"], df["Survived"])
print("\nPassenger Class vs Survival")
print(class_survival)

# -------------------------------
# Hypothesis Testing
# -------------------------------

print("\nHypothesis:")
print("Women had a higher survival rate than men.")

female_survival = df[df["Sex"]=="female"]["Survived"].mean()*100
male_survival = df[df["Sex"]=="male"]["Survived"].mean()*100

print(f"Female Survival Rate: {female_survival:.2f}%")
print(f"Male Survival Rate: {male_survival:.2f}%")

# -------------------------------
# Detect Data Issues
# -------------------------------

print("\nPotential Data Issues")
print(df.isnull().sum())