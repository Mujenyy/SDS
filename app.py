import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os
import calendar
from datetime import datetime

st.set_page_config(page_title="Smart Power Scheduler", page_icon="🔋")

st.title("🔋 Smart Power Scheduler (SDG 7: Affordable and Clean Energy)")
st.write("""
This app predicts efficient electricity usage periods 
based on real or simulated hourly data over multiple days.
""")

# --- Automatically load local CSV ---
data_path = os.path.join("data", "energy_data.csv")

if os.path.exists(data_path):
    st.info(f"Using data file: `{data_path}`")
    data = pd.read_csv(data_path)
else:
    st.warning("No CSV found in /data — using simulated data instead.")
    # fallback: generate 7 days of simulated data
    days = np.arange(1, 8)
    hours = np.arange(0, 24)
    records = []
    for d in days:
        daily_pattern = 0.3 + 1.8 * np.exp(-((hours - 13)**2) / 40) + np.random.uniform(0, 0.2, 24)
        for h, e in zip(hours, daily_pattern):
            records.append([d, 10, 2025, h, round(e, 2)])
    data = pd.DataFrame(records, columns=["Day", "Month", "Year", "Hour", "Consumption (kWh)"])

# --- Check CSV columns ---
required_cols = {"Day", "Month", "Year", "Hour", "Consumption (kWh)"}
if not required_cols.issubset(set(data.columns)):
    st.error(f"CSV must contain columns: {required_cols}")
    st.stop()

# --- Convert numeric month to name ---
data["Month Name"] = data["Month"].apply(lambda m: calendar.month_name[int(m)])

# --- Combine columns into a datetime for sorting ---
data["Datetime"] = data.apply(
    lambda r: datetime(int(r["Year"]), int(r["Month"]), int(r["Day"]), int(r["Hour"])), axis=1
)
data = data.sort_values("Datetime").reset_index(drop=True)

# --- Display Data ---
st.subheader("📊 Full Energy Use Log (7 Days, Hourly)")
st.write("Below is the dataset used for prediction:")

# Add a checkbox to toggle full view
show_full = st.checkbox("Show full CSV data")

# Reorder columns for better readability
display_cols = ["Year", "Month Name", "Day", "Hour", "Consumption (kWh)", "Datetime"]

if show_full:
    st.dataframe(data[display_cols], use_container_width=True, hide_index=True)
else:
    st.dataframe(data[display_cols].head(20), use_container_width=True, hide_index=True)
    st.caption("Showing first 20 rows — check the box above to view full dataset.")

# --- Compute average consumption per hour ---
avg_hourly = data.groupby("Hour")["Consumption (kWh)"].mean().reset_index()
best_hour = int(avg_hourly.loc[avg_hourly["Consumption (kWh)"].idxmin(), "Hour"])

# --- Train Linear Regression model ---
X = np.arange(len(data)).reshape(-1, 1)
y = data["Consumption (kWh)"].values
model = LinearRegression().fit(X, y)
pred = model.predict(X)

# --- Visualization ---
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(data["Datetime"], data["Consumption (kWh)"], "bo-", label="Actual Usage")
ax.plot(data["Datetime"], pred, "r--", label="Predicted Trend")
ax.set_xlabel("Date and Hour")
ax.set_ylabel("Energy Use (kWh)")
ax.set_title("Hourly Energy Consumption Over Time")
plt.xticks(rotation=45)
ax.legend()
st.pyplot(fig)

# --- Hourly pattern plot ---
st.subheader("🕒 Average Hourly Consumption Pattern")
fig2, ax2 = plt.subplots(figsize=(8, 4))
ax2.bar(avg_hourly["Hour"], avg_hourly["Consumption (kWh)"], color="skyblue")
ax2.axvline(best_hour, color="red", linestyle="--", label=f"Optimal Hour: {best_hour:02d}:00")
ax2.set_xlabel("Hour of Day")
ax2.set_ylabel("Average Consumption (kWh)")
ax2.set_title("Average Energy Use per Hour of Day")
ax2.legend()
st.pyplot(fig2)

# --- Recommendation ---
st.subheader("✅ Recommendation")
st.success(f"Most energy-efficient time to use appliances: **around {best_hour:02d}:00**")

st.caption("This supports SDG 7 by identifying the daily hour with lowest average demand for efficient energy use.")
