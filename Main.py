import tkinter
from DataBase import *
from Stack import Stack
from Car import Car

car = Car("Blue", "в586ме777")
print(car.RegNum)

AddToDataBase("в666вв666", "15:20")
print(GetTime("в555вв555"))

# Car.SetID(car)
# Car.SeyWTF(car)
# print(car.ID)
