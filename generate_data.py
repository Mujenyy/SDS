import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

try:
    # --- Folder setup ---
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)
    print(f"📁 Data folder ready at: {os.path.abspath(data_dir)}")

    # --- Settings ---
    start_date = datetime(2025, 10, 1, 0, 0, 0)  # Start date & time
    total_hours = 7 * 24  # 1 week of hourly data (168 rows)

    # --- Generate timestamps for every hour ---
    timestamps = [start_date + timedelta(hours=i) for i in range(total_hours)]

    # --- Simulate realistic energy consumption ---
    # More use in the afternoon, less at night; adds small daily drift
    energy_use = []
    for i, t in enumerate(timestamps):
        hour = t.hour
        day_factor = 1 + 0.1 * np.sin(i / 24)  # small variation per day
        base = 0.4 + 1.8 * np.exp(-((hour - 13) ** 2) / 40)  # daily shape
        noise = np.random.uniform(0, 0.2)
        energy_use.append(base * day_factor + noise)

    # --- Build DataFrame ---
    data = pd.DataFrame({
        "Day": [t.day for t in timestamps],
        "Month": [t.month for t in timestamps],
        "Year": [t.year for t in timestamps],
        "Hour": [t.hour for t in timestamps],
        "Consumption (kWh)": np.round(energy_use, 2)
    })

    # --- Save file ---
    file_path = os.path.join(data_dir, "energy_data.csv")
    data.to_csv(file_path, index=False)

    print(f"✅ energy_data.csv generated with {len(data)} hourly logs (7 days total)")
    print(f"📂 Saved to: {os.path.abspath(file_path)}")

except Exception as e:
    print(f"❌ Error: {e}")
