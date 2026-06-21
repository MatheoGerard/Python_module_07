from ex0 import FlameFactory, AquaFactory, Creature
from ex1 import heal_factory, trans_factory
from ex1.other_factory import Shiftling
import ex2

if __name__ == "__main__":
    print("Tournament 0 (basic)")
    normal: ex2.n_s = ex2.n_s()
    aggressive: ex2.a_s = ex2.a_s()
    defensive: ex2.d_s = ex2.d_s()

    flame_factory: FlameFactory = FlameFactory()
    healing_factory: heal_factory = heal_factory()
    aqua_fatcory: AquaFactory = AquaFactory()
    transforming_factory: trans_factory = trans_factory()

    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved")

    flameling: Creature = flame_factory.create_base()
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

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    print("3 opponents involved")
    print("\n* Battle *")
    aquabub: Creature = aqua_fatcory.create_base()
    aquabub.describe()
    print(" vs.")
    sproutling.describe()

    print(" now fight!")
    normal.act(aquabub)
    defensive.act(sproutling)

    print("\n* Battle *")
    shiftling: Creature = transforming_factory.create_base()
    aquabub: Creature = aqua_fatcory.create_base()
    aquabub.describe()
    print(" vs.")
    shiftling.describe()

    print(" now fight!")
    normal.act(aquabub)
    aggressive.act(shiftling)

    print("\n* Battle *")
    sproutling.describe()
    print(" vs.")
    shiftling.describe()

    print(" now fight!")
    defensive.act(sproutling)
    aggressive.act(shiftling)
