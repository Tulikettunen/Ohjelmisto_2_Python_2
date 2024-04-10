"""
Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti
"ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
Tämä tehdään kutsumalla kiihdytä-metodia.

Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
"""
import random

class Auto:
    def __init__(self, rek_tunnus, top_speed):
        self.rek_tunnus = rek_tunnus
        self.top_speed = top_speed
        self.speed_now = 0
        self.distance = 0

    def info_print(self):
        print(f"Auton rekisteritunnus: {self.rek_tunnus}, \nhuippunopeus: {self.top_speed}, "
              f"\nnopeus juuri nyt: {self.speed_now}, \nja kuljettu matka: {self.distance}.\n")


    def kiihdytä(self):
        speed_change = random.randint(-10, 15)
        if speed_change + self.speed_now > self.top_speed:
            self.speed_now = self.top_speed
        elif self.speed_now + speed_change < 0:
            self.speed_now = 0
        else:
            self.speed_now += speed_change


    def kulje(self):
        travel_time = 1
        self.distance += self.speed_now * travel_time


auto_lista = []

for i in range(1, 11):
    auto_lista.append(Auto((f"ABC-{i}"), random.randint(100, 200)))

i = True

while i:    # Lyhenne muodosta 'while i == True'
    for auto in auto_lista:
        if auto.distance > 10000:
            i = False

    for auto in auto_lista:
        auto.kiihdytä()
        auto.kulje()


for auto in auto_lista:
    auto.info_print()
