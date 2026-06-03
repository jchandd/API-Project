# App that uses at least three API's and has a GUI user interface.
# Must return user at least 5 different data points from the API's.
# GUI interface to ask the user for specific information and then request that information from the API sites

import requests
import tkinter as tk
from tkinter import messagebox 

GEODB_KEY = "1b97151aeamshcf5fbd1af73bedbp1535c6jsn90121c4a713a"
WEATHER_KEY = "cc96d68c73cf139304a381905f85826e"
EXCHANGE_KEY = ""


def get_country_info(country):

    url = f"https://wft-geo-db.p.rapidapi.com/v1/geo/countries?namePrefix={country}"

    headers = {
        "X-RapidAPI-Key": GEODB_KEY,
        "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)  # Make the API request with the headers for authentication

    if response.status_code != 200: 
        return None

    data = response.json()["data"][0]

    return {
        "country": data["name"],
        "code": data["code"],
        "capital": data.get("capital", "N/A")
    }


def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_KEY}&units=metric"

    response = requests.get(url) 

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "desc": data["weather"][0]["description"] # Get the weather description from the API response
    }

def get_exchange():

    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_KEY}/latest/CAD"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    return data["conversion_rates"]["USD"]
