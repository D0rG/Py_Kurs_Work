import sqlite3
from Car import Car
import datetime
# FROM выбирает таблицу
# SELECT вобор столба нужного мне
# WHERE условие для вывода SELECT

DataBaseName = "DataBase.sqllite"
TableName = "CarParkingInfo"

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
        return None