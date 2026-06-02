# App that uses at least three API's and has a GUI user interface.
# Must return user at least 5 different data points from the API's.
# GUI interface to ask the user for specific information and then request that information from the API sites

import requests
import tkinter as tk
from tkinter import messagebox

GEODB_KEY = ""
WEATHER_KEY = ""
EXCHANGE_KEY = ""


def get_country_info(country):

    url = f"https://wft-geo-db.p.rapidapi.com/v1/geo/countries?namePrefix={country}"

    headers = {
        "X-RapidAPI-Key": GEODB_KEY,
        "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json()["data"][0]

    return {
        "country": data["name"],
        "code": data["code"],
        "capital": data.get("capital", "N/A")
    }
