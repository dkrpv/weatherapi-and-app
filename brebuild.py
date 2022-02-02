import requests
import json

with open("apikey.txt", "r") as file:
    key = file.readline()
    pass

api_key = str(key)[:-1]
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def weather(city, what):
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        if what == "temp":
            return current_temperature
        if what == "pressure":
            return current_pressure
        if what == "humidity":
            return current_humidity
        if what == "description":
            return weather_description
        else:
            return "invalid request"


def toCelsius(x, measure):
    if (measure.lower()) == "kelvin":
        return (x - 273.15)
    if (measure.lower()) == "fahrenheit":
        return (x - 32) * 5/9


w1 = weather("Moscow", "temp")
print(toCelsius(w1, "kelvin"))
