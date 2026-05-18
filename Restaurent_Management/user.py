class User:
    def __init__(self, name, email, address, phone):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone


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
        self.menu = FoodItem()

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


f1=FoodItem("pizza",30,20)
m1=Menu()
m1.add_item(f1);  
m1.view_items()           
