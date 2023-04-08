import streamlit as st
import requests
import os
import datetime
import fontawesome as fa
import streamlit.components.v1 as components


from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('APP_ID')

sunrise_icon = '<i class="fa-solid fa-sunrise fa-beat-fade"></i>'


st.title("Weather App")

city = st.text_input("Enter city name")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"

response = requests.get(url)

data = response.json()


if data["cod"] != "404":
    st.write("Current temperature:", data['main']['temp'])
    st.write("Current Wind Speed:", data["wind"]["speed"])
    st.write("Current Weather:", data["weather"][0]["description"])
    components.html(sunrise_icon, height=20, width=20)
    st.write("Sunrise:", datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M'))
    st.write("Sunset:", datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M'))
    #st.write(f"{fa.icons['sun-o']} Sunrise: {datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M')}")


    
    #st.write("Current Weather:", data)

  
else:
    st.write("City not found")
