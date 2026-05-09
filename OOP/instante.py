class shop:
    def __init__(self, buyer):
        self.buyer=buyer
        self.card=[]
    def add_to_card(self,item):
        self.card.append(item)

myNeed= shop("Ali")  
myNeed.add_to_card("Pen")
myNeed.add_to_card("pencil")

y= shop("Nur")
y.add_to_card("books")
y.add_to_card("calculator")


print(myNeed.buyer,myNeed.card)
print(y.buyer,y.card)