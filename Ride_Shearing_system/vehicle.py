
from abc import ABC

class Vehicle(ABC):
    speed={
        'car':50,
        'bike':40,
        'cng': 20
    }
    def __init__(self,vehicle_type,number_plate,rate):
        self.vehicle_type= vehicle_type
        self.number_plate= number_plate
        self.rate= rate

class Car(Vehicle):
    def __init__(self, vehicle_type, number_plate, rate):
        super().__init__(vehicle_type, number_plate, rate)
class Bike(Vehicle):
    def __init__(self, vehicle_type, number_plate, rate):
        super().__init__(vehicle_type, number_plate, rate)

        