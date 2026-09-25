import random
from enemy import Enemy


class Boss(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, health = 250, attackPower = 30)
        self.gold=0

    def attack(self):
        damage = super().attack()
        bonus_damage = 5
        print(f"{self.name} released a HUGE fire ball!")
        return damage + bonus_damage