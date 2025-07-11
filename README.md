# 🩺 Diabetes Data Analysis Dashboard

Welcome to the Diabetes Data Analysis Dashboard!  
This interactive web app, built with [Streamlit](https://streamlit.io/), helps you explore and visualize the diabetes dataset in a simple, friendly, and insightful way.

---

## 🚀 Features

- **Intuitive UI:** Effortlessly filter data by age and diabetes outcome using the sidebar.
- **Key Statistics:** Instantly view total records, diabetic cases, and non-diabetic cases.
- **Visualizations:**
  - **Feature Distributions:** Interactive histograms with KDE for any feature.
  - **Correlation Heatmap:** Visualize relationships between all features.
  - **Outcome Comparison:** Boxplots to compare feature distributions for diabetic and non-diabetic groups.
- **Raw Data Viewer:** Inspect the filtered dataset directly in the app.
- **Responsive Layout:** Works well on both desktop and mobile browsers.

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd data\ analysis
```

### 2. Install Requirements

Install all dependencies using pip:

```bash
pip install -r requirements.txt
```

### 3. Run the Dashboard

From your terminal, launch the app:

```bash
streamlit run app.py
```

### 4. Explore the Dashboard

- **Sidebar Filters:** Adjust the age range and diabetes outcome to focus your analysis.
- **Feature Distributions:** Select any feature to see its distribution among the filtered data.
- **Correlation Heatmap:** Understand how features relate to each other.
- **Outcome Comparison:** Compare how each feature differs between diabetic and non-diabetic groups.
- **Raw Data:** Expand the "Show Raw Data" section to see the underlying data for your current filters.

---

## 📊 Dataset Description

The dataset (`diabetes.csv`) contains medical and demographic information for diabetes prediction, including:

| Column                     | Description                                               |
|----------------------------|-----------------------------------------------------------|
| Pregnancies                | Number of times pregnant                                  |
| Glucose                    | Plasma glucose concentration (mg/dL)                      |
| BloodPressure              | Diastolic blood pressure (mm Hg)                          |
| SkinThickness              | Triceps skin fold thickness (mm)                          |
| Insulin                    | 2-Hour serum insulin (mu U/ml)                            |
| BMI                        | Body mass index (weight in kg/(height in m)^2)            |
| DiabetesPedigreeFunction   | Diabetes pedigree function (genetic risk)                 |
| Age                        | Age in years                                              |
| Outcome                    | Diabetes
