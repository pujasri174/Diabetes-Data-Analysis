import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("diabetes.csv")

st.set_page_config(page_title="Diabetes Data Dashboard", layout="wide")
st.title("🩺 Diabetes Data Analysis Dashboard")
st.markdown("""
Welcome! This dashboard provides an easy-to-understand, interactive analysis of the diabetes dataset.
Explore the data, visualize trends, and gain insights!
""")

# Sidebar
st.sidebar.header("Filter Data")
age_range = st.sidebar.slider("Select Age Range", int(df.Age.min()), int(df.Age.max()), (20, 50))
outcome_filter = st.sidebar.selectbox("Diabetes Outcome", options=["All", "Diabetic (1)", "Non-Diabetic (0)"])

filtered_df = df[(df.Age >= age_range[0]) & (df.Age <= age_range[1])]
if outcome_filter == "Diabetic (1)":
    filtered_df = filtered_df[filtered_df.Outcome == 1]
elif outcome_filter == "Non-Diabetic (0)":
    filtered_df = filtered_df[filtered_df.Outcome == 0]

# Show data
with st.expander("Show Raw Data"):
    st.dataframe(filtered_df)

# Key stats
st.subheader("Key Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", len(filtered_df))
col2.metric("Diabetic Cases", int(filtered_df['Outcome'].sum()))
col3.metric("Non-Diabetic Cases", int((filtered_df['Outcome'] == 0).sum()))

# Distribution plots
st.subheader("Feature Distributions")
feature = st.selectbox("Select Feature", options=df.columns[:-1])
fig, ax = plt.subplots()
sns.histplot(filtered_df[feature], kde=True, bins=20, ax=ax, color="skyblue")
ax.set_title(f"Distribution of {feature}")
st.pyplot(fig)

# Correlation heatmap
st.subheader("Correlation Heatmap")
fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.heatmap(filtered_df.corr(), annot=True, cmap="coolwarm", ax=ax2)
st.pyplot(fig2)

# Outcome comparison
st.subheader("Compare Features by Outcome")
feature2 = st.selectbox("Select Feature to Compare", options=df.columns[:-1], key="feature2")
fig3, ax3 = plt.subplots()
sns.boxplot(x="Outcome", y=feature2, data=filtered_df, ax=ax3)
ax3.set_xticklabels(["Non-Diabetic (0)", "Diabetic (1)"])
ax3.set_title(f"{feature2} by Diabetes Outcome")
st.pyplot(fig3)

