import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("clean_weather.csv")
df["time"] = pd.to_datetime(df["time"])

st.title("Karachi Weather Analytics Dashboard")

st.subheader("Raw Clean Data")
st.dataframe(df)

# Temperature
st.subheader("Temperature Trend")
fig1, ax1 = plt.subplots()
ax1.plot(df["time"], df["temperature"])
st.pyplot(fig1)

# Humidity
st.subheader("Humidity Trend")
fig2, ax2 = plt.subplots()
ax2.plot(df["time"], df["humidity"])
st.pyplot(fig2)

# Wind speed
st.subheader("Wind Speed Trend")
fig3, ax3 = plt.subplots()
ax3.plot(df["time"], df["wind_speed"])
st.pyplot(fig3)

# Correlation
st.subheader("Correlation Matrix")
st.write(df[["temperature", "humidity", "wind_speed"]].corr())
