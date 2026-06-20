from ex0 import FlameFactory, AquaFactory, Creature
from ex1 import heal_factory, trans_factory
import ex2

if __name__ == "__main__":
    print("Tournament 0 (basic)")
    normal: ex2.n_s = ex2.n_s()
    aggressive: ex2.a_s = ex2.a_s()
    defensive: ex2.d_s = ex2.d_s()

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
    normal.act(flameling)
    defensive.act(sproutling)

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved")
    print("\n* Battle *")
    print(flameling.describe())
    print(" vs.")
    print(sproutling.describe())

    print(" now fight!")
    try:
        aggressive.act(flameling)
    except Exception as e:
        print(e)
