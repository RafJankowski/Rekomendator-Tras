from __future__ import annotations
from math import sqrt

class GeoPosition:

    _LATITUDE_TO_KM = 111.32
    _LONGITUDE_TO_KM = 111.32
    def __init__(self, 
                 latitude: float, 
                 longitude: float,
                 height_above_sea_level: float = None):
        
        self._latitude = latitude
        self._longitude = longitude
        self._height = height_above_sea_level

    @property
    def latitude(self) -> float:

        return self._latitude

    @latitude.setter
    def latitude(self, value: float):

        self._latitude = value

    @property
    def longitude(self) -> float:

        return self._longitude

    @longitude.setter
    def longitude(self, value: float):

        self._longitude = value

    @property
    def height(self) -> float | None:

        return self._height

    @height.setter
    def height(self, value: float):

        self._height = value

    
    def calculate_distance_to(self, position: GeoPosition):

        horizontal_distance = (position.latitude - self.latitude) * self._LATITUDE_TO_KM
        vertical_distance = (position.longitude - self.longitude) * self._LATITUDE_TO_KM
        height_distance = (position.height or 0) - (self.height or 0)
        return sqrt(horizontal_distance ** 2 + vertical_distance ** 2 + height_distance ** 2)
