class User:
    def __init__(self, name, email, address, phone):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone

class Customer(User):
    def __init__(self, name, email, address, phone):
        super().__init__(name, email, address, phone)
        self.card=None

    def view_menu(self,restaurant):
        restaurant.menu.view_items()


    def add_item(self,restaurant,item_name):
        item = restaurant.menu.find_item(item_name)
        if item:
            pass
        else:
            print("Item not Found")

    def view_card(self):
        print("********* View Card *******")
        print("name\tprice\tquantity")


class Order:
    def __init__(self):
        self.items={}

    def add_item(self,item,quantity):
            if item in self.items:
                self.items[item] += item.quantity
            else:
                self.items[item]=item.quantity

    def remove_item(self,item):
         if item in self.items:
            del self.items[item] 

    def total_price(self):
        return sum(item.price * quantity for item,quantity in self.items.items())

    def clear(self):
        self.items={}

class Employee(User):
    def __init__(self, name, email, address, phone, age, designation, salary):
        super().__init__(name, email, address, phone)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, email, address, phone):
        super().__init__(name, email, address, phone) 
        

    def add_employee(self,restaurant,employee):
        restaurant.add_employee(employee)
       
    def view_employee(self,restaurant):
        restaurant.view_employee()   

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_item(item) 

    def remove_item(self,restaurant ,item):
        restaurant.menu.remove_item(item)       

class RestaurantManagement: 
    def __init__(self,name):
        self.name= name
        self.employees=[]
        self.menu = Menu()

    def add_employee(self,employee):
        self.employees.append(employee)

    def view_employee(self):
        print("---------Employees list ------")    
        for emp in  self.employees:
            print(emp.name,emp.email, emp.designation ,emp.salary)
                         
class Menu:
    def __init__(self):
        self.items=[]

    def add_item(self,item):
        self.items.append(item)

    def find_item(self,item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return(item) 
           
        return None     
     
    def remove_item(self,item_name):
           item = self.find_item(item_name)
           if item:
               self.items.remove(item)
           else:
              print(f"Item not available ") 

    def view_items(self):
        print("****** Menu **********")
        print("name \tprice\tquantity")
        for item in self.items:
            print(f"{item.name}\t{ item.price}\t {item.quantity}")


class FoodItem:
    def __init__(self,name,price,quantity):
        self.name= name 
        self.price= price
        self.quantity= quantity

admin1= Admin("A","a@gmail.com","Dhaka",3928456)
r1=RestaurantManagement("R1")

f1=FoodItem("pizza",30,20)
f2=FoodItem("Burger",20,40)
f3=FoodItem("Cock",20,60)

admin1.add_new_item(r1,f1)
admin1.add_new_item(r1,f2)
admin1.add_new_item(r1,f3)

c1=Customer("B","b@gmail.com","Dhaka",3837)
c1.view_menu(r1)           
