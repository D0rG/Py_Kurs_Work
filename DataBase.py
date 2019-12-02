import sqlite3
# FROM выбирает таблицу
# SELECT вобор столба нужного мне
# WHERE условие для вывода SELECT

DataBaseName = "DataBase.sqllite"

def AddToDataBase(RegNum, ParkTime, TableName = "CarParkingInfo"): # Добавляет регНомер и время в БД
    try:
        DBconnect = sqlite3.connect(DataBaseName) # Подключение к базе (возмжоно нужно ватащить наружу)
        cursor = DBconnect.cursor()
        cursor.execute("INSERT INTO {} (RegNumber, ParkingTime) VALUES ('{}','{}')".format(TableName, RegNum, ParkTime))
        DBconnect.commit() # Синхронизирует изменения с баззой
        DBconnect.close()
    except Exception as e:
        print("Ошибка при занесении данных в базу: " + e)
        return None

def GetTime(RegNum, TableName = "CarParkingInfo"):
    try:
        DBconnect = sqlite3.connect(DataBaseName)
        cursor = DBconnect.cursor()
        cursor.execute("SELECT ParkingTime FROM {} WHERE RegNumber='{}'".format(TableName, RegNum))
        res = cursor.fetchall()
        DBconnect.close()
        return res
    except Exception as e:
        print("Ошибка при получении времени из базы: " + e)
        return None

def DelFromDataBase(RegNumber, TableName = "CarParkingInfo"):  # Удаляет каждое упоминание о номере
    try:
        DBconnect = sqlite3.connect(DataBaseName)
        cursor = DBconnect.cursor()
        cursor.execute("DELETE FROM {} WHERE RegNumber='{}'".format(TableName, RegNumber))
        DBconnect.commit()
        DBconnect.close()
    except Exception as e:
        print("Ошибка при удалении из базы: " + e)
        return None

def SetUnparking(UnParkingTime, RegNumber, TableName = "CarParkingInfo"):
    try:
        DBconnect = sqlite3.connect(DataBaseName)
        cursor = DBconnect.cursor()
        cursor.execute("UPDATE {} SET OutTime='{}' WHERE RegNumber='{}'".format(TableName, UnParkingTime, RegNumber))
        DBconnect.commit()
        DBconnect.close()
    except Exception as e:
        print("Ошибка при задавании времени выезда в базу: " + e)
        return None