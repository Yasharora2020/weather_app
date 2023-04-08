import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('APP_ID')

st.title("Weather App")

city = st.text_input("Enter city name")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"

response = requests.get(url)

data = response.json()


if data["cod"] != "404":
    st.write("Current temperature:", data["main"]["temp"])
    st.write("Current temperature:", data)

   # st.write("Weather description:", data["weather"][0]["description"])
    #st.write("Wind speed:", data["wind"]["speed"])
else:
    st.write("City not found")
