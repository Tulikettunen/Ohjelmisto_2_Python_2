"""
Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa
ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin. Uuden auton
nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma,
jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta
pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.
"""

# Tässä koodissa on myös paljon ylimääräistä, ja ylimääräisiä muistiinpanoja
# itseäni varten ja oppiakseni, ignore them please, thanks :)


class Auto:
    def __init__(self, rek_tunnus, top_speed):   # määrittää mikä ajetaan joka erta, millaisia tietoja oliolle luodaan
        self.rek_tunnus = rek_tunnus            # __init__ on metodi, joka __jotain__ ajaa kyseisen metodin aina.
        self.top_speed = top_speed              # Se on alustaja, eli constructor. __init__ ei ole pakollinen
        self.speed_now = 0
        self.distance = 0
        print("hei")    # itselle tarkistus että mikä toiminnallisuus tapahtuu missäkin kohtaa

    # lisää info_print metodin määrittelyn/funktion, joka toimii nimenomaan classin eli luokan metodina,
    # vain tätä luokkaa kutsuttaessa metodina
    def info_print(self):
        print(f"Auton rekisteritunnus: {self.rek_tunnus}, huippunopeus: {self.top_speed}, "
              f"nopeus juuri nyt: {self.speed_now} ja kuljettu matka: {self.distance}")

    def __str__(self):
        return (f"Tämä printtaa kutsuttaessa 'print(auto_x)' "
                f"jotain muuta kuin '<__main__.Auto object at 0x0000020E58C08770>'")


print("moi")    # tsekkaa missä kohtaa mitäkin printataan

auto_1 = Auto('ABC-123', 142)
# Luo objektin johon viitataan auto_1 termillä,
# ja joiden asetettavat parametrit ovat annetut arvot, paramtrit menevät __init__ funktioon/metodiin,
# joka pyöritetään automaattisesti tässä kohtaa vaikka sitä ei erikseen kutsuta

print("moi")    # tsekkaa missäkohtaa mitäkin printataan

print(auto_1)   # printtaa "<__main__.Auto object at 0x0000020E58C08770>"
                # jossa main pääohjelmassa on luotu .Auto objekt,
                # ja at xxxxx on muistipaikka

auto_1.info_print()     # kutsuu metodia info_print oliosta auto_1
