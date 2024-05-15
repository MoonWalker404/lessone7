# class SmartHouse():
#     def turn_on_light(self):
#         pass
#
#     def heat_food(self):
#         pass
#
#     def turn_on_music(self):
#         pass
# Это 4 принцип SOLID 👆
# Принцип разделения интерфейсов (ISP, Interface Segregation Principle)


class Light():
    def turn_on_light(self):
        print("Свет включен")


class Food():
    def heat_food(self):
        print("Еда начала разогреваться")


class Music():
    def turn_on_music(self):
        print("Включаю подборку ваших любимых песен")

