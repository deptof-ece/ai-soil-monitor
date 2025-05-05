import streamlit as st
import pandas as pd
import numpy as np

st.title("🌱 AI-Assisted Soil Health Monitoring System")

# Simulated sensor data
np.random.seed(42)
df = pd.DataFrame({
    "pH": np.random.uniform(4.5, 8.5, 10),
    "Moisture (%)": np.random.uniform(10, 60, 10),
    "Nitrogen (N)": np.random.uniform(20, 200, 10),
    "Phosphorus (P)": np.random.uniform(10, 150, 10),
    "Potassium (K)": np.random.uniform(10, 150, 10),
    "Crop": np.random.choice(["Wheat", "Tomato", "Maize"], 10)
})

# Recommendation logic
def recommend(row):
    advice = []
    if row["pH"] < 5.5: advice.append("Add lime")
    elif row["pH"] > 7.5: advice.append("Add sulfur")

    if row["Nitrogen (N)"] < 50: advice.append("Add composted manure")
    if row["Moisture (%)"] < 30: advice.append("Use mulch")
    if row["Crop"] == "Tomato" and row["Phosphorus (P)"] < 40: advice.append("Add bone meal")
    if row["Crop"] == "Maize" and row["Potassium (K)"] < 60: advice.append("Add wood ash")
    
    return ", ".join(advice) if advice else "Soil is healthy"

df["AI Recommendation"] = df.apply(recommend, axis=1)

# Display table
st.subheader("📊 Soil Sensor Data & AI Recommendations")
st.dataframe(df)

# Plotting
st.subheader("📉 Visual Soil Analysis")
st.bar_chart(df[["pH", "Moisture (%)", "Nitrogen (N)", "Phosphorus (P)", "Potassium (K)"]])

# Download option
st.download_button("Download Data as CSV", df.to_csv(index=False), "soil_data.csv")
