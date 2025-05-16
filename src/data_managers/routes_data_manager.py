import pathlib
import sqlite3
from src.models.route import Route
from src.models.route_point import RoutePoint
import pprint

class RoutesDataManager:

    _DATABASE_DIR = pathlib.Path(__file__).parent / ".." / "data" / "sqlite.db"
    def get_all(max_difficulty: int = None):

        connection = sqlite3.connect(RoutesDataManager._DATABASE_DIR)
        connection.row_factory = sqlite3.Row # Zamienia zwracane rekordy na obiekty typu Row, co pozwala na dostęp do kolumn po nazwach. Nieznacznie zmiejsza wydajność!
        cursor = connection.cursor()
        sql = "SELECT * FROM routes_full_view" # Edge loading - pobiera wszystkie relacje N:N z tabelą jednocześnie.
        if max_difficulty:

            sql += f" WHERE "
            if 5 >= max_difficulty >= 0:

                sql += f"difficulty_level <= {max_difficulty}"
            
            else:
                
                ValueError("Trudność musi być liczbą z przedziału 1-5")

        cursor = cursor.execute(sql)
        results = cursor.fetchall()
        connection.close()
        routes = {}
        for record in results:

            current_uuid = record['route_uuid']
            if current_uuid not in routes.keys():

                routes[current_uuid] = Route(
                    name = record['route_name'],
                    region = record['region_name'],
                    route_points = [],
                    difficulty = record['difficulty_level'],
                    terrain_type = record['terrain_type_name'],
                    description = record['route_description'],
                    tags = set(),
                    uuid = current_uuid
                )

            if record['tag_name'] not in routes[current_uuid].tags:

                routes[current_uuid].add_tag(record['tag_name'])

            if record['number_in_order'] not in routes[current_uuid].route_points:

                routes[current_uuid].set_route_point(RoutePoint(
                    latitude=record['latitude'],
                    longitude=record['longitude'],
                    number_in_order=record['number_in_order'],
                    point_desc=record['point_description']
                ))

        return routes
