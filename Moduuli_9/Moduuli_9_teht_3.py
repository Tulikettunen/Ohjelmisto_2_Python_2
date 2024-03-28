"""
Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa
tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.
"""

# ohjelmaa muokattu edellisestä sen verran, että myös nopeuden lisäykset voidaan laittaa
# inputtina käyttäjältä

# Hups, se vähän eskaloitu.


class Auto:
    def __init__(self, rek_tunnus, top_speed):
        self.rek_tunnus = rek_tunnus
        self.top_speed = top_speed
        self.speed_now = 0
        self.distance = 0


    def info_print(self):
        print(f"Auton rekisteritunnus: {self.rek_tunnus}, \nhuippunopeus: {self.top_speed}, "
              f"\nnopeus juuri nyt: {self.speed_now} \nja kuljettu matka: {self.distance}\n")


    def kiihdytä(self):
        y = True
        while y:
            try:
                speed_change = int(input("Kuinka paljon nopeus on muuttunut? (km/h): \n >"))
                if speed_change + self.speed_now > self.top_speed:
                    self.speed_now = self.top_speed
                    print(f"Olet saavuttanut maksiminopeuden, {self.top_speed} km/h.\n")
                elif self.speed_now + speed_change < 0:
                    self.speed_now = 0
                    print("Olet jarruttanut auton pysähdyksiin, nopeutesi on 0km/h.\n")
                else:
                    self.speed_now += speed_change
                    if speed_change < -80:
                        print(f"Auto {auto_1.rek_tunnus} teki hätä jarrutuksen, ja sen nykyinen nopeus on {auto_1.speed_now} km/h.\n")
                    else:
                        print(f"Uusi nopeutesi on {self.speed_now} km/h.\n")
                y = False
            except ValueError:
                print("Syötätkö tähän kenttään numeroita vaan, tänks.\n")


    def kulje(self):
        # tähän kohtaan pitäisi lisätä ehto että käyttäjä ei voi syöttää negatiivista aikaa
        e = True
        while e:
            try:
                travel_time = float(input("Kuinka monta tuntia nykyisellä nopeudella on kuljettu?: \n >"))
                if travel_time < 0:
                    print("Idiootti, et voi matkustaa ajassa taaksepäin, sorry.\n")
                else:
                    self.distance += self.speed_now * travel_time
                    print(f"Matka {self.speed_now * travel_time} km on lisätty matkamittariisi. \n"
                          f"Nykyinen kuljettu kokonaismatkasi on {self.distance} km.\n")
                    e = False
            except ValueError:
                print("Syötätkö tähän kohtaan numeroita vaan tänks.\n")

auto_1 = Auto("ABC-123", 142)

i = True
while i:
    choice = input("Haluatko muuttaa nopeutta (1) \n"
                   "kertoa kauanko olet kulkenut kyseisellä nopeudella (2) \n"
                   "tai Lopettaa? (any other key) \n>")
    if choice == "1":
        auto_1.kiihdytä()
    elif choice == "2":
        auto_1.kulje()
    else:
        i = False


"""
auto_1.kiihdytä()   # tässä kohtaa aluksi lisättiin nopeutta 30 km/h
auto_1.kulje()      # laita tähän kohtaan haluamasi aika

auto_1.kiihdytä()   # tässä kohtaa aluksi lisättiin nopeutta 70 km/h
auto_1.kulje()

auto_1.kiihdytä()   # tässä kohtaa aluksi lisättiin nopeutta 50 km/h
auto_1.kulje()

auto_1.kiihdytä()   # tässä kohtaa aluksi vähennettiin nopeutta -200 km/h
auto_1.kulje()
"""

print("Auton tiedot matkan lopuksi:")
auto_1.info_print()

