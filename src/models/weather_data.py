from datetime import datetime
import requests
from urllib.parse import urlencode

class WeatherData:

    def __init__(self, 
                 longitude: float, 
                 latitude: float, 
                 temperature_max_avg: float,
                 temperature_min_avg: float,
                 temperature_avg: float,
                 humidity_avg: float,
                 wind_speed_avg: float,
                 precipitation_propability: float,
                 cloud_cover_avg: float,
                 date_from: datetime = None,
                 date_to: datetime = None):
        
        self.__latitude = latitude
        self.__longitude = longitude
        self.__date_from = date_from
        self.__date_to = date_to
        self.__temperature_max_avg = temperature_max_avg
        self.__temperature_min_avg = temperature_min_avg
        self.__temperature_avg = temperature_avg
        self.__humidity_avg = humidity_avg
        self.__wind_speed_avg = wind_speed_avg
        self.__precipitation_propability = precipitation_propability
        self.__cloud_cover_avg = cloud_cover_avg

    @property
    def latitude(self):
        return self.__latitude

    @property
    def longitude(self):
        return self.__longitude

    @property
    def date_from(self):
        return self.__date_from

    @property
    def date_to(self):
        return self.__date_to

    @property
    def temperature_max_avg(self):
        return self.__temperature_max_avg

    @property
    def temperature_min_avg(self):
        return self.__temperature_min_avg

    @property
    def temperature_avg(self):
        return self.__temperature_avg

    @property
    def humidity_avg(self):
        return self.__humidity_avg

    @property
    def wind_speed_avg(self):
        return self.__wind_speed_avg

    @property
    def precipitation_propability(self):
        return self.__precipitation_propability

    @property
    def cloud_cover_avg(self):
        return self.__cloud_cover_avg
    