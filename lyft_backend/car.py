class Car:
    def __init__(self, engine, battery, tire) -> None:
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self) -> bool:
        return self.engine.engine_needs_service() or self.battery.battery_needs_service() or self.tire.tire_needs_service()
