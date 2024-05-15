# class Bird():
#     def __init__(self, name):
#         self.name = name
#
#     def fly(self):
#         print(f"Птица {self.name} летает")
#
# class Pinguin(Bird):
#     pass
#
# pinguin = Pinguin("Сара")
# pinguin.fly()
# Пингвины не летают и это 3-й принцип SOLID 👆
# Принцип подстановки Барбары Лисков (LSP, Liskov substitution Principle)
# Вот как делают по  факту👇

class Bird():
    def fly(self):
        print(f"Эта птица летает")

class Duck(Bird):
    def fly(self):
        print("Эта утка летает быстро")

def flyinsky(animal):
    animal.fly()

bird = Bird()
duck = Duck()

flyinsky(bird)
flyinsky(duck)