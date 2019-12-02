class Car(object): # номер выглядит так wNNNwwNNN
    Liters = ['а', 'в', 'е', 'к', 'м', 'н', 'о', 'р', 'с', 'т', 'у', 'х'] #все буквы из автомобильных номеров
    Color = ""
    RegNum = ""
    ID = 0

    def __init__(self, Color, RegNum):
        self.Color = Color
        self.RegNum = RegNum
        print("Создан обтект машина")

    def SetID(self):
        id = 0
        AutoNum = ""
        print("старт")

        for Lit in self.Liters:
            for Num in range(1, 1000):
                for Lit2 in self.Liters:
                    for Lit3 in self.Liters:
                        for Reg in range(1, 1000):
                            if(Num < 10):
                                NewNum = "00" + str(Num)
                            elif(Num < 100):
                                NewNum = "0" + str(Num)
                            else:
                                NewNum = str(Num)

                            if(Reg < 10):
                                NewReg = "0" + str(Reg)
                            else:
                                NewReg = str(Reg)

                            AutoNum = Lit + NewNum + Lit2 + Lit3 + NewReg
                            print(AutoNum)
                            print("\n")
                            id += 1


    def SeyWTF(self):
        print("WTF")