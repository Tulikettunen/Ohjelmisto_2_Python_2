"""
Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. Sähköautolla on
ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden
ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman
kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden
polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan
kolmen tunnin verran ja tulosta autojen matkamittarilukemat.
"""

class Car:
    def __init__(self, rek_tunnus, top_speed):
        self.rek_tunnus = rek_tunnus
        self.top_speed = top_speed
        self.speed_now = 0
        self.distance = 0

    def drive(self):
        self.speed_now = random.randint(0, self.top_speed)
        travel_time = int(input("How long do you travel? \n>"))
        auto.distance += self.speed_now * travel_time

    def info_print(self):
        print(f"________________________________________\n"
              f"Register plade: {self.rek_tunnus},\n roadometer count: {self.distance} km. ")



class Electric(Car):
    def __init__(self, rek_tunnus, top_speed, battery_capacity):
        super().__init__(rek_tunnus, top_speed)
        self.battery_capacity = battery_capacity

    def info_print(self):
        super().info_print()
        print(f"Other information: \nBattery capacity: {self.battery_capacity}, ")



class Fuel(Car):
    def __init__(self, rek_tunnus, top_speed, gas_tank):
        super().__init__(rek_tunnus, top_speed)
        self.gas_tank = gas_tank

    def info_print(self):
        super().info_print()
        print(f"Other information: \n fuel runnin car, sixe in littres {self.gas_tank}

