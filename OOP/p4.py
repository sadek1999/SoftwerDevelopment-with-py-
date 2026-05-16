class SimCard:
    def get_signal(self):
        return f"Get Connection of 5G Network"
    
class Phone:
   def __init__(self):
       self.sim=SimCard()

   def makeCall(self):
       print(f"Making call for : {self.sim.get_signal()}")
       

myPhone= Phone()

myPhone.makeCall()
