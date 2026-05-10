class Product:
    def __init__(self,name,price):
        self.name= name
        self.price=price
        
    

class Shop:
    def __init__(self,name):
        self. name= name
        self.products=[]

    def add_product(self,name,price):
        self.name=name
        self.price=price
        new_product=Product(name,price)
        self.products.append(new_product)

    def by_product(self,name,price):
        for item in self.products:
            
            print(item.name,item.price)
            # print("successful")



my_shop=Shop("Ali's shop")
my_shop.add_product("pen",20)
my_shop.add_product("pencil",20)

my_shop.by_product("attur",40)