from engine.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on) -> None:
        self.warning_light_is_on = warning_light_is_on

    def engine_needs_service(self) -> bool:
        return self.warning_light_is_on
