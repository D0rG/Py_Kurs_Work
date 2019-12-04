import tkinter
from DataBase import *
from Stack import Stack

car = Car("Blue", "а586аа775")

if(car.ID == None):
    print("Автомобиль не действителен")
else:
    print("Автомобиль нормальный")

#print(car.RegNum)

#AddToDataBase(car, None)
#SetUnparking(None,  car)
#DelFromDataBase(car)
#SetUnparking(str(datetime.datetime.now()), car)

