class TempState:
    def __init__(self,temp):
        self.temp=temp

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self,t):
        if(t<10):
            return(f"Give more than 10 you temperature : {t}")
        elif(t > 40):
            return(f"Give under 40, you give : {t}") 
        else:
            self._temp=t   


myRoom= TempState(30)

print(f"Room temperature is : {myRoom.temp}")

myRoom.temp=35
print(f"Room temperature is : {myRoom.temp}")
