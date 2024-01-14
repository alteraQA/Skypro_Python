class Address:
    def __init__(self, index, city, street, house, apartment):
        self.addressindex=index
        self.addresscity=city
        self.addressstreet=street
        self.addresshouse=house
        self.addressapartment=apartment
    def __str__(self):
        return f"{self.addressinde}, {self.addresscity}, {self.addressstreet}, {self.addresshouse}, {self.addressapartment}"  
