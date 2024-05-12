"""
Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat
alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa
julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien
julkaisujen kaikki tiedot toteuttamiesi metodien avulla.
"""

class Julkaisu():
    def __init__(self, name):
        self.name = name


class Kirja(Julkaisu):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_info(self):
        print(f"{self.name}: Kirjailija {self.author}, {self.pages} sivua.")

class Lehti(Julkaisu):
    def __init__(self, name, reporter):
        super().__init__(name)
        self.reporter = reporter

    def print_info(self):
        print(f"{self.name}, Toimittaja {self.reporter}.")



kirja1 = Kirja( 'Hytti n:o 6', 'Rosa Liksom', 200)
lehti1 = Lehti('Aku Ankka', 'Aki Hyyppä')

kirja1.print_info()
lehti1.print_info()