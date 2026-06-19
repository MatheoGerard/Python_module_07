from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self) -> None:
        self._name: str = ""
        self._type: str = ""

    @abstractmethod
    def attack() -> str:
        pass

    def describe(self) -> str:
        return f"{self._name} is a {self._type} type Creature"
