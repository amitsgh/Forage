from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tire_wear_array) -> None:
        self.tire_wear_array = tire_wear_array

    def tire_needs_service(self):
        return sum(self.tire_wear_array) >= 3
