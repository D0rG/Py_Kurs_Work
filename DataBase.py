import sqlite3
from Car import Car
import datetime

# FROM выбирает таблицу
# SELECT вобор столба нужного мне
# WHERE условие для вывода SELECT

DataBaseName = "DataBase.sqllite"
TableName = "CarParkingInfo"
NameListVIP = "VIP_List"

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
        cursor.execute("SELECT RegNum FROM {}".format(NameListVIP))
        res = cursor.fetchall()

        InList = False
        for i in range(0, len(res)):
            if(res[i][0] == Car.RegNum):
                InList = True
        if(InList == False):
            cursor.execute("INSERT INTO {} (RegNum) VALUES ('{}')".format(NameListVIP, Car.RegNum))


        DBconnect.commit()
        DBconnect.close()
        return False
    except Exception as e:
        print("Ошибка при добавлении в VIP список: " + e)
        DBconnect.close()
        return None