"""
Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa
kerroksessa. Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy
viidenteen kerrokseen. Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin
ja ilmoittavat, missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa
hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.
"""


class Hissi():
    def __init__(self, first_floor, last_floor):
        self.first_floor = first_floor
        self.last_floor = last_floor
        self.current_floor = first_floor

    def next_floor(self):
        self.current_floor += 1
        return self.current_floor


    def one_floor_down(self):
        self.current_floor -= 1
        return self.current_floor


hissi = Hissi(1, 7)

mihin_kerrokseen = int(input("In to which floor do you want to go? \n>"))

if mihin_kerrokseen == hissi.current_floor:
    print(f"The floor you are is {mihin_kerrokseen}.")
elif mihin_kerrokseen > hissi.current_floor and mihin_kerrokseen < hissi.last_floor:
    for i in range (mihin_kerrokseen - hissi.current_floor):
        hissi.next_floor()
    print(f"The floor you are now is {hissi.current_floor}.")
elif mihin_kerrokseen < hissi.current_floor and mihin_kerrokseen > hissi.first_floor:
    for i in range(hissi.current_floor - mihin_kerrokseen):
        hissi.one_floor_down()
    print(f"The floor you are now is {hissi.current_floor}.")
else:
    print(f"The floor you tried to choose doesn't exist. The floor you are at is {hissi.current_floor}, "
          f"first floor is {hissi.first_floor} and last floor is {hissi.last_floor}")
