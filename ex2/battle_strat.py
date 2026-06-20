from abc import ABC, abstractmethod
from ex0 import Creature
from ex1.other_factory import TransformCapability, HealCapability


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, crea: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, crea: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, crea: Creature) -> bool:
        if isinstance(crea, Creature):
            return True
        else:
            return False

    def act(self, crea: Creature) -> None:
        if isinstance(crea, Creature):
            print(crea.attack())
        else:
            raise Exception(
                f"Battle error, aborting tournament: Invalid Creature '{crea._name}' for this normal strategy"
            )


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, crea: Creature) -> bool:
        if isinstance(crea, Creature) and isinstance(crea, TransformCapability):
            return True
        else:
            return False

    def act(self, crea: Creature) -> None:
        if isinstance(crea, TransformCapability):
            print(crea.transform())
            print(crea.attack())
            print(crea.revert())
        else:
            raise Exception(
                f"Battle error, aborting tournament: Invalid Creature '{crea._name}' for this aggressive strategy"
            )


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, crea: Creature) -> bool:
        if isinstance(crea, Creature) and isinstance(crea, HealCapability):
            return True
        else:
            return False

    def act(self, crea: Creature) -> None:
        if isinstance(crea, HealCapability):
            print(crea.attack())
            print(crea.heal("itself"))
        else:
            raise Exception(
                f"Battle error, aborting tournament: Invalid Creature '{crea._name}' for this defensive strategy"
            )
