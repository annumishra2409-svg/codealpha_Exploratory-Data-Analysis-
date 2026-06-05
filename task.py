import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# TASK 2: Exploratory Data Analysis (EDA)
# ==========================================

# 1. Ask meaningful questions before analysis:
# - What was the overall survival rate?
# - Did gender or age play a significant role in survival?
# - Did passenger class (socio-economic status) affect survival chances?

print("--- Loading Dataset ---")
# Using seaborn's built-in Titanic dataset for this project
df = sns.load_dataset('titanic')

# 2. Explore the data structure (variables and data types)
print("\n--- Data Structure ---")
print(df.info()) # Shows columns, non-null counts, and data types
print("\n--- First 5 Rows ---")
print(df.head())

# 3. Detect potential data issues or problems (Missing Values)
print("\n--- Detecting Data Issues (Missing Values) ---")
missing_data = df.isnull().sum()
print(missing_data[missing_data > 0])
# Observation: 'age', 'deck', and 'embarked' have missing values.
# Action: We will fill missing 'age' values with the median age for our analysis.
df['age'] = df['age'].fillna(df['age'].median())

# 4. Identify trends, patterns, and anomalies (Basic Statistics)
print("\n--- Statistical Summary ---")
print(df.describe())

# ==========================================
# TASK 3: Data Visualization
# ==========================================

# Set the visual style for the portfolio
sns.set_theme(style="whitegrid")
plt.figure(figsize=(16, 10))

# --- Chart 1: Survival by Gender (Transforming raw data into visual formats) ---
plt.subplot(2, 2, 1)
ax1 = sns.countplot(data=df, x='sex', hue='survived', palette='Set2')
plt.title('Survival Count by Gender', fontsize=14, fontweight='bold')
plt.xlabel('Gender')
plt.ylabel('Passenger Count')
plt.legend(title='Survived', labels=['No', 'Yes'])
# Insight/Story: Females had a much higher survival rate than males.

# --- Chart 2: Age Distribution (Crafting compelling data stories) ---
plt.subplot(2, 2, 2)
sns.histplot(data=df, x='age', kde=True, color='skyblue', bins=30)
plt.title('Passenger Age Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Age')
plt.ylabel('Frequency')
# Insight/Story: The majority of passengers were between 20 and 30 years old.

# --- Chart 3: Survival by Passenger Class (Testing hypotheses) ---
# Hypothesis: 1st class passengers were prioritized during evacuation.
plt.subplot(2, 2, 3)
ax3 = sns.barplot(data=df, x='pclass', y='survived', palette='viridis', errorbar=None)
plt.title('Survival Rate by Passenger Class', fontsize=14, fontweight='bold')
plt.xlabel('Passenger Class (1 = 1st, 3 = 3rd)')
plt.ylabel('Survival Rate')
# Insight/Story: Hypothesis validated. 1st class passengers had the highest survival rate (>60%).

# --- Chart 4: Correlation Heatmap (Enhancing understanding & validating assumptions) ---
plt.subplot(2, 2, 4)
# Filter only numerical columns for correlation
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix of Numerical Features', fontsize=14, fontweight='bold')
# Insight/Story: 'pclass' has a strong negative correlation with 'fare' (as expected) and 'survived'.

# Adjust layout and display the dashboard
plt.tight_layout()
plt.show()