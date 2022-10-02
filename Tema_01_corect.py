# 2. Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri:
# string, int, float, bool
# Valorile le alegeti voi dupa preferinte

name = 'Sara'
age = 10
weight = 22.5
is_good_girl = True

# 3.Utilizat functia type pentru a verifica daca au tipul de date asteptat
print(type(name))
print(type(age))
print(type(weight))
print(type(is_good_girl))

# 4. Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
# Verificati tipul acesteia

weight = round(weight)
print(type(weight))

# 5. folositi print() si printati in consola 4 propozitii folosind cele 4 variabile.
# (rezolvati nepotrivirile de tip prin ce modalitate doriti)

print(f"My dog`s name is {name}")
print(f"It is {age} years old")
print(f"It weights {weight} kg")
print(f"Is she a good girl?? {is_good_girl}")

# 6. citeste de la tastatura numele
# citeste de la tastatura prenumele
# afiseaza 'Numele complet are x caractere'
last_name = input("Introduceti numele: ")
first_name = input("Introduceti prenumele: ")

print(f"Numele complet are {len(last_name+first_name)} caractere")

# 7. citeste de la tastatura lungimea
# citeste de la tastatura latimea
# afiseaza 'Aria dreptunghiului este x'

length = input("Introduceti lungimea dreptunghiului: ")
width = input("Introduceti latime dreptunghiului: ")

print(f"Aria dreptunghiului este: {int(length)*int(width)}")

# 8. Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
# afisati de cate ori apare cuvantul 'the'

the_string = 'Coral is either the stupidest animal or the smartest rock'
print(the_string.count("the"))

# 9.acelasi string
# inlocuieste the cu THE peste tot
# printeaza rezultatul
the_string = 'Coral is either the stupidest animal or the smartest rock'

the_string = the_string.replace('the', "THE")
print(the_string)

# 10. citeste de la tastatura un string de dimensiune impara
# afiseaza caracterul din mijloc
the_string = input("Introduceti un string de dimensiune impara: ")

middle_index = len(the_string) // 2
print(f'Caracterul din mijloc este {the_string[middle_index]}')

# 11.folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')
# si salveaza fiecare cuvant intr-o variabila
# acum printeaza ambele variabile pentru verificare
the_string = input("Introduceti un string format din 2 cuvinte: ")

# v1
space_index = the_string.find(' ')
s1 = the_string[:space_index]
s2 = the_string[space_index+1:]
print(s1,s2)


# v2
s1, s2 = the_string.split()
print(s1, s2)

# 12. citeste un string de la tastatura (eg: alabala portocala)
# salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite)
# capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
# => alAbAlA portocAla
the_string = input("Introduceti un string: ")

first_character = the_string[0]
the_string = the_string[0] + the_string[1:-1].replace(first_character, first_character.upper()) + the_string[-1]
print(the_string)

# 13. citeste un user de la tastatura
# citeste o parola
# afiseaza: 'Parola pt user x este ***** si are x caractere'
# ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
# eg: parola abc => ***
# parola abcd => ****
user = input("Introduceti user-ul: ")
password = input("Introduceti parola: ")

print(f"Parola pt user {user} este {len(password) * '*'} si are {len(password)} caractere")

# 14. TODO_1 de la curs (C01EX01)
# Cum facem sa afisam valoare lui pi cu doar 2 zecimale? presupunem pi = 3.146712
pi = 3.146712

print(round(pi,2))
print(str(pi)[:4])
print(f"{pi:.2f}")

# 15. TODO_2 de la curs (C01EX02)
# Avand my_string = "Hello Pythonistas" , vrem sa afisam stringul: "eoyoss"
my_string = "Hello Pythonistas"

print(my_string[1::3])
