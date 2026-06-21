from ex1 import heal_factory
from ex1 import trans_factory
from ex0 import Creature
from ex1.other_factory import HealCapability, TransformCapability

if __name__ == "__main__":
    print("Testing Creature with healing capability")

    print(" base:")
    crea_heal_factory: heal_factory = heal_factory()
    base_grass: Creature = crea_heal_factory.create_base()
    if isinstance(base_grass, Creature) and isinstance(
        base_grass, HealCapability
    ):
        print(base_grass.describe())
        print(base_grass.attack())
        print(base_grass.heal("itself"))

    print(" evolved:")
    evolved_grass: Creature = crea_heal_factory.create_evolved()
    if isinstance(evolved_grass, Creature) and isinstance(
        evolved_grass, HealCapability
    ):
        print(evolved_grass.describe())
        print(evolved_grass.attack())
        print(evolved_grass.heal("itself"))

    print("\nTesting Creature with transform capability")
    print(" base:")
    crea_trans_factory: trans_factory = trans_factory()
    base_normal: Creature = crea_trans_factory.create_base()
    if isinstance(base_normal, Creature) and isinstance(
        base_normal, TransformCapability
    ):
        print(base_normal.describe())
        print(base_normal.attack())
        print(base_normal.transform())
        print(base_normal.attack())
        print(base_normal.revert())

    print(" evolved:")
    evolved_dragon: Creature = crea_trans_factory.create_evolved()
    if isinstance(evolved_dragon, Creature) and isinstance(
        evolved_dragon, TransformCapability
    ):
        print(evolved_dragon.describe())
        print(evolved_dragon.attack())
        print(evolved_dragon.transform())
        print(evolved_dragon.attack())
        print(evolved_dragon.revert())
