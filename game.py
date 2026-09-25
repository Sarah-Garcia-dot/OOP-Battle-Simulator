from goblin import Goblin
from hero import Hero
from boss import Boss


ARENA_NAME = "The Iron Claw"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("George")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblinTwo = Goblin("Fred")
    
    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health} health.")

    print("But no hero has answered the call... yet.")

    hero = Hero("Bob The 8th")
    print(f"{hero.name} enters the arena with {hero.health} health.")

    print(f"{hero.name} attackes {goblin.name}")

    goblin.take_damage(hero.attack())
    if goblin.is_alive:
        hero.take_damage(goblin.attack())



if __name__ == "__main__":
    main()
