# App that uses at least three API's and has a GUI user interface.
# Must return user at least 5 different data points from the API's.
# GUI interface to ask the user for specific information and then request that information from the API sites


import requests
import tkinter as tk
from tkinter import messagebox 

WEATHER_KEY = "e69c0b311512754758aff3d3fa571a99"
EXCHANGE_KEY = "939b63a0f18cd04f0384f201"


def get_country_info(country):

    url = f"https://restcountries.com/v3.1/name/{country}"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()[0]

    return {
        "country": data["name"]["common"],
        "code": data["cca2"],
        "capital": data["capital"][0],
        "population": data["population"],
        "currency": list(data["currencies"].values())[0]["name"]
    }


def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_KEY}&units=metric"

    print("City being searched:", city)

    response = requests.get(url)

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "desc": data["weather"][0]["description"]
    }

def get_exchange():

    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_KEY}/latest/CAD"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    return data["conversion_rates"]["USD"]



def search():

    country = entry.get()

    if not country:
        messagebox.showerror("Error", "Please enter a country")
        return

    country_data = get_country_info(country)

    if not country_data:
        messagebox.showerror("Error", "Country not found")
        return

    weather_data = get_weather(country_data["capital"])

    if not weather_data:
        messagebox.showerror("Error", "Weather not found")
        return

    exchange_rate = get_exchange()

    result_text.set(
        f"Country: {country_data['country']}\n"
        f"Code: {country_data['code']}\n"
        f"Capital: {country_data['capital']}\n"
        f"Population: {country_data['population']:,}\n"
        f"Currency: {country_data['currency']}\n\n"
        f"Temperature: {weather_data['temp']}°C\n"
        f"Humidity: {weather_data['humidity']}%\n"
        f"Weather: {weather_data['desc']}\n\n"
        f"1 CAD = {exchange_rate} USD"
    )


# GUI Application
window = tk.Tk()
window.title("Country Info App")

entry = tk.Entry(window)
entry.pack()

tk.Button(window, text="Search", command=search).pack(pady=10)

result_text = tk.StringVar() # Create a StringVar to hold the result text

tk.Label(window, textvariable=result_text, justify="left").pack(pady=10)

window.mainloop() 
