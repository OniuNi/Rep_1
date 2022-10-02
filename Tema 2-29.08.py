#1 b
#voi initiliza variabila

#functia if else-verifica o succesiune de date daca indeplinesc un criteriu; daca nu se indeplineste,se va excuta partea a doua din functie, else

# 2 Verifica si afiseaza daca x este numar natural sau nu
import importlib
import math

x = 3
if x>= 0:
      print(f'x este un numar natural')
elif x<0:
     print(f' x nu este un numar natural')

# 3 Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

a= 13.5

if x>0:
    print(f'a este numar pozitiv')
elif x<0:
    print(f'a este un numar negativ')
else:
    print(f'a este un numar neutru')

# 4 Verifica si afiseaza daca x este intre -2 si 13; de invatat functia range (nu este corect, range retuyrneaza doar int)|
#varianata corecta se compara x cu cele doua numere margine, prin conditia and

b =float (input("de verificat numarul:"))
if x in range(-2,13):
    print("True")
else:
    print("False")


# 5 Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
# se putea folosi functia abs

x = float(input("Introdu primul numar:"))
y = float(input("Introdu al doilea numar:"))


if (x-y) >5:
    print (f'diferenta dintre x si y este mai mare decat 5')
elif (x-y)==5:
    print (f'diferenta dintre x si y este egala cu 5')
else:
    print(f'diferenta intre x si y este mai mica decat 5')


# 6 Verifica daca x NU este intre 5 si 27 ( a se folosi not)

x = float(input("se introduce x:"))
if x not in range (5, 27):
    print(True)
else:
    print(False)


# 7, x si y (int) - verifica si afiseaza daca sunt egale, daca nu, afiseaza care din ele este mai mare

x =int(input("introduceti x:"))
y =int(input("introduceti y:"))

if (x-y)==0:
    print("cele doua numere sunt egale")
elif(x-y)<0:
    print("numarul y este mai mare")
else:
    print("numarul x este mai mare")

# 8 x, y, z, laturile unui triunghi.Afiseaza daca triunghiul este isoscel, echilateral sau oarecere
#de reluat conditiile, pentru ca daca cle 3 nu pot fi laturile unui triunghi, atunci nu ar trebui sa execute conditiile

x =float(input("latura x:"))
y =float(input("latura y:"))
z =float(input("latura z:"))
# in prima faza am verificat daca cele 3 numere pot fi laturile unui triunghi
if x<y+z and y<x+z and z<x+y:
    print ("x, y, z, sunt laturile unui triunghi")
else:
    print("x, y, z, nu sunt laturile unui triunghi")
if x == y == z:
    print("trinunghiul este echilateral")
elif x == y or y == z or z == x:
    print("triunghiul este isoscel")
else:
    print("triunghiul este oarecare")

# 9-Citeste o litera de la tastatura
# Verifica si afiseaza daca este vocala sau nu
#if litera.lower()

x =input("Introdu o litera de la tastatura:")

if x in ( 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' ):
    print("x este o vocala")
else:
    print("x este o consoana")

# 13 se verifica daca un numar este par sau impar

x = int(input("Se introduce un numar:"))

r=x%2

if r==0:
    print("x este numar par")
else:
    print("x este numar impar")

# 10Transforma si printeaza notele din sistem romanesc in  >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

import math


