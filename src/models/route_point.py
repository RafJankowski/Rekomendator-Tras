import uuid as uuid_module
from src.models.geo_position import GeoPosition

class RoutePoint(GeoPosition):

    def __init__(self, 
                 latitude: float,
                 longitude: float,
                 number_in_order: int = 0, 
                 point_desc: str = ""):
        
        super().__init__(latitude, longitude)
        self._number_in_order = number_in_order
        self._point_desc = point_desc

    @property
    def number_in_order(self):

        return self._number_in_order

    @property
    def point_desc(self):

        return self._point_desc