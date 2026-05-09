class calculator:
    brand = "casio "
    color = "black"

    def add(self, n1, n2):
        return n1 + n2

    def deduct(self, n1, n2):
        return n1 - n2

    def multiply(self, a, b):
        return a * b

    def divided(self, a, b):
        return a / b


class phone:
    madeIn = "china"

    def __init__(self, owner, brand, price, color):
        self.owner = owner
        self.brand = brand
        self.price = price
        self.color = color


phone1 = phone("me", "samsung", 30000, "black")
phone2 = phone("you", "Oppo", 44900, "white")
phone3 = phone("His", "Nokia", 3500, "red")
print(phone2.brand,phone2.owner,phone2.price,phone2.color)
print(phone1.brand,phone1.owner,phone1.price,phone1.color)
my_calculator = calculator()

print("multiply", my_calculator.deduct(33, 4))
