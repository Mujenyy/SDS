# 🔋 Smart Power Scheduler (SDG 7: Affordable and Clean Energy)

### 🎯 Overview
The Smart Power Scheduler helps users identify the most energy-efficient time of day to use electricity.  
By simulating energy consumption and applying a simple AI model, it supports **SDG 7** — promoting clean and affordable energy.

### 🧠 Technologies Used
- **Python**
- **Streamlit** – Interactive web dashboard
- **Scikit-learn** – Linear Regression model
- **Matplotlib** – Visualization
- **Pandas/Numpy** – Data handling

### ⚙️ How It Works
1. The system generates 24-hour energy usage data or loads from `energy_data.csv`.
2. A simple ML model predicts future usage trends.
3. The app identifies the **lowest usage hour** (best time to use appliances).
4. Results and graphs are displayed on the Streamlit dashboard.

### 🚀 How to Run
1. Install dependencies:  
