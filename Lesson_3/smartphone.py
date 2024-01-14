class Smartphone:
    def __init__(self, brand, model, number):
        self.phonebrand=brand
        self.phonemodel=model
        self.phonenumber=number

    def __str__(self):
        return f"{self.phonebrand} , {self.phonemodel}, {self.phonenumber}"
    def sayBrand(self):
        print("Марка телефона", self.phonebrand)
    def sayModel(self):
        print("Модель телефона", self.phonemodel)
    def sayNumber(self):
        print("Абонентский номер", self.phonenumber)