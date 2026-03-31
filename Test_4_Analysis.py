import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("motor_control_performance_dataset_with_target.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Convert needed columns to numeric
df["Time (s)"] = pd.to_numeric(df["Time (s)"], errors="coerce")
df["Speed (RPM)"] = pd.to_numeric(df["Speed (RPM)"], errors="coerce")
df["Torque (Nm)"] = pd.to_numeric(df["Torque (Nm)"], errors="coerce")

# Drop bad rows
df = df.dropna(subset=["Time (s)", "Speed (RPM)", "Torque (Nm)"])

# Optional smoothing
df["Speed_smooth"] = df["Speed (RPM)"].rolling(window=5, min_periods=1).mean()
df["Torque_smooth"] = df["Torque (Nm)"].rolling(window=5, min_periods=1).mean()

# Speed graph
plt.figure(figsize=(10,5))
plt.plot(df["Time (s)"], df["Speed (RPM)"], label="Raw Speed")
plt.plot(df["Time (s)"], df["Speed_smooth"], label="Smoothed Speed")
plt.xlabel("Time (s)")
plt.ylabel("Speed (RPM)")
plt.title("Speed vs Time")
plt.grid(True)
plt.legend()
plt.show()

# Torque graph
plt.figure(figsize=(10,5))
plt.plot(df["Time (s)"], df["Torque (Nm)"], label="Raw Torque")
plt.plot(df["Time (s)"], df["Torque_smooth"], label="Smoothed Torque")
plt.xlabel("Time (s)")
plt.ylabel("Torque (Nm)")
plt.title("Torque vs Time")
plt.grid(True)
plt.legend()
plt.show()