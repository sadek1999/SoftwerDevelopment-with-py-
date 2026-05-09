class shopping:
    def __init__(self,name):
        self.name=name
        self.card=[]

    def add_to_cad(self,item,quantity,price):
        product={"item":item,"price":price,"quantity":quantity}
        self.card.append(product)  

    def checkOut(self,amount):
        total=0
        
        for product in self.card:
            a = product["price"]*product["quantity"]
            total += a
        print(total)
        if total > amount:
                bill = total-amount
                print(f"give more {bill}")
        elif amount > total:
                bill = amount - total
                print(f"this is you products and hear you change is {bill}")

        else:
                print(f"Your total bill = {total} all paid \nCome again \nthank you sir \nGood buy \nHave good day ")

                
               


my_shopping = shopping('Ali')
my_shopping.add_to_cad("Rice",50,55)
my_shopping.add_to_cad("oil",5,90)
my_shopping.add_to_cad("Shope",4,55)
my_shopping.checkOut(3420)


# print(my_shopping.card)