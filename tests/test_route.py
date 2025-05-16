import unittest
from src.models.route import Route
from src.models.route import RoutePoint
from pprint import pprint
import uuid as uuid_module
import re

class TestRoute(unittest.TestCase):

    def setUp(self):
        self.route_points = {
            0: RoutePoint(0, 0, "Start"),
            1: RoutePoint(3, 4, "End")
        }
        self.tags = {"mountain", "scenic"}
        self.route = Route(
            name="Test Route",
            region="Tatry",
            difficulty=1,
            terrain_type="górzysty",
            description="Test description",
            route_points=self.route_points.copy(),
            tags=self.tags.copy(),
            uuid=str(uuid_module.uuid4())
        )

    def test_name_setter_and_getter(self):
        self.route.name = "A" * 350
        self.assertEqual(len(self.route.name), 300)

    def test_region_setter_and_getter(self):
        self.route.region = "Pomorze"
        self.assertEqual(self.route.region, "Pomorze")
        with self.assertRaises(ValueError):
            self.route.region = ""

    def test_difficulty_setter_and_getter(self):
        self.route.difficulty = 1
        self.assertEqual(self.route.difficulty, 1)
        with self.assertRaises(ValueError):
            self.route.difficulty = 999

    def test_terrain_type_setter_and_getter(self):
        self.route.terrain_type = "górzysty"
        self.assertEqual(self.route.terrain_type, "górzysty")
        with self.assertRaises(ValueError):
            self.route.terrain_type = "marsjański"

    def test_description_setter_and_getter(self):
        self.route.description = "B" * 350
        self.assertEqual(len(self.route.description), 300)

    def test_tags_add_and_get(self):
        self.route.add_tag("new_tag")
        self.assertIn("new_tag", self.route.tags)

    def test_set_route_point(self):
        new_point = RoutePoint(10, 10, "Midpoint")
        self.route.set_route_point(2, new_point)
        self.assertIn(2, self.route.route_points)
        self.assertEqual(self.route.route_points[2], new_point)

    def test_get_route_length(self):
        self.route._points = [self.route_points[0], self.route_points[1]]
        self.assertEqual(self.route.get_route_length(), 5)