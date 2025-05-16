import unittest
from datetime import datetime
from src.models.weather_data import WeatherData

class TestWeatherData(unittest.TestCase):

    def test_getting_weather_data_from_api_with_invalid_coordinates(self):

        with self.assertRaises(Exception):

            WeatherData(-1000, -1000, datetime.now())