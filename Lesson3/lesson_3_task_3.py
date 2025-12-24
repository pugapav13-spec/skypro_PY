from Address import Address
from Mailing import Mailing

to_address = Address("630001", "Новосибирск", "Линейная", "21", "41")
from_address = Address("650633", "Вавилон", "ИбнИажазура", "77", "18")

mailing = Mailing(to_address, from_address, 999, "AGKEIWIJWJSWKJJ20")

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - "
    f"{mailing.from_address.apartment} в {mailing.to_address.index}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)
