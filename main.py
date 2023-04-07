import tkinter as tk
import requests
from tkinter import Label, messagebox
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

MAIN_BG = '#bfc0c0'
SEARCH_BG = '#77676d'
VALUES_BG = '#bfc0c0'
FG = '#4F5d75'
API_KEY = os.getenv('APP_ID')
API_URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'

def get_weather_data(city_name):
    try:
        response = requests.get(API_URL.format(city_name, API_KEY))
        response.raise_for_status()
        json_data = response.json()
    except requests.exceptions.HTTPError as error:
        messagebox.showerror("Error", f"Error fetching data: {error}")
        return None
    except requests.exceptions.ConnectionError as error:
        messagebox.showerror("Error", "Error connecting to server")
        return None
    except requests.exceptions.Timeout as error:
        messagebox.showerror("Error", "Request timed out")
        return None
    except requests.exceptions.RequestException as error:
        messagebox.showerror("Error", "Error fetching data")
        return None
    
    return {
        'condition': json_data['weather'][0]['main'],
        'temperature': f"{json_data['main']['temp']}°C",
        'min_temperature': f"{json_data['main']['temp_min']}°C",
        'max_temperature': f"{json_data['main']['temp_max']}°C",
        'pressure': f"{json_data['main']['pressure']}hPa",
        'humidity': f"{json_data['main']['humidity']}%",
        'wind_speed': f"{json_data['wind']['speed']}m/s",
        'sunrise_time': datetime.utcfromtimestamp(json_data['sys']['sunrise'] + json_data['timezone']).strftime('%H:%M'),
        'sunset_time': datetime.utcfromtimestamp(json_data['sys']['sunset'] + json_data['timezone']).strftime('%H:%M'),
    }

def update_weather_data(canvas, data):
    if data is None:
        return
    
    pressure_label.config(text=data['pressure'])
    humidity_label.config(text=data['humidity'])
    wind_speed_label.config(text=data['wind_speed'])
    temperature_label.config(text=data['temperature'])
    min_temp_label.config(text=data['min_temperature'])
    max_temp_label.config(text=data['max_temperature'])
    sunrise_label.config(text=data['sunrise_time'])
    sunset_label.config(text=data['sunset_time'])

def get_weather():
    city_name = city_entry.get()
    weather_data = get_weather_data(city_name)
    update_weather_data(canvas, weather_data)

canvas = tk.Tk()
canvas.geometry("300x500")
canvas.title("Weather App")
canvas.configure(background=MAIN_BG)

title_label = Label(text="Weather App", font=("sans serif", 25, "bold"), bg=MAIN_BG, fg=FG)
title_label.pack(pady=10)

city_entry = tk.Entry(canvas, justify='center', width=20, font=("sans serif", 15, "bold"), bg=SEARCH_BG)
city_entry.pack(pady=5)
city_entry.focus()

search_button = tk.Button(canvas, text="Search", command=get_weather, font=("sans serif", 15, "bold"), bg=SEARCH_BG)
search_button.pack(pady=5)

values_frame = tk.Frame(canvas, bg=VALUES_BG)
values_frame.pack(pady=10)

pressure_label = Label(values_frame, text="Pressure:", font=("sans serif", 15, "bold"), bg=VALUES_BG, fg=FG)
pressure_label.grid(row=0, column=0, padx=10, pady=10)
humidity_label = Label(values_frame, text="Humidity:", font=("sans serif", 15, "bold"), bg=VALUES_BG, fg=FG)
humidity_label.grid(row=1, column=0, padx=10, pady=10)
wind_speed_label = Label(values_frame, text="Wind Speed:", font=("sans serif", 15, "bold"), bg=VALUES_BG, fg=FG)
wind_speed_label.grid(row=2, column=0, padx=10, pady=10)
temperature_label = Label(values_frame, text="Temperature:", font=("sans serif", 15, "bold"), bg=VALUES_BG, fg=FG)
temperature_label.grid(row=3, column=0, padx=10, pady=10)
min_temp_label = Label(values_frame, text="Min Temperature:", font=("sans serif", 15, "bold"), bg=VALUES_BG, fg=FG)
min_temp_label.grid(row=4, column=0, padx=10, pady=10)
max_temp_label = Label(values_frame, text="Max Temperature:", font=("sans serif", 15, "bold"), bg=VALUES_BG, fg=FG)
max_temp_label.grid(row=5, column=0, padx=10, pady=10)
sunrise_label = Label(values_frame, text="Sunrise:", font=("sans serif", 15, "bold"), bg=VALUES_BG, fg=FG)
sunrise_label.grid(row=6, column=0, padx=10, pady=10)
sunset_label = Label(values_frame, text="Sunset:", font=("sans serif", 15, "bold"), bg=VALUES_BG, fg=FG)
sunset_label.grid(row=7, column=0, padx=10, pady=10)

canvas.mainloop()

