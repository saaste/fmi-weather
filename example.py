import logging
import os

import fmi_weather_client as fmi
from fmi_weather_client.models import Forecast, Weather, WeatherData

log_level = getattr(logging, os.environ.get("LOG_LEVEL", "INFO").upper(), logging.INFO)
logging.basicConfig(level=log_level)


def print_weather(weather: Weather):
    print()
    print(weather.place)
    print("Location: %s, %s" % (weather.lat, weather.lon))
    print_weather_data(weather.data)
    print(" ")


def print_forecast(station_forecast: Forecast):
    print()
    print("Place: %s" % station_forecast.place)
    print("Location: %s, %s" % (station_forecast.lat, station_forecast.lon))
    for weather in station_forecast.forecasts:
        print_weather_data(weather)
        print("  ")


def print_weather_data(weather: WeatherData):
    print(f"  Timestamp: {weather.time}")
    print(f"  Temperature: {weather.temperature}")
    print(f"  Humidity: {weather.humidity}")
    print(f"  Wind speed: {weather.wind_speed}")
    print(f"  Cloud cover: {weather.cloud_cover}")


weather1 = fmi.weather_by_coordinates(60.170998, 24.941325)
weather2 = fmi.weather_by_place_name("Kuopio")
forecast1 = fmi.forecast_by_place_name("Jäppilä, Pieksämäki")
forecast2 = fmi.forecast_by_coordinates(67.6894, 28.62406, timestep_hours=12)

print_weather(weather1)
print_weather(weather2)
print_forecast(forecast1)
print_forecast(forecast2)
