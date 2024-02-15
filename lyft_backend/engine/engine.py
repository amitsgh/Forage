from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def engine_needs_service(self) -> bool:
        pass
