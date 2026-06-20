from abc import ABC, abstractmethod
from ex0 import Creature, CreatureFactory


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self._is_transform: bool = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if not self._is_transform:
            return f"{self._name} attacks normally."
        else:
            return f"{self._name} performs a boosted strike!"

    def transform(self) -> str:
        if not self._is_transform:
            self._is_transform = True
            return f"{self._name} shifts into a sharper form!"
        else:
            return f"{self._name} is already in a sharper form..."

    def revert(self) -> str:
        if self._is_transform:
            self._is_transform = False
            return f"{self._name} returns to normal."
        else:
            return f"{self._name} is already normal..."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if not self._is_transform:
            return f"{self._name} attacks normally."
        else:
            return f"{self._name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        if not self._is_transform:
            self._is_transform = True
            return f"{self._name} morphs into a dragonic battle form!"
        else:
            return f"{self._name} is already in a dragonic form..."

    def revert(self) -> str:
        if self._is_transform:
            self._is_transform = False
            return f"{self._name} stabilizes its form."
        else:
            return f"{self._name} is already normal..."


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self._name} uses Vine Whip!"

    def heal(self, target: str) -> str:
        return f"{self._name} heals {target} for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"

    def heal(self, target: str) -> str:
        return f"{self._name} heals {target} and others for a large amount"


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> "Sproutling":
        return Sproutling()

    def create_evolved(self) -> "Bloomelle":
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> "Shiftling":
        return Shiftling()

    def create_evolved(self) -> "Morphagon":
        return Morphagon()
