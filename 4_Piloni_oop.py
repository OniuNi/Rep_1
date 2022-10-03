class Bird:
    def __init__(self):
        self.name = "Birdy"
        print("Bird created")

    def who_am_i(self):
        print("I am a bird")

    def fly(self):
        print("I am flying")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin created")
        self.name = "Penguin"

    def who_am_i(self):
        print("I am a penguin")

    def swim(self):
        print("I am swimming")

pengu = Penguin()
pengu.who_am_i()
pengu.swim()
pengu.fly()

#Polymorphism:abilitatea oop de a permite obiectelor sa ia mai multe forme prin crearea unei interfete comnue

class Romania:
    def language(self):
        print("In Romania the spoken language is Romanian")

class USA:
    def language(self):
        print("In USA the spoken language is English")

def what_do_they_speak(country):
    country.language()

ro = Romania()
us = USA()

what_do_they_speak(ro)
what_do_they_speak(us)

#Abstraction (abstractizare):concept oop prin care se ascunde fata de user functionalitatea interna a unei metode, oferindu-i acestuia doar informatia asupra CE face funtia si nu CUM

from abc import ABC, abstractmethod

class Car(ABC):
    def description(self):
        print("Your object is a car")
    @abstractmethod
    def top_speed(self):
        raise NotImplementedError
    #fie pass

class Dacia(Car):
    def top_speed(self):
        print("The top speed is 240 km/h")

class Tesla(Car):
    def top_speed(self):
        print("The top speed is 250 km/h")

class BMW(Car):
    pass

dacia =  Dacia()
dacia.description()
dacia.top_speed()

tesla = Tesla()
tesla.description()
tesla.top_speed()

bmw = BMW()

#Encapsulation(incapsulare):se ascunde accesul la date din exterior, modificarea lor se face doar dintr-un singur loc, prin intermedoiul unei metode

class Computer():
    def __init__(self):
        self.__price = 1000
    def set_price(self, new_price):
        self.__price = new_price
    def get_price(self):
        print(self.__price)

c1 = Computer()
c1.get_price()
c1.set_price(2000)
c1.get_price()






