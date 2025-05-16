from __future__ import annotations #daje możliwość typehintowania klasy wewnątrz jej metod
import uuid as uuid_module
from math import sqrt
from src.models.route_point import RoutePoint
from src.models.geo_position import GeoPosition

class Route():

    def __init__(self, 
                 name: str, 
                 region: str, 
                 difficulty: int,
                 terrain_type: str,
                 description: str,
                 route_points: list = [],
                 tags: set = None,
                 uuid: str = str(uuid_module.uuid4())):

        self._name = name
        self._region = region
        self._route_points = route_points
        self._difficulty = difficulty
        self._terrain_type = terrain_type
        self._description = description
        self._tags = tags if tags is not None else set()
        self._uuid = uuid
    
    @property
    def name(self):

        return self._name
    
    @name.setter
    def name(self, name):

        if(len(name) > 300):

            raise Warning("Ta wartość może mieć maksymalną długość 300 znaków, Reszta znaków zostanie obcięta przy zapisywaniu!")
        
        self._name = name[:300]

    @property
    def region(self):

        return self._region
    
    @region.setter
    def region(self, region):

        self._region = region
    
    @property
    def route_points(self):

        return self._route_points.copy()
    
    def add_route_point(self, route_point: RoutePoint):

        self._route_points.append(route_point)

    def set_route_point(self, route_point: RoutePoint):

        self._route_points.append(route_point)


    def delete_route_point(self, index: int):

        if 0 <= index < len(self._route_points):

            del self._route_points[index]

        else:

            raise IndexError("Index poza zakresem listy punktów trasy.")

    @property
    def difficulty(self):

        return self._difficulty
    
    @difficulty.setter
    def difficulty(self, difficulty):

        if 6 > difficulty > 0:

            raise ValueError("Trudność trasy musi być jedną z wartością od 1 do 5") 
    
        self._difficulty = difficulty

    @property
    def terrain_type(self):

        return self._terrain_type
    
    @terrain_type.setter
    def terrain_type(self, terrain_type):
    
        self._terrain_type = terrain_type

    @property
    def description(self):

        return self._description
    
    @description.setter
    def description(self, description):

        if(len(description) > 300):

            raise Warning("Ta wartość może mieć maksymalną długość 300 znaków, Reszta znaków zostanie obcięta przy zapisywaniu!")
        
        if(not isinstance(description, str)):

            raise ValueError("Description musi być typu string")
        
        self._description = description[:300]

    @property
    def tags(self):
        return self._tags.copy()

    def add_tag(self, tag):

        self._tags.add(tag)

    def remove_tag(self, tag):
        
        self._tags.remove(tag)

    @property
    def uuid(self):

        return self._uuid
    
    def get_route_length(self):

        if len(self._route_points) < 2:

            return 0
        
        length = 0
        for i in range(len(self._route_points) - 1):

            length += self._route_points[i].calculate_distance_to(self._route_points[i + 1])

        return length
    
    def get_time_to_complete(self):
        
        speed = 5.0
        difficulty_factor = max(0.4, 1 - (self._difficulty - 1) * 0.15)
        effective_speed = speed * difficulty_factor

        return self.get_route_length() / effective_speed
    
    def calculate_mid_point(self) -> GeoPosition | bool:

        if len(self._route_points) == 0:

            return False

        mid_lat = sum(point.latitude for point in self._route_points) / len(self._route_points)
        mid_lon = sum(point.longitude for point in self._route_points) / len(self._route_points)

        return GeoPosition(mid_lat, mid_lon)
