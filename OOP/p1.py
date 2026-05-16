class CoffeeMachine:
    def brew(self):
        print("Brew make a coffee ..... ")


class PremiumCoffeeMachine(CoffeeMachine):
     def brew(self):
         print("Brew make a rich coffee .....")    


coffee_shop1 = PremiumCoffeeMachine();
coffee_shop2= CoffeeMachine()

coffee_shop1.brew()
coffee_shop2.brew()