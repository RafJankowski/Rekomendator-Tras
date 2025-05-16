import requests
import json
from src.models.geo_position import GeoPosition
from src.models.weather_data import WeatherData
from datetime import datetime
import pprint

class WeatherDataManager:

    def get_weather_data(position: GeoPosition, date_from: datetime, date_to: datetime):

        if date_from == None or date_to == None:

            date_from = datetime.now()
            date_to = datetime.now()

        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": position.latitude,
            "longitude": position.longitude,
            "daily": "temperature_2m_max,temperature_2m_min",
            "hourly": "temperature_2m,relative_humidity_2m,cloud_cover,wind_speed_10m,precipitation_probability",
            "timezone": "auto",
            "start_date": date_from.strftime("%Y-%m-%d"),
            "end_date": date_to.strftime("%Y-%m-%d")
        }
        try:

            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
        
        except Exception as exception:

            raise Exception(f"Błąd przy żądaniu: {exception}")
        
        temperature_max_avg = sum(data["daily"]["temperature_2m_max"]) / len(data["daily"]["temperature_2m_max"])
        temperature_min_avg = sum(data["daily"]["temperature_2m_min"]) / len(data["daily"]["temperature_2m_min"])
        temperature_avg = sum(data["hourly"]["temperature_2m"]) / len(data["hourly"]["temperature_2m"])
        humidity_avg = sum(data["hourly"]["relative_humidity_2m"]) / len(data["hourly"]["relative_humidity_2m"])
        wind_speed_avg = sum(data["hourly"]["wind_speed_10m"]) / len(data["hourly"]["wind_speed_10m"])
        precipitation_propability = sum(data["hourly"]["precipitation_probability"]) / len(data["hourly"]["precipitation_probability"])
        cloud_cover_avg = sum(data["hourly"]["cloud_cover"]) / len(data["hourly"]["cloud_cover"])


        return WeatherData(
            latitude= position.latitude,
            longitude= position.longitude,
            date_from= date_from,
            date_to= date_to,
            temperature_max_avg= temperature_max_avg,
            temperature_min_avg= temperature_min_avg,
            temperature_avg= temperature_avg,
            humidity_avg= humidity_avg,
            wind_speed_avg= wind_speed_avg,
            precipitation_propability= precipitation_propability,
            cloud_cover_avg= cloud_cover_avg
        )
