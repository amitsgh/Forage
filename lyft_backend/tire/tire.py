from abc import ABC, abstractmethod


class Tire(ABC):
    @abstractmethod
    def tire_needs_service(self) -> bool:
        pass
