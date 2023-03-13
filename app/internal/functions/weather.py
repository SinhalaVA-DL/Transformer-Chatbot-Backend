import datetime as dt
import requests
from app import config
from .translator import translateSinhala

global_settings = config.get_settings()

API_KEY = global_settings.weather_apiKey



Base_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Colombo"

url = Base_URL + "&appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()


def kelvinToCelsius(temp):
    return str(int(temp - 273.15)) + "°C"

def getWeather():
    weather_result = translateSinhala(response['weather'][0]['description'])
    result = "අද "+ weather_result+ " සහිත කාලගුණයක් බලාපොරොත්තු වෙන්න පුළුවන් "
    return result








