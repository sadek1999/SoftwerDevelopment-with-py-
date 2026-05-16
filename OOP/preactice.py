class Person:
    def __init__(self, name, age, hight, weight):
        self.name = name
        self.age = age
        self.hight = hight
        self.weight = weight

    def __lt__(self, other):
        return self.age < other.age


class Cricketer(Person):
    def __init__(self, name, age, hight, weight):
        super().__init__(name, age, hight, weight)


sakib = Cricketer("Sakib", 38, 68, 91)
musfiq = Cricketer("Rahim", 36, 68, 88)
kamal = Cricketer("Kamal", 39, 68, 94)
jack = Cricketer("Jack", 38, 68, 91)
kalam = Cricketer("Kalam", 37, 68, 95)

players = [sakib, musfiq, kamal, jack, kalam]
oldest_player = max(players)

print(oldest_player.name)
