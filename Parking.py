from Stack import Stack
from DataBase import*
from Car import Car
from Tree import *

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
            return False

    def CanAddToVIP(self):
        if(GetMaxPlaceVIP(self.Name) - GetFreePlaceVIP(self.Name) > 0):
            return True
        else:
            return False

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
            AddFreePlaceDef(1, self.Name)
        else:
            self.AddToVIP(car)
            AddFreePlaceVIP(1, self.Name)

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

    def CarOnPark(self, car):
        BufStack = Stack()
        BufMirrorStack = Stack()

        for i in range(self.parkVIP.size()):
            BufStack.push(self.parkVIP.pop())
        for i in range(BufStack.size()):
            car = BufStack.pop()
            BufMirrorStack.push(car)
            self.parkVIP.push(car)

        for i in range(BufMirrorStack.size()):
            if((BufMirrorStack.pop()).RegNum == car.RegNum):
                return True

        for i in range(self.parkDef.size()):
            BufStack.push(self.parkDef.pop())
        for i in range(BufStack.size()):
            car = BufStack.pop()
            BufMirrorStack.push(car)
            self.parkDef.push(car)

        for i in range(BufMirrorStack.size()):
            if ((BufMirrorStack.pop()).RegNum == car.RegNum):
                return True

        return False

    def DelCar(self, car):
        BufStack = Stack()
        CarHere = False
        intMoved = None
        for i in range(self.parkDef.size()):
            newCar = self.parkDef.pop()
            if(newCar.RegNum == car.RegNum):  # Удаление машины
                CarHere = True
                intMoved = newCar.Moved
                SetUnparking(None, car)
                AddFreePlaceDef(-1, self.Name)
            else:
                newCar.Moved += 1
                BufStack.push(newCar)
        for i in range(BufStack.size()):
            self.parkDef.push(BufStack.pop())

        if(CarHere):
            return intMoved

        for i in range(self.parkVIP.size()):
            newCar = self.parkVIP.pop()
            if(newCar.RegNum == car.RegNum):  # Удаление машины
                CarHere = True
                intMoved = newCar.Moved
                SetUnparking(None, car)
                AddFreePlaceVIP(-1, self.Name)
            else:
                BufStack.push(newCar)
        for i in range(BufStack.size()):
            self.parkVIP.push(BufStack.pop())

        if (CarHere):
            return intMoved

    def ReturnCarListDef(self):  # Возвращает представление парковки в виде массива
        List = []
        parkBuf = Stack()

        for i in range(self.parkDef.size()):  # Перегоняет машины в стек, что бы узнать какие машины на парковке
            carBuf = self.parkDef.pop()
            List.append(carBuf)
            parkBuf.push(carBuf)
        for i in range(parkBuf.size()):  # Отрпавляет обратно в стек
            self.parkDef.push(parkBuf.pop())
        return List

    def ReturnCarListVIP(self):  # Возвращает представление парковки в виде массива
        List = []
        parkBuf = Stack()

        for i in range(self.parkVIP.size()):  # Перегоняет машины в стек, что бы узнать какие машины на парковке
            carBuf = self.parkVIP.pop()
            List.append(carBuf)
            parkBuf.push(carBuf)
        for i in range(parkBuf.size()):  # Отрпавляет обратно в стек
            self.parkVIP.push(parkBuf.pop())
        return List


    def SortTree(self):  # Сортирует и VIP и обычную парковку
        temp = []  # Сюда попадает отсортированные деревом ID автомобилей
        ListDef = self.ReturnCarListDef()
        TreeDef = None
        for car in ListDef:  # Перегоняет парковеу в дерево
            TreeDef = insert(TreeDef, car.ID)
        postorder(TreeDef, temp)  # Получает от дерева отсортированный массив
        self.parkDef = Stack()  # Обнуляет стек

        for carID in temp: # Отсортированный массив айдишников из дерева
            for car in range(len(ListDef)):  # Массив автомобилей созданый из стека
                if(carID == ListDef[car].ID):  # Если встречаеться айдишник, то машина попадает на парковку и удаляеться из ListDef для того что бы повторне не пробегать. Последним эллементом добавленным в стак будет корень дерева
                    self.parkDef.push(ListDef[car])
                    ListDef.pop(car)
                    break

        temp = []
        ListVIP = self.ReturnCarListVIP()
        TreeVIP = None
        for car in ListDef:
            TreeVIP = insert(TreeVIP, car.ID)
        postorder(TreeVIP, temp)
        self.parkVIP = Stack()

        for carID in temp:
            for car in range(len(ListVIP)):
                if (carID == ListVIP[car].ID):
                    self.parkVIP.push(ListVIP[car])
                    ListVIP.pop(car)
                    break
