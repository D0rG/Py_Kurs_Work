import datetime
import re
class Car(object):

    Liters = ['а', 'в', 'е', 'к', 'м', 'н', 'о', 'р', 'с', 'т', 'у', 'х']  # Все буквы из автомобильных номеров
    Color = ""
    RegNum = ""  # Номер выглядит так wNNNwwNNN
    ID = 0

    def __init__(self, Color, RegNum):
        if(re.match("\w{1}\d{3}\w{2}\d{3}", RegNum)):
            self.Color = Color
            self.RegNum = RegNum
            print("Номер действителен")
        else:
            print("номер не действителен")

    def GetRegNum(self):
        return self.RegNum

    # def SetID(self):  # Код которого не должно существовать
    #     if(self.RegNum != ""):
    #         id = 0
    #         f = open("Nums.txt", 'a')
    #
    #         for Lit in self.Liters:
    #             for Num in range(1, 1000):
    #                 for Lit2 in self.Liters:
    #                     for Lit3 in self.Liters:
    #                         for Reg in range(1, 1000):
    #                             if(Num < 10):
    #                                 NewNum = "00" + str(Num)
    #                             elif(Num < 100):
    #                                 NewNum = "0" + str(Num)
    #                             else:
    #                                 NewNum = str(Num)
    #
    #                             if(Reg < 10):
    #                                 NewReg = "0" + str(Reg)
    #                             else:
    #                                 NewReg = str(Reg)
    #
    #                             AutoNum = Lit + NewNum + Lit2 + Lit3 + NewReg
    #                             AutoNum = AutoNum + " " + str(id) + "\n"
    #                             f.write(AutoNum)
    #                             id += 1
    #         f.close()
