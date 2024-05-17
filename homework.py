from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом")


class Bow(Weapon):
    def attack(self):
        print("Боец делает выстрел из лука")


class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return f"{self.name} наносит {self.weapon.attack()}"
        else:
            return f"{self.name} - нету оружия"


class Monster:
    def __init__(self, name):
        self.name = name

    def defeate(self):
        return f"{self.name} побежден"

if __name__ == "__main__":
    fighter = Fighter("Боец")
    monster = Monster("Монстр")
    sword = Sword()
    bow = Bow()
    fighter.changeWeapon(sword)
    print("Боец выбирает меч")
    print(fighter.attack())
    print(monster.defeate())
    fighter.changeWeapon(bow)
    print("Боец выбирает лук")
    print(fighter.attack())
    print(monster.defeate())


