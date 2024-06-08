from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Воин наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Воин наносит удар из лука."

class Axe(Weapon):
    def attack(self):
        return "Воин наносит удар топором."

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return self.weapon.attack()
        else:
            return "Воин безоружен."

class Monster:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def defend(self):
        return f"{self.name} защищается!"

    def take_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} ранен, осталось здоровья: {self.health}"
        else:
            return self.defeat()

    def defeat(self):
        return f"{self.name} побежден!"

def battle(fighter, monster, damage):
    print(fighter.attack())
    print(monster.take_damage(damage))

fighter = Fighter("Воин 1")
monster = Monster("Монстр")

print("Воин выбирает лук.")
bow = Bow()
fighter.changeWeapon(bow)
print(monster.defend())
battle(fighter, monster, 20)

print("\nВоин выбирает топор.")
axe = Axe()
fighter.changeWeapon(axe)
battle(fighter, monster, 40)


print("\nВоин выбирает меч.")
sword = Sword()
fighter.changeWeapon(sword)
battle(fighter, monster, 40)