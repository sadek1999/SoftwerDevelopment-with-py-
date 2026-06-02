from datetime import datetime

class RideShearing:
    def __init__(self,company_name):
        self.company_name=company_name
        self.riders=[]
        self.drivers=[]
        self.rides=[]
    
    def add_rider(self,rider):
        self.riders.append(rider)

    def add_driver(self,driver):
        self.drivers.append(driver)  

    def __str__(self):
        return f"Company name : {self.company_name} with riders : {len(self.riders) } drivers : {len(self.drivers)}"      

class Ride:
    def __init__(self,start_location,end_location):
        self.start_location=start_location
        self.end_location= end_location
        self.driver=None
        self.ride=None
        self.start_time= None
        self.end_time= None
        self. estimated_fare=None
        
    def set_Driver(self,driver):
        self.driver=driver

    def start_ride(self):
        self.start_time= datetime.now()

    def end_ride(self):
        self.end_time=datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare 

    def __repr__(self):
        return f"From: {self.start_location} to {self.end_location} "  


class Rider_Request:
    def __init__(self,rider,end_location):
        self.rider=rider
        self.end_location=end_location

class Ride_Matching:
    def __init__(self,driver):
        self.available_drivers= driver


    def find_drivers(self,ride_request):
        if len(self.available_drivers)>0:
            print("Looking fo drivers......")
            driver = self.available_drivers[0]
            ride= Ride(ride_request.rider.current_location,ride_request.end_location)
            driver.accept_request(ride)
            return ride


             
                   