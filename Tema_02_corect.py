# Pentru toate exercitiile se va folosi notiunea de if in rezolvare.
# Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if.
# x poate fi initializat direct in cod sau citit de la tastatura, dupa preferinte.
# x este un int.

# 2.Verificati si afisati daca x este numar natural sau nu

# v1
x = 1
if x >= 0:
    print(f'Numarul {x} este natural')
else:
    print(f'Numarul {x} NU este natural')

x = -1
if x >= 0:
    print(f'Numarul {x} este natural')
else:
    print(f'Numarul {x} NU este natural')

# Dar daca apelam cu 3.5, care nu e natural...?
x = 3.5  # numar natural = numar intreg mai mare sau egal cu 0
if x >= 0:
    print(f'Numarul {x} este natural')
else:
    print(f'Numarul {x} NU este natural')

# v2
x = 3.5
if x >= 0 and isinstance(x, int):
    print(f'(v2)Numarul {x} este natural')
else:
    print(f'(v2)Numarul {x} NU este natural')

# 3. Verificati si afisati daca x este numar pozitiv, negativ sau neutru

nr = int(input("Introduceti un numar: "))

if nr > 0:
    print('Nr e pozitiv')
elif nr < 0:
    print('Nr e negativ')
elif nr == 0:
    print('Nr e neutru')
# 4. Verificati si afisati daca x este intre -2 si 13
x = int(input("Introduceti un numar: "))

# v1
if x in range(-2, 13):
    print(True)
else:
    print(False)

# v2
print(x in range(-2, 13))

# v3 (merge si cu flaots)
print(x >= -2 and x <= 13)
# 5. Verificati si afisati daca dif dintre x si y e mai mica decat 5.
x = int(input('Indroduceti x: '))
y = int(input('Indroduceti y: '))

diff = x - y
if diff < 5:
    print("Diferenta e mai mica decat 5")
else:
    print("Diferenta e mai mare decat 5")

# Daca vrem sa verificam ca diferenta fie x > y, fie x < y sa fie mai mica decat 5?
# v1
if x >= y:
    diff = x - y
else:
    diff = y - x

if diff < 5:
    print("Diferenta e mai mica decat 5")
else:
    print("Diferenta e mai mare sau egala cu 5")

# v2 (optima)
if abs(x - y) < 5:
    print("Diferenta e mai mica decat 5")
else:
    print("Diferenta e mai mare sau egala cu 5")
# 6. Verificati daca x NU este intre 5 si 27. (a se folosi ‘not’)
x = int(input("Introduceti un numar: "))

# v1
print(x not in range(5, 27))  # 27 nu e inclus, ca sa il includa trebuie range(5,28)

# v2 (merge si cu flaots)
print(not (x >= 5 and x <= 27))
# 7. x si y (int). Verificati si afisati daca sunt egale, daca nu afisati care din ele este mai mare
x = int(input("x = "))
y = int(input("y = "))

if x == y:
    print(f"x={x} este egal cu y={y}")
elif x > y:
    print(f"x={x} este mai mare decat y={y}")
else:
    print(f"x={x} este mai mic decat y={y}")
# 8. x, y, z - laturile unui triunghi. Afisati daca triunghiul este isoscel, echilateral sau oarecare.
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

if x == y and x == z:
    print('Triunghiul este echilateral')
elif x == y or x == z or y == z:
    print('Triunghiul este isoscel')
else:
    print('Triunghiul este unul oarecare')
# 9. Cititi o litera de la tastatura. Verificati si afisati daca e vocala sau nu.
litera = input('Introduceti o litera: ')
vocale = 'aeiou'  # sau vocale = ('a', 'e', 'i', 'o', 'u')

if litera.lower() in vocale:
    print('Litera e vocala')
else:
    print('Litera NU e vocala')
# 10. Transformati si printati notele din sistem romanesc in  >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

nota = input("Introduceti nota in sistem romanesc: ")
if nota.replace('-', '', 1).replace('.', '', 1).isnumeric():
    nota = round(float(nota))  # am ales sa accept nota ca float si sa rotunjesc, doar o alegere...
    if nota > 10 or nota < 1:
        print("Introduceti o valoare intre 1 si 10..")
    elif nota > 9:  # tot o alegere e sa aleg > si nu >=...
        print("A")
    elif nota > 8:
        print("B")
    elif nota > 7:
        print("C")
    elif nota > 6:
        print("D")
    elif nota > 4:
        print("E")
    else:
        print("F")
else:
    print("Nu ati introdus un numar...")
# 11. Verificati daca x are minim 4 cifre (x e int) (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
x = input('x = ')
x = str(x)  # lucram cu numarul ca string (input returneaza string, dar am facut casting sa fie clar)

# v1
if x[0] == '-':
    x = x[1:]  # renuntam la primul caracter daca e -
if x[0] == '0':
    x = x[1:]  # renuntam la primul caracter daca e 0

if x.isnumeric():  # verificam ca inputul e intr-adevar un int valid
    if len(x) < 4:
        print("Nr NU are minim 4 cifre!")
    else:
        print("Nr are minim 4 cifre!")
else:
    print("Nu ati introdus un numar integer valid!")

# v2 (x poate fi si float):
x = input('(v2: x float) x = ')
x = str(x)  # lucram cu numarul ca string (input returneaza string, dar am facut casting sa fie clar)

if x[0] == '-':
    x = x[1:]  # renuntam la primul caracter daca e -
if x[0] == '0':
    x = x[1:]  # renuntam la primul caracter daca e 0

if x.replace('.', '', 1).isnumeric():  # verificam ca inputul e intr-adevar un numar valid (doar cifre si maxim un .)
    if len(x) < 4 or (len(x) == 4 and '.' in x):
        print("Nr nu are minim 4 cifre!")
    else:
        print("Nr are minim 4 cifre!")
else:
    print("Nu ati introdus un numar valid!")
# 12. Verificati daca x are exact 6 cifre.
x = input('x = ')

# Daca x poate fi si float:
x = str(x)  # lucram cu numarul ca string
if x.replace('-', '', 1).replace('.', '',
                                 1).isnumeric():  # verificam ca inputul e intr-adevar un numar valid (doar cifre si maxim un - si/sau .)
    if x[0] == '0':  # numerele nu incep cu 0
        x = x[1:]
    if (len(x) == 6 and '.' not in x) or (len(x) == 7 and ('.' in x or '-' in x)) or (
            len(x) == 8 and '.' in x and '-' in x):
        print('Nr are exact 6 cifre!')
    else:
        print('Nr nu are exact 6 cifre!')
else:
    print("Nu ati introdus un numar valid!")
# 13. Verificati daca x este numar par sau impar (x e int)
x = int(input("x = "))

if x % 2 == 0:  # sau if not x % 2:
    print(f"x={x} e par")
else:
    print(f"x={x} e impar")
# 14. x, y, z (int). Afisati care este cel mai mare dintre ele?
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

# v1
if (x == y and x > z) or (x == z and x > y) or (y == z and y > x):
    print("Doua numere sunt egale si mai mari decat al 3-lea..")
else:
    if x > y and x > z:
        print(f"x={x} e cel mai mare")
    elif y > x and y > z:
        print(f"y={y} e cel mai mare")
    else:
        print(f"z={z} e cel mai mare")

# v2
print(max(x, y, z))
# 15. x, y, z - reprezinta unghiurile unui triunghi. Verificati si afisati daca triunghiul este valid sau nu.
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

# v1
if x + y > z and y + z > x or z + x > y:  # suma a oricaror doua laturi trebuie sa fie mai mare decat cea de-a 3-a
    print("Triunghi valid")
else:
    print("Triunghi invalid")

# v2 (mai optima deoarece conditia se poate opri la primul fals)
if x + y <= z or y + z <= x or z + x <= y:  # suma a oricaror doua laturi trebuie sa fie mai mare decat cea de-a 3-a
    print("Triunghi invalid")
else:
    print("Triunghi valid")
# 16. Avand stringul: 'Coral is either the stupidest animal or the smartest rock' cititi de la tastatura un int x.
# Sa se afiseze stringul fara ultimele x caractere (ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte')
the_string = 'Coral is either the stupidest animal or the smartest rock'
x = int(input("Alegeti numarul de caractere care sa se elimine din string: "))

print(the_string[:-x])
# 17.Acelasi string; declarati un string nou care sa fie format din primele 5 caractere + ultimele 5
the_string = 'Coral is either the stupidest animal or the smartest rock'
new_string = the_string[:5] + the_string[-5:]

print(new_string)
# 18. Acelasi string.
# Salvati intr-o variabila si afiseaza indexul de start al cuvantului rock.
# (hint: este o functie care va ajuta sa faceti asta).
# Folosind aceasta variabila + slicing, afisati tot stringul pana la acest cuvant
# output: 'Coral is either the stupidest animal or the smartest '
the_string = 'Coral is either the stupidest animal or the smartest rock'
word_to_find = 'rock'

index_of_word = the_string.find(
    word_to_find)  # daca am folosi functia .index si cautam cu un cuvant care nu e in string, primim eroare
if index_of_word >= 0:
    print(the_string[:index_of_word])
else:
    print("Cuvantul cautat nu e in string...")
# 19. Cititi de la tastatura un string. Verificati daca primul si ultimul caracter sunt la fel.
# Se va folosi un assert. Atentie: se doreste ca programul sa fie case insensitive: 'apA' e acceptat.
the_string = input("Introduceti un string: ")
assert the_string[0].lower() == the_string[-1].lower()
# 20. Avand stringul '0123456789'. Afisati doar numerele pare.
# Apoi afisati doar numerele impare (hint: folositi slicing, controlati din pas)
the_string = '0123456789'

print(f"Pare:  {the_string[::2]}")
print(f"Imare: {the_string[1::2]}")
# 21. Verificare imbarcare persoane
# Tineti urmatoarele date
# Varsta
# Insotit de mama
# Insotit de tata
# Pasaport
# Act permisiune mama
# Act permisiune tata

# Conditii de imbarcare
# Daca pers are varsta peste 18 ani si are pasaport
# Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
# Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la celalat parinte

# Aici vreau sa testati codul cu toate variantele posibile
# Sa generati cazuri de test si expected result, apoi sa rulati codul si sa completati actual results
# Ex:
# Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
# Etc...


age = int(input("Introduceti varsta (introduceti un varsta valida): "))
passport = bool(int(input("Persoana are pasaport? (introduceti 1 pt da, 0 pt nu)")))
accompanied_mother = bool(int(input("Persoana e insotita de mama? (introduceti 1 pt da, 0 pt nu): ")))
accompanied_father = bool(int(input("Persoana e insotita de tata? (introduceti 1 pt da, 0 pt nu): ")))
permission_mother = bool(int(input("Persoana are act de permisiune de la mama? (introduceti 1 pt da, 0 pt nu): ")))
permission_father = bool(int(input("Persoana are act de permisiune de la tata? (introduceti 1 pt da, 0 pt nu): ")))

if (age >= 18 and passport) or (age < 18 and passport and accompanied_father and accompanied_mother) or \
        (age < 18 and passport and accompanied_father and permission_mother) or (
        age < 18 and passport and accompanied_mother and permission_father):
    print("Person boarded")
else:
    print("Person cannot board")
# 22. Joc ghicit zarul:
# Cautati pe net si vedeti cum se genereaza un numar random.
# Ne imaginam ca dam cu zarul si salvam acest numar in dice_roll.
# Luati un nr ghicit de la utilizator.
# Verificati si afisati daca utilizatorul a ghicit.
# 3 optiuni:
#   Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
#   Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
#   Felicitari! Ai ghicit. Ai ales x si zarul a fost y.
import random

dice_roll = random.randint(1, 6)
number_guessed = input('Alegeti un numar intre 1 si 6: ')

if number_guessed not in '123456':
    print('Nu ati ales un numar intre 1 is 6!')
else:
    number_guessed = int(number_guessed)
    if dice_roll > number_guessed:
        print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {number_guessed}, dar a fost {dice_roll}')
    elif dice_roll < number_guessed:
        print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {number_guessed}, dar a fost {dice_roll}')
    else:
        print(f'Felicitări! Ai ghicit. Ai ales {number_guessed} si zarul a fost {dice_roll}')
