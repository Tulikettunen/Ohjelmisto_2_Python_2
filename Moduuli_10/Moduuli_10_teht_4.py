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

class Kilpailu:
    def __init__(self, kilpailun_nimi, kilpailun_pituus, auto_lista):
        self.kilpailun_nimi = kilpailun_nimi
        self.kilpailun_pituus = kilpailun_pituus
        self.auto_lista = []

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

    def info_print(self):
        for auto in self.auto_lista:
            print(f"Auton rekisteritunnus: {self.rek_tunnus}, \nhuippunopeus: {self.top_speed}, "
                  f"\nnopeus juuri nyt: {self.speed_now}, \nja kuljettu matka: {self.distance}.\n")

