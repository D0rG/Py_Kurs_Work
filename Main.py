import tkinter
from DataBase import *
from Stack import Stack

car = Car("Blue", "к777кс777")
SizeParkDef = 0
SizeParkVIP = 0
parkDef = Stack()
parkVIP = Stack()

print(str(GetMaxPlaceDef() + 2))

# parkDef.push(car)
# parkDef.push(car)
# parkDef.push(car)
# print(parkDef.pop().RegNum)
# print(parkDef.size())
#
# if(car.ID == None):
#     print("Автомобиль не действителен")
# else:
#     if (CarOnParing(car) == True):
#         print("Автомобиль на стоянке")
#     elif (CarOnParing(car) == False):
#         print("Автомобиль не на стоянке")
#
#     if(VIP(car) == True):
#         print("Автомобиль VIP")
#     elif(VIP(car) == False):
#         print("Автомобиль не в VIP")


AddToVIP(car)
#print(car.RegNum)
#AddToDataBase(car, None)
#SetUnparking(None,  car)
#DelFromDataBase(car)
#SetUnparking(str(datetime.datetime.now()), car)
# AddMaxPlaceDef(-10)
# AddMaxPlaceVIP(-122)
# AddFreePlaceDef(-23)
# AddFreePlaceVIP(-34)

