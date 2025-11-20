import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("raw_weather.csv")

# Cleaning
df["time"] = pd.to_datetime(df["time"])
df.dropna(inplace=True)

# 1. Summary statistics
print(df.describe())

# 2. Temperature trend
plt.figure()
plt.plot(df["time"], df["temperature"])
plt.title("Temperature Trend")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Humidity trend
plt.figure()
plt.plot(df["time"], df["humidity"])
plt.title("Humidity Trend")
plt.xlabel("Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Wind speed trend
plt.figure()
plt.plot(df["time"], df["wind_speed"])
plt.title("Wind Speed Trend")
plt.xlabel("Time")
plt.ylabel("Wind Speed (m/s)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Correlation matrix
print("Correlation matrix:")
print(df[["temperature", "humidity", "wind_speed"]].corr())

df.to_csv("clean_weather.csv", index=False)

print("Cleaned data saved to clean_weather.csv")
