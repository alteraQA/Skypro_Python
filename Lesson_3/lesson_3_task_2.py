from smartphone import Smartphone

phone1=Smartphone("Apple", "iPhone11", "+7-913-000-00-00")
phone2=Smartphone("Apple", "iPhone12", "+7-913-000-00-01")
phone3=Smartphone("Apple", "iPhone13", "+7-913-000-00-02")
phone4=Smartphone("Xiaomi", "MiA1", "+7-913-000-00-03")
phone5=Smartphone("Xiaomi", "MiA2", "+7-913-000-00-04")

catalog=[phone1, phone2, phone3, phone4, phone5]
l=len(catalog)
for x in range(0, l):
    print(catalog[x])