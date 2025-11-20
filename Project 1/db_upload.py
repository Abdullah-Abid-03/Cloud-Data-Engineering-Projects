import sqlite3
import pandas as pd

# Load cleaned CSV
df = pd.read_csv("clean_weather.csv")

# Connect or create SQLite DB file
conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS WeatherData (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time TEXT,
    temperature REAL,
    humidity REAL,
    wind_speed REAL
)
""")

# Insert each row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO WeatherData (time, temperature, humidity, wind_speed)
        VALUES (?, ?, ?, ?)
    """, (
        row.time,
        row.temperature,
        row.humidity,
        row.wind_speed
    ))

conn.commit()
conn.close()

print("Data uploaded to weather.db successfully.")

