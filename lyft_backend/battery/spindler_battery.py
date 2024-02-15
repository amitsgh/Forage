from datetime import datetime
from battery.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date) -> None:
        self.current_date = current_date
        self.last_service_date = last_service_date

    def battery_needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 3)
        return service_threshold_date < self.current_date
