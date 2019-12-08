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
                self.parkDef = Stack()
                self.parkVIP = Stack()
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

    def Dell(self):  # Удаляет из БД
        DelPark(self.Name)

    def ParkCar(self, car, place = "DEF"):
        AddToDataBase(car, None)
        if(place == "DEF"):
            self.AddToDef(car)
        else:
            self.AddToVIP(car)

    def PrintStackDef(self):
        BufStack = Stack()
        BufMirrorStack = Stack()

        for i in range(self.parkDef.size()):
            BufStack.push(self.parkDef.pop())
        for i in range(BufStack.size()):
            car = BufStack.pop()
            BufMirrorStack.push(car)
            self.parkDef.push(car)


        list = []
        for i in range(BufMirrorStack.size()):
            list.append((BufMirrorStack.pop()).RegNum)
        return list

    def PrintStackVIP(self):
        BufStack = Stack()
        BufMirrorStack = Stack()

        for i in range(self.parkVIP.size()):
            BufStack.push(self.parkVIP.pop())
        for i in range(BufStack.size()):
            car = BufStack.pop()
            BufMirrorStack.push(car)
            self.parkVIP.push(car)

        list = []
        for i in range(BufMirrorStack.size()):
            list.append((BufMirrorStack.pop()).RegNum)
        return list