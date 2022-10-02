# Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei

# 1. Clasa Cerc
# Atribute: raza, culoare
# Constructor pt ambele atribute

# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()
from math import pi


class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def describe_circle(self):
        print(f"Circle radius is {self.radius} and color is {self.color}")

    def area(self):
        return pi * self.radius ** 2

    def diameter(self):
        return 2 * self.radius

    def circumference(self):
        return 2 * pi * self.radius


c1 = Circle(5, 'green')
c2 = Circle(3, 'purple')

c1.describe_circle()
c2.describe_circle()

print(c1.area())
print(c2.area())

print(c1.diameter())
print(c2.diameter())

print(c1.circumference())
print(c2.circumference())


# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pt toate atributele

# Metode:
# descrie()
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().
class Rectangle:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    def describe_rectangle(self):
        print(f"Rectangle has length = {self.length}, width = {self.width} and color is {self.color}")

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def change_color(self, new_color):
        self.color = new_color


d1 = Rectangle(2, 4, 'black')
d1.describe_rectangle()
print(d1.area())
print(d1.perimeter())
d1.change_color('white')
print(d1.color)


# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele

# Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)

class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def describe(self):
        print(
            f"Emplyee`s first name is {self.first_name}, last name is {self.last_name} and has a salary of {self.salary}")

    def full_name(self):
        print(f"Employee`s full name is: {self.first_name} {self.last_name}")

    def monthly_salary(self):
        print(f"Monthly salary = {self.salary}")

    def annual_salary(self):
        print(f"Annual salary = {self.salary * 12}")


e1 = Employee("John", "Doe", 5000)
e1.describe()
e1.full_name()
e1.monthly_salary()
e1.annual_salary()


# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate

# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)
class Account:
    def __init__(self, iban, titulary, balance):
        self.iban = iban
        self.titulary = titulary
        self.balance = balance

    def show_balance(self):
        print(f"Titulary {self.titulary} with the accout {self.iban} has a balance of {self.balance}RON")

    def debit(self, amount):
        if amount > self.balance:
            print()
        else:
            self.balance -= amount
            print(f"{amount}RON has been debited from the account")

    def credit(self, amount):
        self.balance += amount
        print(f"{amount}RON has been credited to the account")


a1 = Account('RORONWHATEVER66666633999', 'Badea Gheorghe', 1_000_000)
a1.show_balance()
a1.debit(100)
a1.show_balance()
a1.credit(1_000_000)
a1.show_balance()

# 5.Clasa Factura
# Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie

# Metode:
# schimba_cantitatea(cantitate)
# schimba_pretul(pret)
# schimba_nume_produs(nume)
# genereaza_factura() - va printa tabelar daca reusiti

# Factura seria x numar y
# Data: generati automat data de azi
# Produs | cantitate | pret bucata | Total
# Telefon |      7       |       700       | 4900
from datetime import date


class Bill:
    series = "7777.2.555.88.8"

    def __init__(self, number, product_name, quantity, price_per_unit):
        self.number = number
        self.product_name = product_name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def change_quantity(self, new_quantity):
        self.quantity = new_quantity

    def change_price(self, new_ppu):
        self.price_per_unit = new_ppu

    def change_product_name(self, new_prod_name):
        self.product_name = new_prod_name

    def generate_bill_v1(self):
        print(
            f"Date: {date.today()}\nProduct|Quantity|Price per unit|Total\n{self.product_name}|{self.quantity}|{self.price_per_unit}|{self.quantity * self.price_per_unit}")

    def generate_bill_v2(self):
        print(f"Date: {date.today()}\n| Product | Quantity | Price per unit | Total |")
        print("-" * 47)
        print(
            f"| {self.product_name:^8}|{self.quantity:^10}|{self.price_per_unit:^16}|{self.quantity * self.price_per_unit:^7}|")  # :^ dupa atributul dintre acolade aliniaza valoarea la centru


b1 = Bill(1001, "Telefon", 7, 700)
b1.generate_bill_v1()

print('\nv2:')

b1.generate_bill_v2()


# 6. Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate masinile cand ies din fabrica sunt gri
# Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
# Culori disponibile = alegeti voi 5-7 culori
# Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
# Inmatriculata = False

# Constructor: model, viteza_maxima

# Metode:
# descrie() (se vor printa toate atributele, inafara de culori_disponibile)
# inmatriculare() - va schimba atributul inmatriculata in True
# vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
# accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
# franeaza() - masina se va opri si va avea viteza 0
class SpeedError(Exception):
    pass


class Car:
    def __init__(self, model, max_speed):
        self.brand = "Tesla"
        self.model = model
        self.max_speed = max_speed
        self.current_speed = 0
        self.color = 'Grey'
        self.colors_available = set(["Grey", "White", "Black", "Red", "Blue", "Green", "Purple",
                                     "Orange"])  # sau {"Grey", "White", "Black", "Red", "Blue", "Green", "Purple"}
        self.is_licensed = False

    def describe(self):
        print(
            f"""Congratz, you got yourself a new {self.brand} {self.model} car. It reaches an astonishing max speed of {self.max_speed}km/h. """
            f"""Currently it is colored {self.color}, but keep in mind that you can change that anytime for a modest amount of 99999$ ;). """
            f"""Right now it is driving at {self.current_speed}km/h. Is it licensed? {'Yes' if self.is_licensed else 'No'}""")

    def paint(self, new_color):
        if new_color in self.colors_available:
            self.color = new_color
            print(f"We painted your car {self.color}")
        else:
            print(f"Your desired color is not available... You can choose from: {self.colors_available}")

    def license(self):
        self.is_licensed = True

    def accelerate(self, new_speed):
        if new_speed < 0:
            raise SpeedError(f"!!Speed error!! {new_speed} < 0!")
        else:
            if new_speed > self.max_speed:
                self.current_speed = self.max_speed
            else:
                self.current_speed = new_speed

        print(f"VRRUUUM, you`re now at {self.current_speed}km/h!!!")

    def brake(self):
        self.current_speed = 0
        print(f"SCRRRRR, you`re breaking, you`re now at {self.current_speed}km/h...")


c1 = Car(model="X", max_speed=250)
c1.describe()
c1.license()
print(f"How about now: is it licensed now?? {c1.is_licensed}")
c1.paint("Red")
c1.accelerate(100)
c1.accelerate(300)
c1.brake()
c1.paint("Yellow")
c1.accelerate(-15)


# 7. Clasa TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor

# Metode:
# adauga_task(nume, descriere) - se va adauga in dict
# finalizeaza_task(nume) - se va sterge din dict
# afiseaza_todo_list() - doar cheile
# afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare
# daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
# Daca acesta raspunde nu - la revedere
# daca raspunde da - il cerem detalii task si salvam nume+detalii in dict

class TodoList:
    def __init__(self):
        self.todo = {}

    def add_task(self, name, description):
        self.todo[name] = description

    def finalize_task(self, name):
        print(f"Task {self.name}: \u2713. Removing it from the list.")
        #         self.todo.pop(name)
        del self.todo[name]

    def show_todo_list(self):
        print(list(self.todo.keys()))

    def show_task_details(self, task_name):
        if task_name not in self.todo:
            to_add = input(f"Task {task_name} is not in the todo list. Do you want to add it? [y/n]: ")
            if to_add.lower().startswith('y'):
                details = input(f"Add a description for the task {task_name}: ")
                self.todo[task_name] = details
            else:
                print("Aright, bye bye!:)")
        else:
            print(f">Task: {task_name}\n>Description: {self.todo[task_name]}")


todo_list = TodoList()
todo_list.show_todo_list()
todo_list.add_task("Cooking Pasta",
                   "This is my amazing pasta recipe that goes like:\n\t 1. boil some water \n\t 2. take a hand full of spaghetti... \n\t 3. break them in half... and somewhere in the world some italian will cry in anger for doing such a sacrilege :D")
todo_list.show_todo_list()
todo_list.show_task_details("Cooking Pasta")
todo_list.show_task_details("Exercise")
todo_list.show_task_details("Exercise")

# 8. C06_EX01 (Homework ex8): Creati un fisier rectangle.py in care sa va definiti o clasa Rectangle, care are 2 atribute width si length,
# instantiate in cadrul constructorului cu 2 valori integer.
# a) Pentru clasa respectiva creati o functie get_area care returneaza aria dreptunghiului.
# b) Creati si o functie display care afiseaza dreptunghiul folosind un parametru optional pentru a desena; in cazul in care
# parametrul nu este dat, se foloseste ca default caracterul *.
# c) Creati un fisier nou test_rectangle.py unde sa va importati clasa Rectangle (din rectangle.py) si testati codul.
# Exemplu de rulare:
# new_rectangle = Rectange(2, 4)
# print(new_rectangle.get_area()) => 8
# new_rectangle.display() => ****     sau: new_rectangle.display('#') => ####
#                            ****                                        ####


# rectangle.py
vvv

# test_rectangle.py
# from rectangle import Rectangle  - aici in jupyter-notebook, nu are sens importul, dar in fisier e nevoie de el

new_rectangle = Rectangle(2, 4)
print(new_rectangle.get_area())
new_rectangle.display()
new_rectangle.display("#")