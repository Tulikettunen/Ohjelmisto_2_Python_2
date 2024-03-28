
class Animal:
    def __init__(self, species: str):
        self.species = species

    def speak(self):
        print("Animal is making sound.")

class Dog(Animal):
    def __init__(self, species: str, breed: str):
        self.species = species
        self.breed = breed

    def speak(self):
        print("Dog is making sound: Woof woof!.")

animal1 = Animal('Dog')
animal2 = Animal('Cat')
dog1 = Dog("Dog", "Golden retriever")


class Cat(Animal):
    def __init__(self, species: str, breed: str):
        super().__init__(species)
        self.breed = breed


animal1 = Animal("Dog")
animal1.speak()
dog1.speak()


class Person:
    def __init__(self, nimi: str, ikä: int):
        self.nimi = nimi
        self.ikä = ikä

    def tervehdys(self):
        print(f"Hei! mä oon henkilö {self.nimi}, ja {self.ikä} vuotias!")


class Student(Person):
    def __init__(self, nimi:str , ikä: int, opiskelija_numero: int):
        super().__init__(nimi, ikä)
        self.opiskelija_numero = opiskelija_numero

    def tervehdys(self):
        super().tervehdys()
        print(f"Hei! Mun opiskelijanumero on {self.opiskelija_numero}.")


person1 = Person("Oona", 23)
oppilas1 = Student("Olli", 20, 1234)

#Person.tervehdys(oppilas1)
oppilas1.tervehdys()


