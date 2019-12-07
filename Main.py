import random
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtSql import QSqlRelationalTableModel, QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QTableWidgetItem

from MainWindow import Ui_MainWindow

from DataBase import *
from Parking import Parking

# Много стеков.

# car = Car("Blue", "к777рс777")
# Park = Parking("New Park", 10, 11)
# print(str(GetMaxPlaceDef("Parking")))

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

#AddToVIP(car)
# y = input()
#print(car.RegNum)
#AddToDataBase(car, None)
#SetUnparking(None,  car)
#DelFromDataBase(car)
#SetUnparking(str(datetime.datetime.now()), car)
# AddMaxPlaceDef(-10)
# AddMaxPlaceVIP(-122)
# AddFreePlaceDef(-23)
# AddFreePlaceVIP(-34)



class Mywin(QtWidgets.QMainWindow):
    ParkingsList = []
    CountList = 0
    def __init__(self):  # Инициирует каждую кнопку
        super(Mywin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Py_Kurs_Work")
        self.ui.PrintDB.clicked.connect(self.DrawOnTimeTable)
        self.ui.Table.setColumnCount(4)  # Кол-во столбов
        self.ui.BTCreatePark.clicked.connect(self.AddParking)
        self.ui.BtDelPark.clicked.connect(self.DellParking)

    def AddParking(self):  # Добавляет парковку в лист парковок
        ParkName = self.ui.TbParkName.text()
        MaxPlaceDef = self.ui.TbMaxDef.text()
        MaxPlaceVIP = self.ui.TbMaxVIP.text()
        self.ui.TbMaxVIP.setText(None)
        self.ui.TbMaxDef.setText(None)
        self.ui.TbParkName.setText(None)
        try:
            self.ParkingsList.append(Parking(ParkName, int(MaxPlaceDef), int(MaxPlaceVIP)))
            self.CountList -=-1
            self.UpdateParkComboBox()
        except Exception as e:
            print(e)

    def DellParking(self):
        text = self.ui.SelectDelPark.currentText()
        if(self.CountList > 0):  # Если нет парковок, то не пытаться их удалить
            for i in range(self.CountList):
                park = self.ParkingsList[i]
                if(park.Name == text and park.BusyPlaceDef()):  # Если нашлось имя такое же как у нужной парковки и на ней нет машин, то можно удалять
                    self.ParkingsList[i].Dell()  # Удаляет парковку из БД
                    self.ParkingsList.pop(i)  # Удаляет эллемент по индексу
                    self.UpdateParkComboBox()  # Обновляет все комбобоксы
                    self.CountList -= 1
                    break
                elif(park.Name == text and not park.BusyPlaceDef()):  # Не удалять парковку, пока на ней находиться автомобиль
                    print("На парковке ещё есть автомобили")
                    break


    def UpdateParkComboBox(self):  # Обнавляет все комбобоксы с парковками
        self.ui.SelectDelPark.clear()
        self.ui.SelectPark.clear()
        self.ui.SelectParkLeave.clear()

        for park in self.ParkingsList:
            self.ui.SelectDelPark.addItem(park.Name)
            self.ui.SelectPark.addItem(park.Name)
            self.ui.SelectParkLeave.addItem(park.Name)

    def DrawOnTimeTable(self):  # Рисует выбранную пользователем БД
        try:
            buf = self.ui.SelectDB.currentIndex()
            if(buf == 0):
                data = ReturnTeble("CarParkingInfo")  # Имя таблицы из которой будет рисоваться таблица
                row = 0  # Строка
                self.ui.Table.setRowCount(len(data))  # Кол-во строк
                self.ui.Table.setColumnCount(4)  # Кол-во столбов
                self.ui.Table.setHorizontalHeaderLabels(("ID", "Номер", "Время вьезда", "Время выезда"))  # Имена столбов у таблицы
                for tup in data:  # Строка не поделённая на столбы
                    col = 0  # Столбец
                    for item in tup:  # Значение каждой клетки в одной строке (Разных стобах)
                        cellinfo = QTableWidgetItem(str(item))  # Задаёт элемент
                        cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Только для чтения
                        self.ui.Table.setItem(row, col, cellinfo)  # Вставляет элемент в определённую ячейку по строке/столбу
                        col += 1
                    row += 1

            elif(buf == 1):
                data = ReturnTeble("Places")
                row = 0
                self.ui.Table.setRowCount(len(data))  # Кол-во строк
                self.ui.Table.setColumnCount(len(data[0]))  # Кол-во столбов
                self.ui.Table.setHorizontalHeaderLabels(("Имя парковки", "Макс. места на обычной","Занятое место на обычной", "Макс. места на VIP","Занятое место на VIP"))
                for tup in data:
                    col = 0

                    for item in tup:
                        cellinfo = QTableWidgetItem(str(item))
                        cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Только для чтения
                        self.ui.Table.setItem(row, col, cellinfo)
                        col += 1
                    row += 1

            elif(buf == 2):
                data = ReturnTeble("VIP_List")
                row = 0
                self.ui.Table.setRowCount(len(data))  # Кол-во строк
                self.ui.Table.setColumnCount(len(data[0]))  # Кол-во столбов
                self.ui.Table.setHorizontalHeaderLabels(("Автомобильный номер", ""))
                for tup in data:
                    col = 0
                    for item in tup:
                        cellinfo = QTableWidgetItem(str(item))
                        cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Только для чтения
                        self.ui.Table.setItem(row, col, cellinfo)
                        col += 1
                    row += 1

        except Exception as e:
            self.ui.Table.setColumnCount(2)
            self.ui.Table.setRowCount(1)
            self.ui.Table.setItem(0, 0, QTableWidgetItem("Ошибка при выводе БД"))
            self.ui.Table.setItem(0, 1, QTableWidgetItem(str(e)))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Mywin()
    win.show()
    sys.exit(app.exec())

