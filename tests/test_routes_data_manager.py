from src.data_managers.routes_data_manager import RoutesDataManager
import unittest
from src.models.route import Route
from src.models.route_point import RoutePoint

class TestRoutesDataManager(unittest.TestCase):

    def test_get_all_returns_dict(self):
        routes = RoutesDataManager.get_all()
        self.assertIsInstance(routes, dict)

    def test_get_routes_returns_list_of_routes_objects(self):
        routes = RoutesDataManager.get_all()
        for route in routes.values():
            self.assertIsInstance(route, Route)

    def test_get_all_routes_have_uuid_keys(self):
        routes = RoutesDataManager.get_all()
        for uuid in routes.keys():
            self.assertIsInstance(uuid, str)

    def test_route_has_route_points(self):
        routes = RoutesDataManager.get_all()
        for route in routes.values():
            self.assertIsInstance(route.route_points, dict)
            for point in route.route_points.values():
                self.assertIsInstance(point, RoutePoint)

    def test_route_has_tags(self):
        routes = RoutesDataManager.get_all()
        for route in routes.values():
            self.assertIsInstance(route.tags, set)

    def test_route_has_name_and_description(self):
        routes = RoutesDataManager.get_all()
        for route in routes.values():
            self.assertIsInstance(route.name, str)
            self.assertIsInstance(route.description, str)

    def test_route_has_region_and_terrain_type(self):
        routes = RoutesDataManager.get_all()
        for route in routes.values():
            self.assertIsInstance(route.region, str)
            self.assertIsInstance(route.terrain_type, str)

    def test_route_has_difficulty(self):
        routes = RoutesDataManager.get_all()
        for route in routes.values():
            self.assertIsInstance(route.difficulty, int)

    def test_route_points_have_lat_lon_and_desc(self):
        routes = RoutesDataManager.get_all()
        for route in routes.values():
            for point in route.route_points.values():
                self.assertIsInstance(point.latitude, float)
                self.assertIsInstance(point.longitude, float)
                self.assertIsInstance(point.number_in_order, int)
                self.assertIsInstance(point.point_desc, str)

    def test_get_types_table_for_tags_returns_dict(self):
        tags = RoutesDataManager.get_types_table_for('tags')
        self.assertIsInstance(tags, dict)
        for key, value in tags.items():
            self.assertIsInstance(key, int)
            self.assertIsInstance(value, str)

    def test_get_types_table_for_invalid_table_raises(self):
        with self.assertRaises(ValueError):
            RoutesDataManager.get_types_table_for('invalid_table')

    def test_get_types_table_for_regions_returns_dict(self):
        regions = RoutesDataManager.get_types_table_for('regions')
        self.assertIsInstance(regions, dict)
        for key, value in regions.items():
            self.assertIsInstance(key, int)
            self.assertIsInstance(value, str)

    def test_get_types_table_for_terrain_types_returns_dict(self):
        terrain_types = RoutesDataManager.get_types_table_for('terrain_types')
        self.assertIsInstance(terrain_types, dict)
        for key, value in terrain_types.items():
            self.assertIsInstance(key, int)
            self.assertIsInstance(value, str)

    def test_route_tags_are_non_empty(self):
        routes = RoutesDataManager.get_all()
        for route in routes.values():
            self.assertTrue(len(route.tags) > 0)

    def test_route_points_numbers_are_unique(self):
        routes = RoutesDataManager.get_all()
        for route in routes.values():
            numbers = [point.number_in_order for point in route.route_points.values()]
            self.assertEqual(len(numbers), len(set(numbers)))

    def test_route_points_have_valid_coordinates(self):
        routes = RoutesDataManager.get_all()
        for route in routes.values():
            for point in route.route_points.values():
                self.assertGreaterEqual(point.latitude, -90)
                self.assertLessEqual(point.latitude, 90)
                self.assertGreaterEqual(point.longitude, -180)
                self.assertLessEqual(point.longitude, 180)