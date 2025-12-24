from lesson_03.smartphone import Smartphone

catalog = [
    Smartphone("Nokia", "3110", "+79999999999"),
    Smartphone("Huawei", "p50", "+78888888888"),
    Smartphone("Xiaomi", "h10", "+77777777777"),
    Smartphone("Huawei", "P20pro", "+7666666666666"),
    Smartphone("Motorola", "c350", "+444444444444")
]

for mobile in catalog:
    print(f"{mobile.brand} - {mobile.model}. {mobile.number}")
