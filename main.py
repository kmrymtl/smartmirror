import tkinter as tk
import requests
import random
from datetime import datetime


#LAYOUT
root = tk.Tk() 
#root.geometry("800x500") #for development
root.attributes('-fullscreen', True)
root.config(bg="black")
padding = 10

def exit(event): #If you bind an event, it will pass event information to the function meaning that the function should expect at least 1 argument. Here event is arbitrary
    """Exit the program with mouse left click"""
    root.destroy()

root.bind('<Button-1>', exit)   
 
#COMPLIMENT   
compliments = ["Hello Gorgeous", "You look amazing", "You look sharp today", "Hi Beautiful", "Damn!"]
     
compliment_label = tk.Label(root, text = random.choice(compliments), bg = "black", fg = "white", font = ("Helvetica", 36))
compliment_label.place(relx = 0.5, rely = 0.5, anchor = "center")

def update_compliment():
    """Update the compliment every 24h""" 
    
    compliment_label.config(text = random.choice(compliments))
    compliment_label.after(86400000,update_compliment)

#DATE AND TIME
today = datetime.now()
today = today.strftime("%A %d %B, %Y \n %H:%M:%S")

today_label = tk.Label(root, text = today, bg = "black", fg = "white", font = ("Helvetica", 26))
today_label.place(relx = 0.01, rely = 0.01, anchor = "nw")
    
def update_datetime():
    """Update the time every minute"""
    
    today_label.config(text = datetime.now().strftime("%A %d %B, %Y \n %H:%M:%S"))
    today_label.after(60000,update_datetime)
    

#WEATHER 
def update_weather():
    """Update the weather every 12 hours"""
 
    CITY = "montreal"
    API_KEY_WEATHER = "MY API KEY"

    parameters_weather = {
        "q" : CITY,
        "appid" : API_KEY_WEATHER
    }

    try:
        weather = requests.get("https://api.openweathermap.org/data/2.5/weather?", params = parameters_weather)
        current_weather = weather.json()["weather"][0]["description"]
    except:
        current_weather = "Error in the API call"

    weather_label = tk.Label(root, text = f"The current weather in {CITY} is \n {current_weather}", bg = "black", fg = "white", font = ("Helvetica", 20))
    weather_label.place(relx = 0.99, rely = 0.01, anchor = "ne")
    weather_label.after(43200000,update_weather)


update_compliment()
update_datetime()
update_weather()
root.mainloop()
