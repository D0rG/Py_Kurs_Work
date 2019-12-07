from Stack import Stack
from DataBase import*
from Car import Car

class Parking:
    Name = None
    MaxPlaceDef = 0
    MaxPlaceVIP = 0
    parkDef = Stack()
    parkVIP = Stack()

    def __init__(self, Name, PlaceDef, PlaceVip):
        if(isinstance(Name, str) and isinstance(PlaceDef, int) and isinstance(PlaceVip, int)):
            try:
                self.Name = Name
                self.MaxPlaceDef = PlaceDef
                self.MaxPlaceVIP = PlaceVip
                if(not Park(self.Name)):
                    NewPark(self.Name, self.MaxPlaceDef, self.MaxPlaceVIP)
                else:
                    Name = None
            except Exception as e:
                self.Name = None
                print(e)
        else:
            Name = None

    def CanAddToDef(self):
        if(GetMaxPlaceDef(self.Name) - GetFreePlaceDef(self.Name) > 0):
            return True
        else:
            return True

    def CanAddToVIP(self):
        if(GetMaxPlaceVIP(self.Name) - GetFreePlaceVIP(self.Name) > 0):
            return True
        else:
            return True

    def AddToDef(self, car):
        if(self.CanAddToDef() and isinstance(car, Car)):
            self.parkDef.push(car)

    def AddToVIP(self, car):
        if(self.CanAddToVIP() and isinstance(car, Car)):
            self.parkVIP.push(car)

    def BusyPlaceDef(self):  # Возвращет True если на парковке 0 автомобилей и False, если на парковке есть хотя бы один автомобиль
        if(GetFreePlaceDef(self.Name) == 0):
            return True
        else:
            return False

    def BusyPlaceVIP(self):  # Возвращет True если на парковке 0 автомобилей
        if(GetFreePlaceVIP(self.Name) == 0):
            return True
        else:
            return False

    def Dell(self):
        DelPark(self.Name)