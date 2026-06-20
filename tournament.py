from ex0 import FlameFactory, AquaFactory, Creature
from ex1 import heal_factory, trans_factory

if __name__ == "__main__":
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved")
    flame_factory: FlameFactory = FlameFactory()
    flameling: Creature = flame_factory.create_base()

    healing_factory: heal_factory = heal_factory()
    sproutling: Creature = healing_factory.create_base()
    print("\n* Battle *")
    print(flameling.describe())
    print(" vs.")
    print(sproutling.describe())

    print(" now fight!")
    print(flameling.attack())
    print(sproutling.attack())
    print(sproutling.heal("itself"))
