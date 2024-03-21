"""
Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan
nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa.
Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa
kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten,
että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h
ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.
"""


class Auto:
    def __init__(self, rek_tunnus, top_speed):
        self.rek_tunnus = rek_tunnus
        self.top_speed = top_speed
        self.speed_now = 0
        self.distance = 0

    def info_print(self):
        print(f"Auton rekisteritunnus: {self.rek_tunnus}, huippunopeus: {self.top_speed}, "
              f"nopeus juuri nyt: {self.speed_now} ja kuljettu matka: {self.distance}")

    def kiihdytä(self, speed_change):
        if speed_change + self.speed_now > self.top_speed:
            self.speed_now = self.top_speed
        elif self.speed_now + speed_change < 0:
            self.speed_now = 0
        else:
            self.speed_now += speed_change

auto_1 = Auto("ABC-123", 142)


auto_1.kiihdytä(30)
print(f"Auton {auto_1.rek_tunnus} uusi nopeus on nyt {auto_1.speed_now} km/h.")

auto_1.kiihdytä(70)
print(f"Auton {auto_1.rek_tunnus} uusi nopeus on nyt {auto_1.speed_now} km/h.")

auto_1.kiihdytä(50)
print(f"Auton {auto_1.rek_tunnus} uusi nopeus on nyt {auto_1.speed_now} km/h.")

auto_1.kiihdytä(-200)
print(f"Auto {auto_1.rek_tunnus} teki hätä jarrutuksen, ja sen nykyinen nopeus on {auto_1.speed_now} km/h.")


auto_1.info_print()