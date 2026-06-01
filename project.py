# App that uses at least three API's and has a GUI user interface.
# Must return user at least 5 different data points from the API's.
# GUI interface to ask the user for specific information and then request that information from the API sites

import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(city):  