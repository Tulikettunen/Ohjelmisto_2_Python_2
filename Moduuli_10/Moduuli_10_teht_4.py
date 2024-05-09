"""
Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina
kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa
parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa
on seuraavat metodit:

    tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät
    toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.

    tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.

    kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun
    kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.

Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia,
jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi. Ajantasainen
tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen
jälkeen, kun kilpailu on päättynyt.
"""

import random

#def main():
#    suuri_romuralli = Kilpailu('Suuri romuralli', 8000, 10)

  ##  for i in range(1, 11):
    ##    suuri_romuralli.auto_lista.append(Auto((f"ABC-{i}"), random.randint(100, 200)))

class Kilpailu:

    def __init__(self, kilpailun_nimi, kilpailun_pituus, lkm):
        self.kilpailun_nimi = kilpailun_nimi
        self.kilpailun_pituus = kilpailun_pituus
        self.auto_lista = []

    def an_hour(self):
        for auto in self.auto_lista:
            speed_change = random.randint(-10, 15)
            if speed_change + auto.speed_now > auto.top_speed:
                auto.speed_now = auto.top_speed
            elif auto.speed_now + speed_change < 0:
                auto.speed_now = 0
            else:
                auto.speed_now += speed_change
            travel_time = 1
            auto.distance += auto.speed_now * travel_time

    def race_over(self):
        is_race_over = False
        for auto in self.auto_lista:
            if auto.distance > 8000:
                self.is_race_over = True
        return is_race_over

    def info_print(self):
        for auto in self.auto_lista:
            print(f"__________________________________\n"
                  f"Auton rekisteritunnus: {auto.rek_tunnus}, \nhuippunopeus: {auto.top_speed}, "
                  f"\nnopeus juuri nyt: {auto.speed_now}, \nja kuljettu matka: {auto.distance}.\n")
"""
    for i in range (lkm):
        auto = Auto("ABC-" + str(i+1), random.randint(100,200))
        self.auto_lista.append(auto)
    while not self.race_over():
        self.an_hour()
        self.info_print()
"""




class Auto:
    def __init__(self, rek_tunnus, top_speed):
        self.rek_tunnus = rek_tunnus
        self.top_speed = top_speed
        self.speed_now = 0
        self.distance = 0



suuri_romuralli = Kilpailu('Suuri romuralli', 8000, 10)

for i in range(1, 11):
    suuri_romuralli.auto_lista.append(Auto((f"ABC-{i}"), random.randint(100, 200)))

i = True
while i:
    time_passed = 0
    if suuri_romuralli.race_over() == False:
        suuri_romuralli.an_hour()
        time_passed =+ 1
        if time_passed % 10 == 0:
            for auto in suuri_romuralli.auto_lista:
                suuri_romuralli.info_print()
    else:
        print("Kilpailu on ohi! Viimeiset tulostiedot:")
        suuri_romuralli.info_print()
        for auto in suuri_romuralli.auto_lista:
            if auto.distance > 8000:
                print(f"Kilpailun voittanut auto {auto.rek_tunnus}.")
        i = False

#suuri_romuralli.auto_lista[auto].rek_tunnus


#if __name__ == "__main__":
#    main()