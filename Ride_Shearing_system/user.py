
from abc import ABC , abstractmethod

class User(ABC):
    def __init__(self,name,email,nid):
        self.name=name
        self.email=email
        self.nid= nid
        self.wallet=0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError    


class Rider(User):
    def __init__(self, name, email, nid,current_location,initial_amount):
        super().__init__(name, email, nid)
        self.current_location=current_location
        self.wallet= initial_amount
        self.current_ride=None

    def display_profile(self):
        print(f"Rider : {self.name} his email : {self.email}")

    def load_cash(self,amount):
        if amount > 0 :
            self.wallet += amount
        else:
            print("you amount is less then 0.00 tk")   

    def update_location(self,current_location):
        self.current_location=current_location 

    def ride_request(self,ride_shearing,destination ):
        pass
    def current_ride (self):
        print(f" now I am in {self.current_ride}")                


class Driver(User):
    def __init__(self, name, email, nid,current_location):
        super().__init__(name, email, nid)
        self.current_location= current_location
        self.wallet=0

    def display_profile(self):
       print(f"Rider : {self.name} ")

    def ride_request(self,destination):
        pass 

    def accept_ride(self,ride):
        ride.set_driver(self)
     