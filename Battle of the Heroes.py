class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20
    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")
    def is_alive(self):
        return self.health > 0
class Game:
    def __init__(self,):
        self.player = Hero("Игрок")
        self.computer = Hero("Компьютер")
    def start(self):
        print("Начинается битва героев")

        while True:
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.player.name} побеждает!")
                break

            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.computer.name} побеждает!")
                break


if __name__ == "__main__":
    game = Game()
    game.start()