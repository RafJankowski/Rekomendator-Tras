import unittest
from src.models.route import RoutePoint
import uuid as uuid_module

class TestRoutePoint(unittest.TestCase):

    def test_calculating_distance_between_two_points(self):

        test_variables = [
            (RoutePoint(2.5, 3, str(uuid_module.uuid4())), RoutePoint(5.5, 8, str(uuid_module.uuid4())), 5.830951),
            (RoutePoint(0, 0, str(uuid_module.uuid4())), RoutePoint(3, 4, str(uuid_module.uuid4())), 5.0),
            (RoutePoint(-1, -1, str(uuid_module.uuid4())), RoutePoint(-4, -5, str(uuid_module.uuid4())), 5.0),
            (RoutePoint(10, 10, str(uuid_module.uuid4())), RoutePoint(13, 14, str(uuid_module.uuid4())), 5.0),
            (RoutePoint(1.1, 2.2, str(uuid_module.uuid4())), RoutePoint(3.3, 4.4, str(uuid_module.uuid4())), 3.111269)
        ]
        for case in test_variables:
            
            distance = case[0].calculate_distance_to(case[1])
            self.assertAlmostEqual(distance, case[2], places=5)

