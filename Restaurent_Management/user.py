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
        self.employees=[]

    def add_employee(self,name, email, address, phone, age, designation, salary):
        employee= Employee(name,email,address,phone,age,designation,salary)
        self.employees.append(employee)
        print(f"successfully create employee: {name}")         


