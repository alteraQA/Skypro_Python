from address import Address
from mailing import Mailing

# Создаем экземпляр класса Address для to_address
to_address = Address("100018", "г. Караганда", "16 микрорайон", "Дом 7", "Квартира 888")

# Создаем экземпляр класса Address для from_address
from_address = Address("630117", "г. Новосбирск", "Бульвар Молодежи", "Дом 44", "Квартира 555")

# Создаем экземпляр класса Mailing
mailing_instance = Mailing(to_address, from_address, 100, "track77777777777777")

# Выводим информацию о почтовом отправлении
print(f"Отправление {mailing_instance.track} из {to_address.addressindex}, {to_address.addresscity}, {to_address.addressstreet}, {to_address.addresshouse}, {to_address.addressapartment} "
      f"в {from_address.addressindex}, {from_address.addresscity}, {from_address.addressstreet}, {from_address.addresshouse} - {from_address.addressapartment}. Стоимость {mailing_instance.cost} рублей.")