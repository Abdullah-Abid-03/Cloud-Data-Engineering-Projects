import requests
import pandas as pd

API_URL = (
    "https://api.open-meteo.com/v1/forecast?"
    "latitude=24.86&longitude=67.01&"
    "hourly=temperature_2m,relativehumidity_2m,wind_speed_10m"
)

response = requests.get(API_URL).json()

hourly = response["hourly"]

df = pd.DataFrame({
    "time": hourly["time"],
    "temperature": hourly["temperature_2m"],
    "humidity": hourly["relativehumidity_2m"],
    "wind_speed": hourly["wind_speed_10m"],
})

df.to_csv("raw_weather.csv", index=False)

print("Raw weather data extracted and saved to raw_weather.csv")
