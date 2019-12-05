import sqlite3
from Car import Car
import datetime

#region Information
# FROM выбирает таблицу
# SELECT вобор столба нужного мне
# WHERE условие для вывода SELECT

DataBaseName = "DataBase.sqllite"
TableName = "CarParkingInfo"
NameListVIP = "VIP_List"
NameParkList = "Places"
#endregion

#region CarParkingInfo
def AddToDataBase(Car, ParkTime):  # Добавляет регНомер и время в БД
    try:
        DBconnect = sqlite3.connect(DataBaseName)  # Подключение к базе (возмжоно нужно ватащить наружу)
        cursor = DBconnect.cursor()  # Место нахождение в таблице
        if(ParkTime == None):  # Если время парковки НОНЕ, то автоматом задаётся дата на данный момент
            ParkTime = str(datetime.datetime.now())
        cursor.execute("INSERT INTO {} (ID, RegNumber, ParkingTime, OutTime) VALUES ('{}', '{}','{}', '{}')".format(TableName, Car.ID, Car.RegNum, ParkTime, ' '))
        DBconnect.commit()  # Синхронизирует изменения с баззой
        DBconnect.close()  # Закрывает открытую БД
    except Exception as e:
        print("Ошибка при занесении данных в базу: " + e)
        DBconnect.close()
        return None

def GetTime(Car):  # Пока хз зачем это
    try:
        DBconnect = sqlite3.connect(DataBaseName)
        cursor = DBconnect.cursor()
        cursor.execute("SELECT ParkingTime FROM {} WHERE RegNumber='{}'".format(TableName, Car.RegNum))
        res = cursor.fetchall()
        DBconnect.close()
        return res
    except Exception as e:
        print("Ошибка при получении времени из базы: " + e)
        DBconnect.close()
        return None

def DelFromDataBase(Car):  # Удаляет каждое упоминание о номере
    try:
        DBconnect = sqlite3.connect(DataBaseName)
        cursor = DBconnect.cursor()
        cursor.execute("DELETE FROM {} WHERE RegNumber='{}'".format(TableName, Car.RegNum))
        DBconnect.commit()
        DBconnect.close()
    except Exception as e:
        print("Ошибка при удалении из базы: " + e)
        DBconnect.close()
        return None

def SetUnparking(UnParkingTime, Car):  # Задаёт время выеза, примерно так же как и время вьезда
    try:
        DBconnect = sqlite3.connect(DataBaseName)
        cursor = DBconnect.cursor()
        if(UnParkingTime == None):
            UnParkingTime = str(datetime.datetime.now())
        # cursor.execute("SELECT ParkingTime FROM {} WHERE RegNumber='{}'".format(TableName, RegNumber))
        # res = cursor.fetchall()
        # print(res[0][0]) # Получает строку времени парковки
        cursor.execute("UPDATE {} SET OutTime='{}' WHERE RegNumber='{}' AND OutTime=' '".format(TableName, UnParkingTime, Car.RegNum))
        DBconnect.commit()
        DBconnect.close()
    except Exception as e:
        print("Ошибка при задавании времени выезда в базу: " + e)
        DBconnect.close()
        return None

def CarOnParing(Car):  # Если есть пустой АутТайм, то автомобиль ещё на паркинге
    try:
        DBconnect = sqlite3.connect(DataBaseName)
        cursor = DBconnect.cursor()
        cursor.execute("SELECT OutTime FROM {} WHERE RegNumber='{}'".format(TableName, Car.RegNum))  # Получаем все АутТаймы, где данный номер
        res = cursor.fetchall()  # Если в АутТайме есть пустой эллемент, это значит что автомобиль находиться на парковке

        result = False
        if(len(res) == 0):  # Если нет эллементов АутТайм, то тачка точно не на парковке
            result = False
        else:  # Проверяет все элементы АутТайм и если какой то из них равен пробелу, тачка на парковке
            for i in res:
                if(i[0] == " "):
                    result = True

        DBconnect.close()
        return result
    except Exception as e:
        print("Ошибка при поиске наличии машины на парковке: " + e)
        DBconnect.close()
        return e
#endregion

#region VIP List
def VIP(Car):  # Если машина в вип листе
    try:
        DBconnect = sqlite3.connect(DataBaseName)
        cursor = DBconnect.cursor()
        cursor.execute("SELECT RegNum FROM {}".format(NameListVIP))
        res = cursor.fetchall()

        for i in range(0, len(res)):
            if(res[i][0] == Car.RegNum):
                DBconnect.close()
                return True

        DBconnect.close()
        return False
    except Exception as e:
        print("Ошибка при проверки ВИП автомобиля: " + e)
        DBconnect.close()
        return None

def AddToVIP(Car):  # Если машина в вип листе
    try:
        DBconnect = sqlite3.connect(DataBaseName)
        cursor = DBconnect.cursor()
        if(VIP(Car) == False):
            cursor.execute("INSERT INTO {} (RegNum) VALUES ('{}')".format(NameListVIP, Car.RegNum))

        DBconnect.commit()
        DBconnect.close()
        return False
    except Exception as e:
        print("Ошибка при добавлении в VIP список: " + e)
        DBconnect.close()
        return None
#endregion

#region Places
#region Get
def GetMaxPlaceDef(ParkName):
     try:
        DBconnect = sqlite3.connect(DataBaseName)
        cursor = DBconnect.cursor()
        cursor.execute("SELECT {} FROM {} WHERE ParkName='{}'".format("MaxPlaceDef", NameParkList, ParkName))
        res = cursor.fetchall()
        DBconnect.close()
        return int(res[0][0])
     except Exception as e:
        print("Ошибка при получении максимального места на стандартной парковке: " + e)
        DBconnect.close()
        return None


def GetMaxPlaceVIP(ParkName):
    try:
        DBconnect = sqlite3.connect(DataBaseName)
        cursor = DBconnect.cursor()
        cursor.execute("SELECT {} FROM {} WHERE ParkName='{}'".format("MaxPlaceVIP", NameParkList, ParkName))
        res = cursor.fetchall()
        DBconnect.close()
        return int(res[0][0])
    except Exception as e:
        print("Ошибка при получении максимального места на vip парковке: " + e)
        DBconnect.close()
        return None

def GetFreePlaceDef(ParkName):
    try:
        DBconnect = sqlite3.connect(DataBaseName)
        cursor = DBconnect.cursor()
        cursor.execute("SELECT {} FROM {} WHERE ParkName='{}'".format("FreePlaceDef", NameParkList, ParkName))
        res = cursor.fetchall()
        DBconnect.close()
        return int(res[0][0])
    except Exception as e:
        print("Ошибка при получении занятого места на обычной парковке: " + e)
        DBconnect.close()
        return None

def GetFreePlaceVIP(ParkName):
    try:
        DBconnect = sqlite3.connect(DataBaseName)
        cursor = DBconnect.cursor()
        cursor.execute("SELECT {} FROM {} WHERE ParkName='{}'".format("FreePlaceVIP", NameParkList, ParkName))
        res = cursor.fetchall()
        DBconnect.close()
        return int(res[0][0])
    except Exception as e:
        print("Ошибка при получении занятого места на vip парковке: " + e)
        DBconnect.close()
        return None
#endregion

#region Add
def AddMaxPlaceDef(add, ParkName):
    try:
        DBconnect = sqlite3.connect(DataBaseName)
        cursor = DBconnect.cursor()
        cursor.execute("SELECT {} FROM {} WHERE ParkName='{}'".format("MaxPlaceDef", NameParkList, ParkName))
        res = cursor.fetchall()
        add += int(res[0][0])
        cursor.execute("UPDATE {} SET MaxPlaceDef='{}' WHERE ParkName='{}'".format(NameParkList, str(add), ParkName))
        DBconnect.commit()
        DBconnect.close()
    except Exception as e:
        print("Ошибка при добавлении в MaxPlaceDef: " + e)
        DBconnect.close()
        return None


def AddMaxPlaceVIP(add, ParkName):
    try:
        DBconnect = sqlite3.connect(DataBaseName)
        cursor = DBconnect.cursor()
        cursor.execute("SELECT {} FROM {} WHERE ParkName='{}'".format("MaxPlaceVIP", NameParkList, ParkName))
        res = cursor.fetchall()
        add += int(res[0][0])
        cursor.execute("UPDATE {} SET MaxPlaceVIP='{}' WHERE ParkName='{}'".format(NameParkList, str(add), ParkName))
        DBconnect.commit()
        DBconnect.close()
    except Exception as e:
        print("Ошибка при добавлении в MaxPlaceVIP: " + e)
        DBconnect.close()
        return None


def AddFreePlaceDef(add, ParkName):
    try:
        DBconnect = sqlite3.connect(DataBaseName)
        cursor = DBconnect.cursor()
        cursor.execute("SELECT {} FROM {} WHERE ParkName='{}'".format("FreePlaceDef", NameParkList, ParkName))
        res = cursor.fetchall()
        add += int(res[0][0])
        cursor.execute("UPDATE {} SET FreePlaceDef='{}' WHERE ParkName='{}'".format(NameParkList, str(add), ParkName))
        DBconnect.commit()
        DBconnect.close()
    except Exception as e:
        print("Ошибка при добавлении в FreePlaceDef: " + e)
        DBconnect.close()
        return None


def AddFreePlaceVIP(add, ParkName):
    try:
        DBconnect = sqlite3.connect(DataBaseName)
        cursor = DBconnect.cursor()
        cursor.execute("SELECT {} FROM {} WHERE ParkName='{}'".format("FreePlaceVIP", NameParkList, ParkName))
        res = cursor.fetchall()
        add += int(res[0][0])
        cursor.execute("UPDATE {} SET FreePlaceVIP='{}' WHERE ParkName='{}'".format(NameParkList, str(add), ParkName))
        DBconnect.commit()
        DBconnect.close()
    except Exception as e:
        print("Ошибка при добавлении в FreePlaceVIP: " + e)
        DBconnect.close()
        return None
#endregion
#endregion

def Park(ParkName):  # Есть ли уже навзание данной стоянки
    try:
        DBconnect = sqlite3.connect(DataBaseName)
        cursor = DBconnect.cursor()
        cursor.execute("SELECT ParkName FROM {}".format(NameParkList))
        res = cursor.fetchall()

        for i in range(0, len(res)):
            if(res[i][0] == ParkName):
                DBconnect.close()
                return True

        DBconnect.close()
        return False
    except Exception as e:
        print("Ошибка при проверки стоянки: " + e)
        DBconnect.close()
        return None

def NewPark(ParkName, MaxPlaceDef, MaxPlaceVIP):
    try:
        DBconnect = sqlite3.connect(DataBaseName)  # Подключение к базе (возмжоно нужно ватащить наружу)
        cursor = DBconnect.cursor()  # Место нахождение в таблице
        cursor.execute("INSERT INTO {} (ParkName, MaxPlaceDef, FreePlaceDef, MaxPlaceVIP, FreePlaceVIP) VALUES ('{}', '{}','0', '{}', '0')".format(NameParkList, ParkName, str(MaxPlaceDef), str(MaxPlaceVIP)))
        DBconnect.commit()  # Синхронизирует изменения с баззой
        DBconnect.close()  # Закрывает открытую БД
    except Exception as e:
        print("Ошибка при занесении данных в базу: " + e)
        DBconnect.close()
        return None