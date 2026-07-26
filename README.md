# 🚢 Titanic Exploratory Data Analysis (EDA)

## 📌 Project Overview
This project performs Exploratory Data Analysis (EDA) on the Titanic dataset using Python. The objective is to understand the dataset, identify missing values, analyze survival patterns, and answer important business questions through data exploration.

---

## 🎯 Objectives
- Load and explore the Titanic dataset.
- Understand dataset structure and data types.
- Identify missing values and data quality issues.
- Generate descriptive statistics.
- Analyze passenger survival based on different factors.
- Compare survival rates by gender and passenger class.
- Test the hypothesis that women had a higher survival rate than men.

---

## 🛠️ Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn

---

## 📂 Dataset
**Dataset:** Titanic Dataset (`titanic.csv`)

The dataset contains information about Titanic passengers such as:
- Passenger ID
- Survival Status
- Passenger Class
- Name
- Sex
- Age
- Number of Siblings/Spouses
- Number of Parents/Children
- Fare
- Embarked Port

---

## 📊 Exploratory Data Analysis Performed

The following analyses were performed:

### 1. Dataset Overview
- Displayed the first five rows.
- Checked dataset dimensions.
- Inspected data types.

### 2. Data Cleaning
- Identified missing values.
- Detected potential data quality issues.

### 3. Statistical Summary
- Generated descriptive statistics for numerical columns.

### 4. Business Questions Answered
- What is the overall survival rate?
- Did gender affect survival?
- Did passenger class affect survival?
- Did age affect survival?
- Are there any missing values or anomalies?

### 5. Survival Analysis
- Overall survival percentage.
- Gender-wise survival comparison.
- Passenger class-wise survival comparison.

### 6. Hypothesis Testing
**Hypothesis:**
> Women had a higher survival rate than men.

The analysis compares the survival percentages of male and female passengers.

---

## 📈 Key Findings

- Overall survival rate is approximately **38%**.
- Female passengers had a significantly higher survival rate than male passengers.
- First-class passengers survived more frequently than second- and third-class passengers.
- The dataset contains missing values in columns such as **Age**, **Cabin**, and **Embarked**.
- Missing values should be handled before building machine learning models.

---

## ▶️ How to Run

1. Install the required libraries:

```bash
pip install pandas matplotlib seaborn
```

2. Place `titanic.csv` in the same folder as the Python script.

3. Run the script:

```bash
python titanic_eda.py
```

---

## 📁 Project Structure

```
Titanic-EDA/
│── titanic.csv
│── titanic_eda.py
│── README.md
```

---

## 📚 Libraries Used

- pandas
- matplotlib.pyplot
- seaborn
- os

---

## 📌 Conclusion

This project demonstrates how Exploratory Data Analysis (EDA) helps in understanding a dataset before applying machine learning techniques. It highlights survival trends based on gender and passenger class while identifying missing values and data quality issues that require preprocessing.

---

## 👩‍💻 Author

**Anuradha Mishra**

Data Analytics Internship Project
