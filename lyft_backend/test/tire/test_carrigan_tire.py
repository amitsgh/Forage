import unittest

from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_need_service_true(self):
        tire_wear_array = [0.2, 0.8, 0.9, 0.9]

        tire = CarriganTire(tire_wear_array)
        self.assertTrue(tire.tire_needs_service())
    
    def test_need_service_false(self):
        tire_wear_array = [0.2, 0.8, 0.8, 0.1]

        tire = CarriganTire(tire_wear_array)
        self.assertFalse(tire.tire_needs_service())
