import requests
from pprint import pprint

import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API_Key = config('API_Key')   # API_Key = "..." is in the .env file (for security reasons)

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key \
           + "&q=" + city

weather_data = requests.get(base_url).json()

pprint(weather_data)