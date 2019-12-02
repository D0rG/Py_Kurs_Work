import sqlite3
# FROM выбирает таблицу
# SELECT вобор столба нужного мне
# WHERE условие для вывода SELECT

def AddToDataBase(RegNum, ParkTime): # Добавляет регНомер и время в БД
    DBconnect = sqlite3.connect("DataBase.sqllite")
    cursor = DBconnect.cursor()

    cursor.execute("INSERT INTO CarParkingInfo (RegNumber, ParkingTime) VALUES ('{}','{}')".format(RegNum, ParkTime))
    DBconnect.commit()
    res = cursor.fetchall()

    DBconnect.close()
    return res

def GetTime(RegNum):
    DBconnect = sqlite3.connect("DataBase.sqllite")
    cursor = DBconnect.cursor()

    cursor.execute("SELECT ParkingTime FROM CarParkingInfo WHERE RegNumber='{}'".format(RegNum))
    res = cursor.fetchall()

    DBconnect.close()
    return res