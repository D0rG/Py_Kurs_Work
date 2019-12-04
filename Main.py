import tkinter
from DataBase import *
from Stack import Stack

car = Car("Blue", "к777кс777")

if(car.ID == None):
    print("Автомобиль не действителен")
else:
    if (CarOnParing(car) == True):
        print("Автомобиль на стоянке")
    elif (CarOnParing(car) == False):
        print("Автомобиль не на стоянке")

    if(VIP(car) == True):
        print("Автомобиль VIP")
    elif(VIP(car) == False):
        print("Автомобиль не в VIP")


AddToVIP(car)
#print(car.RegNum)

#AddToDataBase(car, None)
#SetUnparking(None,  car)
#DelFromDataBase(car)
#SetUnparking(str(datetime.datetime.now()), car)

