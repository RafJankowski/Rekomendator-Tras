import unittest
from src.models.geo_position import GeoPosition
import uuid as uuid_module

class TestRoutePoint(unittest.TestCase):

    def test_latitude_and_longitude_properties(self):
        pos = GeoPosition(10.0, 20.0)
        self.assertEqual(pos.latitude, 10.0)
        self.assertEqual(pos.longitude, 20.0)

        pos.latitude = 15.0
        pos.longitude = 25.0
        self.assertEqual(pos.latitude, 15.0)
        self.assertEqual(pos.longitude, 25.0)

    def test_height_property_not_set(self):
        pos = GeoPosition(10.0, 20.0)
        self.assertEqual(pos.height, None)

    def test_height_property(self):
        pos = GeoPosition(10.0, 20.0, 100.0)
        self.assertEqual(pos.height, 100.0)

    def test_calculate_distance_to_without_height(self):
        pos1 = GeoPosition(0.0, 0.0)
        pos2 = GeoPosition(3.0, 4.0)
        distance = pos1.calculate_distance_to(pos2)
        self.assertAlmostEqual(distance, 5.0)

    def test_calculate_distance_to_with_height(self):
        pos1 = GeoPosition(0.0, 0.0, 0.0)
        pos2 = GeoPosition(0.0, 0.0, 5.0)
        distance = pos1.calculate_distance_to(pos2)
        self.assertAlmostEqual(distance, 5.0)

    def test_calculate_distance_to_with_all_coordinates(self):
        pos1 = GeoPosition(1.0, 2.0, 2.0)
        pos2 = GeoPosition(4.0, 6.0, 5.0)
        distance = pos1.calculate_distance_to(pos2)
        self.assertAlmostEqual(distance, 34 ** 0.5)

