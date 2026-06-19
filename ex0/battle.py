from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, crea_type: str) -> None:
        self._name: str = name
        self._crea_type: str = crea_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self._name} is a {self._crea_type} type Creature"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base() -> "Creature":
        pass

    @abstractmethod
    def create_evolved() -> "Creature":
        pass


class Flameling(Creature):
    def __init__(self, name: str, crea_type: str) -> None:
        super().__init__(name, crea_type)

    def attack(self) -> str:
        return f"{self._name} uses Ember!"


if __name__ == "__main__":
    print("Testing factory")
    pokemon: Flameling = Flameling("Flameling", "Fire")
    print(pokemon.describe())
