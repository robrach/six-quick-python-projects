import requests
from pprint import pprint

API_Key = '28195b13606ef59939734f585b66d471'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key \
           + "&q=" + city

weather_data = requests.get(base_url).json()

pprint(weather_data)