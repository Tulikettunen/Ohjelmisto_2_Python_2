"""
Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina
annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä
talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena. Kirjoita
taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen. Kirjoita
pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.
"""

class Building():
    def __init__(self, first_floor, last_floor, no_of_elevs):
        self.first_floor = first_floor
        self.last_floor = last_floor
        self.no_of_elevs = no_of_elevs
        self.hissi_lista = []
        for i in range(no_of_elevs):
            self.hissi_lista.append(Hissi(first_floor, last_floor))

    def drive_elev(self, milla_hissilla, mihin_kerrokseen):
        if milla_hissilla + 1 > self.no_of_elevs or milla_hissilla <= -1:
            print(f"The elevator you chose doesn't exist, please choose another elevator. No. of elevators: {self.no_of_elevs}")
        elif mihin_kerrokseen == self.hissi_lista[milla_hissilla].current_floor:
            print(f"The floor you are is {mihin_kerrokseen}.")
        elif mihin_kerrokseen > self.hissi_lista[milla_hissilla].current_floor and mihin_kerrokseen < self.hissi_lista[
            milla_hissilla].last_floor:
            for i in range(mihin_kerrokseen - self.hissi_lista[milla_hissilla].current_floor):
                self.hissi_lista[milla_hissilla].next_floor()
            print(f"The floor you are now is {self.hissi_lista[milla_hissilla].current_floor}.")
        elif mihin_kerrokseen < self.hissi_lista[milla_hissilla].current_floor and mihin_kerrokseen > self.hissi_lista[
            milla_hissilla].first_floor:
            for i in range(self.hissi_lista[milla_hissilla].current_floor - mihin_kerrokseen):
                self.hissi_lista[milla_hissilla].one_floor_down()
            print(f"The floor you are now is {self.hissi_lista[milla_hissilla].current_floor}.")
        else:
            print(
                f"The floor you tried to choose doesn't exist. The floor you are at is {self.hissi_lista[milla_hissilla].current_floor}, "
                f"first floor is {self.hissi_lista[milla_hissilla].first_floor} and last floor is {self.hissi_lista[milla_hissilla].last_floor}")


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


talo = Building(1, 9, 3)

e = True

while e:
    try:
        command = input("If you want to drive an elevator, press enter \nIf you want to quit press 'q', "
                        "\nIn case of emergency, press '!'.\n>")
        if command != "!":
            milla_hissilla = int(input("Which elevator do you want to use? \n>")) - 1
            mihin_kerrokseen = int(input("In to which floor do you want to go? \n>"))
            talo.drive_elev(milla_hissilla, mihin_kerrokseen)
        elif command.upper == "Q":
            print("'Driving elevator' program have been  stopped.")
            e = False
        else:
            print("Emergency button activated.")
            e = False
    except ValueError:
        print("You can only choose numbers.\n")



