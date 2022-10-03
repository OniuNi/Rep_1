#2. Faceti exercitiul dupa ce ati urcat proiectul (tot ce am facut pana acum impreuna)
class FormaGeometrica:
    def __init__(self, PI = 3.14):
        self.__latura = "latura"
    def description(self):
        print("Cel mai probabil am colturi")
    def get_latura(self):
        self.__latura = 12
    def set_latura(self):
        self.__latura = 12
    def del_latura(self):
        self.__latura = 0
    def aria(self):
        pass
#ABSTRACTION
#Clasa abstracta FormaGeometrica
#Contine un field PI=3.14
#Contine o metoda abstracta aria (optional)
#Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’

from abc import ABC, abstractmethod
class FormaGeometrica:
    def __init__(self, PI = 3.14):
        self.__latura = "latura"
    def description(self):
        print("Cel mai probabil am colturi")
    def get_latura(self):
        self.__latura = 12
    def set_latura(self):
        self.__latura =12
    def del_latura(self):
        self.__latura = 0
    @abstractmethod
    def aria(self):
        raise NotImplementedError

#INHERITANCE
#Clasa Patrat - mosteneste FormaGeometrica
#constructor pt latura

class Patrat(FormaGeometrica):
    def __init__(self):
        super().__init__()
        self.__latura = "latura"
    def latura(self):
        print("Cele 4 laturi sunt egale")
    def description(self):
        print("Cel mai probabil am colturi")
    def get_latura(self):
        self.__latura = 12
    def set_latura(self):
        self.__latura =12
    def del_latura(self):
        self.__latura = 0
    def aria(self):
        raise NotImplementedError
patrat= Patrat()
patrat.latura()
patrat.description()


#ENCAPSULATION
#latura este proprietate privata
#Implementati getter, setter, deleter pt latura
#Implementati metoda ceruta de interfata (optional, doar daca ati ales sa implementati metoda abstracta aria)

class Patrat(FormaGeometrica):
    def __init__(self):
        super().__init__()
        self.__latura = "latura"
    def description(self):
        print("Cel mai probabil am colturi")
    def get_latura(self):
       self.__latura = 12
    def set_latura(self):
        self.__latura = 12
    def del_latura(self):
        self.__latura = 0
    def aria(self):
        raise NotImplementedError
l1 = Patrat()
l1.get_latura()
l1.set_latura()
l1.del_latura()


#Clasa Cerc - mosteneste FormaGeometrica
#constructor pt raza
#raza este proprietate privata
#Implementati getter, setter, deleter pt raza
#Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte (optional, doar daca ati ales sa implementati metoda abstracta aria)
class  Cerc(FormaGeometrica):
    def __init__(self):
        super().__init__()
    def raza(self):
        self.__raza = "raza"
    def set_raza(self, valoare_raza):
        self.__raza = valoare_raza
    def get_raza(self):
        return self.raza
    def raza (self, valoare_raza, noua_raza=None):
        self.__raza = noua_raza
    def aria(self):
        raise NotImplementedError
cerc_1 = Cerc()
cerc_1.get_latura()
cerc_1.set_latura()
cerc_1.del_latura()

#POLYMORPHISM
#Definiti o noua metoda descrie - printati ‘Eu nu am colturi’


#Creati un obiect de tip Patrat si jucati-va cu metodele lui
#Creati un obiect de tip Cerc si jucati-va cu metodele lui



#3.  Creati o clasa Student cu 2 atribute:
#- name: str, numele studentului
#3- grade: int, nota acestuia
#Nota nu trebuie sa fie primita neaparat la initializare si trebuie sa nu poata fi accesata din afara clasei.
#a) Scrieti 2 functii pentru nota: get_grade care sa returneze nota studentului si set_grade care sa ii modifice nota. Asigurati`va ca nota e corecta, in caz contrar aruncati o exceptie custom (clasa) cu un mesaj relevant  - probabil va trebui sa Google-uiti putin pt exceptie :)
#b) Scrieti o functie care sa descrie studentul: "The student`s name is .... and has the grade ..." si permiteti afisarea  descrierii prin intermediul functiei print de ex:
#s = Student(...)
#print(s)
#c) Testati cele 3 functii creandu-va un student caruia sa ii dati nota 7, sa ii afisati detaliile, dupa care sa ii modificati nota in 10 si sa o afisati, iar ulterior sa o modificati in 12 pt a testa exceptia.

class Student:
    name = "Nicoleta"
    grade = 8
    def __init__(self):
        self.grade = 8
    def get_grade(self):
        return self.grade
    def set_grade(self, new_grade=7):
        self.grade = new_grade
    def description(self):
     print(f'The student`s name is {"name"} and has the grade {"grade"}')

s = Student()
print()

#4. Actualizati proiectul pe github facand un push la noul cod
#In Folder de teme ajunge sa puneti doar linkul cu proiectul vostru public
