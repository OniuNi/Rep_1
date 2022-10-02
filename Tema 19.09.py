#1 Functie care sa calculeze si sa returneze suma a doua numere

def sum_2(a,b):
    sum = a + b
    print(sum)
    return
sum_2(78, 65)
sum_2(56568, 695992)

#2 Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

num = int(input(f'Introduceti numarul : '))

def even_odd(num):
    if num % 2 == 0:
        print('True')
    else:
        print('False')
even_odd(num)

#3. Functie care returneaza numarul total de caractere din numele tau complet.(nume, prenume, nume_mijlociu)

nume = str(input(f'Introduceti numele complet : '))
def caractere(nume):
    print(len(nume))
    return
caractere(nume)

#4 Functie care returneaza aria dreptunghiului

def aria_dreptunghi(x, y):
    aria = x * y
    print(f'Aria dreptunghiului este : %.2f'  % aria)
aria_dreptunghi(7,5)


#5 Functie care returneaza aria cercului

def aria_cerc(r):
    PI = 3.14
    return PI * (r * r)
raza = float(input(f'Introduceti raza:'))
print(f'Aria cercului este : %.6f' % aria_cerc(raza))

#6 Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu

def bool_caracter(a, sir):
    if a in sir:
        return True
    else:
        return False
print(bool_caracter('l', "lakajjdlfjfushs"))

#7 Functie fara return, primeste un string si printeaza pe ecran:
#Nr de caractere lower case este x
#Nr de caractere upper case exte y





#8 Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive

def numere_pozitive(listanr):
    pozitive = []
    for i in listanr:
        if i >=0:
            pozitive.append(i)
    return pozitive
listanr = [-1, 22, -3, 14, -5, -6, 27, 0, -2]
print(numere_pozitive(listanr))


#9 Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
#Primul numar x este mai mare decat al doilea nr y
#Al doilea nr y este mai mare decat primul nr x
#Numerele sunt egale.


def verificare_numere(a, b):
    if a > b:
        print (f'Primul numar {a} este mai mare decat {b}')
    elif b > a:
        print (f'Al doilea numar {b} este mai mare decat {a}')
    else:
        print (f'Numerele sunt egale')
verificare_numere(5,5)
verificare_numere(5,8)

#10Functie care primeste un numar si un set de numere.
#Printeaza ‘am adaugat numarul nou in set’ + returneaza True
#Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False

#11  Functie care primeste o luna din an si returneaza cate zile are acea luna

from calendar import monthrange

def zile_luna(an=2018, luna=11):
    return monthrange(an, luna)[1]

print(zile_luna(2018,11))

#la ex 16 trebuia folosit excewpt/try
def numar_ales():
    try:
        num = float(input("Enter a number :"))
    except ValueError:
        print('Nu ati ales un numar valid')
    else:
        if num> 0:
            print("Pozitive number")
        elif num == 0:
            print("Zero")
        else:
            print("Negative number")
    finally:
        print("Sfarsitul functiei")


# 18 functie ce aplica reducerea de pret,#parmetru auxiliar


