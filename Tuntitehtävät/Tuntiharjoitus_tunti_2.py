import random

"""
#versio 1

class Food:
    pass        # Luodaan luokka eli class, joka on tyhjä,
                # laittamalla "pass" ohjelma ei syötä erroria, vaikka luokkaonkin tyhjä

food1 = Food()     #instance
print(food1)

food2 = Food()
print(food2)

food1.name = "jugurtti"
food2.name = "mansikka"


print(food1.name)
print(food2.name)
"""


# Versio 2
class Food:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return (f"Tähän printataan nyt se muistipaikkaa ja classia korvaava teksti.\n "
                f"Tämä asia on RUOKA! Ruoan nimi on {self.name}.\n")


    def info_sheet(self):
        print(f"Tämän ruoan tiedot ovat: \n Nimi: {self.name}.\n")


food1 = Food("jugurtti")
food2 = Food("mansikka")

print(food1.name)
print(food2.name)

food1.info_sheet()
food2.info_sheet()


class Ostoslista():
    def __init__(self, lista):
        self.lista = lista


lista1 = Ostoslista(["porkkana", "kurkku", "suklaa", "dopamiini sipsit"])

print(lista1.lista)


class School():
    def __init__(self, name):
        self.name = name
        self.student_list = []
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)


class Student():
    def __init__(self, name, studentnumber, subject, grade):
        self.name = name
        self.studentnumber = studentnumber
        self.subject = subject
        self.grade = grade
        self.courses = []


class Course():
    def __init__(self, name):
        self.name = name
        self.student_list = []

    def add_student(self, student):
        self.student_list.append(student)


student_number = ""


def student_number_generate():
    for i in range(1, 7):
        global student_number
        student_number += str(random.randint)
    return student_number

school1 = School("Metropolia")
school2 = School("Laurea")

student1 = Student("Mimosa", student_number_generate(), "TiVi", "1")
student2 = Student("Diago", student_number_generate(), "Tradenomi", "2")
student3 = Student("Joona", student_number_generate(), "Tivi", "5")
student4 = Student("Alina", student_number_generate(), "Tradenomi", "3")

course1 = Course("Matikka")
course2 = Course("Ohjelmointi")
course3 = Course("Fysiikka")
course4 = Course("Taloustiede")


school1.add_course(course1)
school1.add_course(course2)
school1.add_course(course3)
school2.add_course(course4)

course1.add_student(student1)
course1.add_student(student3)
course1.add_student(student2)
course4.add_student(student2)
course4.add_student(student4)



for course in school1.courses:
    print(course.name)
    for student in course.students:
        print(student.name)


class Kirja:
    def __init__(self, title):
        self.title = title


kirja_1 = Kirja("Aapinen")
kirja_2 = Kirja("Harry Potter")
kirja_3 = Kirja("Pokemon opas")
kirja_4 = Kirja("Insinöörin algebra")

class Library:
    def __init__(self, name, books):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)


kirjasto_1 = Library("Metkan kirjasto", [])
kirjasto_2 = Library("Kaupungin kirjasto", [])

kirjasto_2.add_book(kirja_2)
kirjasto_1.add_book(kirja_1)
kirjasto_1.add_book(kirja_2)
kirjasto_1.add_book(kirja_4)
kirjasto_2.add_book(kirja_3)


for book in kirjasto_1.books:
    print(book.title)



