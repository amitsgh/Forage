import unittest

from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_need_service_true(self):
        tire_wear_array = [0.3, 0.9, 0.9, 0.9]

        tire = OctoprimeTire(tire_wear_array)
        self.assertTrue(tire.tire_needs_service())

    def test_need_service_false(self):
        tire_wear_array = [0.2, 0.9, 0.9, 0.9]

        tire = OctoprimeTire(tire_wear_array)
        self.assertFalse(tire.tire_needs_service())
