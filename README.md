# First-Model
#  Patient Data Analysis & My First ML Model

> A complete data wrangling and machine learning pipeline built on real-world patient and treatment datasets — from raw CSV to trained regression models.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Monoartiam99/First-Model/blob/main/assignment_02.ipynb)

---

##  Project Overview

This project walks through the **full data science lifecycle** using two datasets — `patients.csv` and `treatments.csv`. It covers exploratory data analysis, data cleaning, feature engineering, and building machine learning models to predict patient HbA1c outcomes.

---

## Datasets

| File | Description |
|---|---|
| `patients.csv` | Patient demographics — name, age, sex, height, weight, contact info, address |
| `treatments.csv` | Treatment records — insulin types (Auralin / Novodra), dosage ranges, HbA1c measurements |

---

##  What's Inside the Notebook

### 1.  Exploratory Data Analysis (EDA)
- Load and preview both datasets using `.head()`, `.tail()`, `.info()`, `.describe()`
- Visualise patient **weight** and **height** distributions using KDE histograms (Seaborn)
- Detect outliers (e.g. height = 27, weight = 48.8)

```python
sns.histplot(patients['weight'], kde=True)
sns.histplot(patients['height'], kde=True)
```

---

### 2. Data Preprocessing

Covers the five pillars of data quality:

1. **Completeness** — identify and fill missing values (e.g. `address`, `auralin`)
2. **Tidiness** — reshape treatment data from wide to long format using `.melt()`
3. **Validity** — check for out-of-range values
4. **Accuracy** — verify correctness of data entries
5. **Consistency** — handle duplicates across name fields

```python
patients_df.fillna('No Data Found', inplace=True)

treatments_df = treatments_df.melt(
    id_vars=['given_name', 'surname', 'hba1c_start', 'hba1c_end', 'hba1c_change'],
    var_name='type',
    value_name='dosage_range'
)
```

---

### 3.  Contact Info Extraction (Regex)

Parses messy `contact` column to extract **phone numbers** and **email addresses** into separate columns using `re` and `str.extract()`.

```python
patients['mobile'] = patients['contact'].str.extract(r'(\+?\d[\d\s\-\(\)]{8,}\d)')
patients['email']  = patients['contact'].str.extract(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})')
```

Cleaned contact data is exported to **`patients_details.xlsx`**.

---

### 4.  Treatment Dataset Cleaning

- Melt wide-format insulin columns into tidy rows
- Remove placeholder `"-"` values
- Split dosage ranges (e.g. `"10-20u"`) into `dosage_start` and `dosage_end`
- Strip the `"u"` unit suffix and cast to `int`
- Visualise dosage distributions by treatment type

---

### 5. My First ML Model — Predicting HbA1c Outcomes

#### Features Used
| Feature | Description |
|---|---|
| `hba1c_start` | Patient's starting HbA1c level |
| `auralin_used` | Binary flag — was Auralin prescribed? |
| `novodra_used` | Binary flag — was Novodra prescribed? |

#### Target Variable
- `hba1c_end` — the patient's HbA1c level after treatment

```python
X = treatments[["hba1c_start", "auralin_used", "novodra_used"]]
y = treatments["hba1c_end"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

---

### 6.  Feature Engineering

New features created to boost model performance:

| Feature | How It's Made |
|---|---|
| `treatment_type` | Categorical encoding of which drug(s) were used (0–3) |
| `auralin_effect` | Interaction: `hba1c_start × auralin_used` |
| `novodra_effect` | Interaction: `hba1c_start × novodra_used` |
| `hba1c_start_sq` | Polynomial: `hba1c_start²` |

---

### 7.  Model Comparison

Two models trained and evaluated head-to-head:

| Model | MAE | R² Score |
|---|---|---|
| Linear Regression | — | — |
| Random Forest (200 trees) | — | — |

> *Actual values printed at runtime — run the notebook to see your results!*

Feature importance from the Random Forest is also analysed to understand which variables drive predictions most.

---

##  Tech Stack

| Library | Purpose |
|---|---|
| `pandas` | Data manipulation |
| `numpy` | Numerical operations |
| `matplotlib` | Plotting |
| `seaborn` | Statistical visualisation |
| `scikit-learn` | ML models, metrics, train/test split |
| `re` | Regular expressions for contact parsing |
| `openpyxl` | Excel export |

---

##  Getting Started

### Run in Google Colab (Recommended)
Click the badge at the top 

### Run Locally

```bash
git clone https://github.com/Monoartiam99/First-Model.git
cd First-Model
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
jupyter notebook assignment_02.ipynb
```

Make sure `patients.csv` and `treatments.csv` are in the same directory as the notebook.

---

##  Output Files

| File | Description |
|---|---|
| `patients_details.xlsx` | Cleaned patient contact info (name, mobile, email) |

---

##  Learning Outcomes

By working through this notebook, you will understand:

- How to perform systematic data quality checks
- Regex-based text parsing for messy real-world data
- Reshaping datasets with `.melt()` for tidy analysis
- Building and evaluating regression models with scikit-learn
- Feature engineering techniques — interactions, polynomials, encoding
- How to compare models and interpret feature importance

---
### Waka Time Update
<img width="1641" height="639" alt="image" src="https://github.com/user-attachments/assets/fe3c4ab8-7ae5-4c5a-ae82-b36691cdd330" />
<img width="1631" height="892" alt="image" src="https://github.com/user-attachments/assets/6c93946e-1516-49e4-8c28-598f7a0e1d72" />



> 💡 *This is Assignment 02 — part of a hands-on data science learning journey.*
