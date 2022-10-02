#1 Functie care sa calculeze si sa returneze suma a doua numere

def sum_2(a,b):
    print(a+b)
sum_2(78,65)

#2 Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

num = int(input(f'Introduceti numarul : '))

def even_odd(num):
    if num % 2 == 0:
        print('True')
    else:
        print('False')
even_odd(num)

#3. Functie care returneaza numarul total de caractere din numele tau complet.(nume, prenume, nume_mijlociu)

#def len(a):
    #a = str(input(f'Introduceti numele complet : '))
    #print(len(a))
#len(a)

def caractere(nume):
  return len(nume) - nume.count(' ')
nume_dat = caractere('Anghelet Cristina Filofteia')
print(nume_dat)

nume_dat = caractere('Anghelet Cristina')
print(nume_dat)



#4Functie care returneaza aria dreptunghiului

def aria_dreptunghi(x, y):
    return x*y


#5Functie care returneaza aria cercului



