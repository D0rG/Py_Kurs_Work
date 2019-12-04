import datetime
import re
class Car(object):

    Liters = ['а', 'в', 'е', 'к', 'м', 'н', 'о', 'р', 'с', 'т', 'у', 'х']  # Все буквы из автомобильных номеров
    Color = ""
    RegNum = ""  # Номер выглядит так wNNNwwNNN
    ID = None

    def __init__(self, Color, RegNum):
        try:
            if(re.match("\w{1}\d{3}\w{2}\d{2,3}", RegNum) and len(RegNum) < 10):
                self.Color = Color
                self.RegNum = RegNum
                self.SetId()
            #     print("Номер действителен")
            # else:
            #     print("номер не действителен")
        except Exception as e:
            ID = None
            # print(e)

    def SetId(self): # Задаёт ID, получает его изменением РегНомера. Для сотрировки.
        RegNumber = self.RegNum
        for liter in range(0, len(self.Liters)):
            RegNumber = RegNumber.replace(self.Liters[liter], str(liter + 1))
        self.ID = int(RegNumber)
