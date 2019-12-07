import datetime
import re
class Car(object):

    Liters = ['а', 'в', 'е', 'к', 'м', 'н', 'о', 'р', 'с', 'т', 'у', 'х']  # Все буквы из автомобильных номеров
    Color = ""
    RegNum = ""  # Номер выглядит так wNNNwwNNN
    ID = None

    def __init__(self, Color, RegNum):
        if(isinstance(Color, str) and isinstance(RegNum, str)):
            try:
                if(re.match("\w{1}\d{3}\w{2}\d{2,3}", RegNum) and len(RegNum) < 10):  # Проверяет соответствует ли номер данному патрену (номер РФ)
                    self.Color = Color
                    self.RegNum = RegNum
                    self.SetId()
            except Exception as e:
                ID = None
        else:
            ID = None

    def SetId(self): # Задаёт ID, получает его изменением РегНомера. Для сотрировки.
        RegNumber = self.RegNum
        for liter in range(0, len(self.Liters)):
            RegNumber = RegNumber.replace(self.Liters[liter], str(liter + 1))
        self.ID = int(RegNumber)
