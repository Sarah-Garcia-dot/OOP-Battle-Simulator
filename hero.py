import random
class Hero:
    
     def __init__(self, name):
            self.name = name
            self.health = 127
            self.attack_power = 23
    
     def attack(self):
            return random.randint(1, self.attack_power)

     def battle_cry(self):
                 print("ARGGGGG")
    
     def take_damage(self, damage):
            self.health = max(0, self.health - damage)
            print(f"{self.name} takes {damage} damage. Health: {self.health}")
            self.battle_cry()
    
     def is_alive(self):
            return self.health > 0

     

