class TempState:
    def __init__(self,temp):
        self.temp=temp

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self,t):
        if(t<10):
            return(f"Give more than 10 you temperature : {t}")
        elif(t > 40):
            return(f"Give under 40, you give : {t}")
        else:
            self._temp=t


myRoom= TempState(30)

print(f"Room temperature is : {myRoom.temp}")

myRoom.temp=35
print(f"Room temperature is : {myRoom.temp}")


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        newName = f"{self.name} & {other.name}"
        newPrice = self.price + other.price
        return Item(newName, newPrice)

    def __str__(self):
        return f"total for {self.name} = {self.price}"


class Dress(Item):
    def __init__(self, name, price):
        super().__init__(name, price)


class Food(Item):
    def __init__(self, name, price):
        super().__init__(name, price)


product1 = Dress("shirt", 50)
product2 = Dress("pant", 70)
food1 = Food("tost", 3)
food2 = Food("Tea", 4)

print(food1 + product1 + food2 + product2)
