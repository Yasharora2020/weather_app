import tkinter as tk
import requests
import time
from tkinter import Label
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&units=metric&appid="+str(os.getenv('APP_ID'))
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = str(json_data['main']['temp']) +str("°C")
    min = str(json_data['main']['temp_min']) + str("°C")
    max = str(json_data['main']['temp_max']) + str("°C")
    pressure = str(json_data['main']['pressure'])+ str("hPa")
    humidity = str(json_data['main']['humidity']) + str("%")
    wind = str(json_data['wind']['speed']) + str("m/s")
    timezone = int(json_data['timezone'])
    sunrise_utc = int(json_data['sys']['sunrise'])
    sunrise_local = datetime.utcfromtimestamp(sunrise_utc + timezone).strftime('%H:%M')
    sunset_utc = int(json_data['sys']['sunset'])
    sunset_local = datetime.utcfromtimestamp(sunset_utc + timezone).strftime('%H:%M')
    

    p.config(text=pressure)
    h.config(text=humidity)
    w.config(text=wind)
    t.config(text=temp)
    m.config(text=min)
    x.config(text=max)
    s.config(text=sunrise_local)
    z.config(text=sunset_local)
    

mainbg= '#bfc0c0'
searchbg= '#77676d'
valuesbg= '#bfc0c0'
fg='#4F5d75'
canvas = tk.Tk()
canvas.geometry("300x500")
canvas.title("Weather App")
canvas.configure(background=mainbg)
f = ("sans serif", 15, "bold")
t = ("sans serif", 35, "bold")

#logo_image = tk.PhotoImage(file="/Users/Personal/Desktop/codingprojects/weather_api/logo.png")
#logo = Label(image=logo_image)
#logo.place_configure(x=0, y=0, relwidth=1, relheight=1)

temp = Label(text="Temp.:", font=f,bg=valuesbg)
temp.place(x=50,y=100)
t=Label(text="....", font=f, bg=valuesbg)
t.place(x=150,y=100)

pressure= Label(text="Pressure:", font=f, bg=valuesbg)
pressure.place(x=50,y=150)
p=Label(text="....", font=f, bg=valuesbg)
p.place(x=150,y=150)

humidity= Label(text="Humidity:", font=f, bg=valuesbg)
humidity.place(x=50,y=200)
h=Label(text="....", font=f, bg=valuesbg)
h.place(x=150,y=200)

wind=Label(text="Wind Speed:", font=f, bg=valuesbg )
wind.place(x=50,y=250)
w=Label(text="....", font=f, bg=valuesbg)
w.place(x=150,y=250)


min = Label(text="Min Temp.:", font=f, bg=valuesbg)
min.place(x=50,y=300)
m=Label(text="....", font=f, bg=valuesbg)
m.place(x=150,y=300)

maxtemp = Label(text="Max Temp.:", font=f, bg=valuesbg)
maxtemp.place(x=50,y=350)
x=Label(text="....", font=f, bg=valuesbg)
x.place(x=150,y=350)

sunrise= Label(text="Sunrise:", font=f, bg=valuesbg)
sunrise.place(x=50,y=400)
s=Label(text="....", font=f, bg=valuesbg)
s.place(x=150,y=400)

sunset = Label(text="Sunset:", font=f, bg=valuesbg)
sunset.place(x=50,y=450)
z=Label(text="....", font=f, bg=valuesbg)
z.place(x=150,y=450)


textField = tk.Entry(canvas, justify='center', width = 20, font = f, bg = searchbg)
textField.pack(pady = 5)
textField.focus()
textField.bind('<Return>', getWeather)


canvas.mainloop()
