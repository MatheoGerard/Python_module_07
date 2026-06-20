from ex0 import Creature, CreatureFactory, FlameFactory, AquaFactory


def verif_factory(factory: CreatureFactory):
    try:
        base: Creature = factory.create_base()
        evolved: Creature = factory.create_evolved()
        base.describe()
        evolved.describe()
        base.attack()
        evolved.attack()
    except Exception as e:
        raise e


def battle(flame_factory: FlameFactory, aqua_factory: AquaFactory):
    try:
        verif_factory(flame_factory)
        verif_factory(aqua_factory)
    except Exception as e:
        print(e)
    base_flame_creature: Creature = flame_factory.create_base()
    base_water_creature: Creature = aqua_factory.create_base()
    print(base_flame_creature.describe())
    print(" vs.")
    print(base_water_creature.describe())
    print(" fight!")
    print(base_flame_creature.attack())
    print(base_water_creature.attack())


if __name__ == "__main__":
    print("Testing factory")
    factory_fire: FlameFactory = FlameFactory()

    fire_creature_base: Creature = factory_fire.create_base()
    fire_creature_evolved: Creature = factory_fire.create_evolved()
    print(fire_creature_base.describe())
    print(fire_creature_base.attack())
    print(fire_creature_evolved.describe())
    print(fire_creature_evolved.attack())

    print("\nTesting factory")
    factory_water: AquaFactory = AquaFactory()

    water_creature_base: Creature = factory_water.create_base()
    water_creature_evolved: Creature = factory_water.create_evolved()
    print(water_creature_base.describe())
    print(water_creature_base.attack())
    print(water_creature_evolved.describe())
    print(water_creature_evolved.attack())

    print("\nTesting battle")
    battle(factory_fire, factory_water)
