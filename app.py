import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ----------------------------
# Page Config
# ----------------------------

st.set_page_config(
    page_title="Student Dashboard",
    layout="wide"
)

st.title("📊 Real-Time Student Dashboard")

# ----------------------------
# Sample Dataset
# ----------------------------

data = {
    "Name": ["Aman", "Riya", "Karan", "Priya"],
    "Department": ["CS", "IT", "CS", "ECE"],
    "Marks": [85, 78, 92, 70],
    "Attendance": [90, 88, 95, 80]
}

df = pd.DataFrame(data)

# ----------------------------
# Simulate Live Data
# ----------------------------

df["Marks"] = df["Marks"] + np.random.randint(-2, 3, size=len(df))

# ----------------------------
# Metrics
# ----------------------------

col1, col2 = st.columns(2)

col1.metric("Average Marks", round(df["Marks"].mean(), 2))
col2.metric("Highest Marks", df["Marks"].max())

# ----------------------------
# Table
# ----------------------------

st.subheader("Student Data")

st.dataframe(df)

# ----------------------------
# Chart
# ----------------------------

fig = px.bar(
    df,
    x="Name",
    y="Marks",
    color="Department",
    title="Student Marks"
)

st.plotly_chart(fig, use_container_width=True)

st.success("Dashboard Running Successfully ✅")