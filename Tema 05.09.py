#declarare lista

note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(note_muzicale)

#inversasare si suprascriere

print(len(note_muzicale))
note_muzicale=(note_muzicale[::-1])
print(note_muzicale)

#aplicarea metodei

note_muzicale.reverse()
print(note_muzicale)

#2 de cate ori apare "do"

print(note_muzicale.count("do"))

#3 unirea a doua liste

#varianta1
lsta = [3, 1, 0, 2]
lstb = [6, 5, 4]
lsta.extend((lstb))
print(lsta)

#varianta2
lsta = [3, 1, 0, 2]
lstb = [6, 5, 4]
lsta =lsta + lstb
print(lsta)

# 4 Sortati si afisati lista generata la ex anterior
# Stergeti numarul 0 folosind o functie

lsta = [3, 1, 0, 2, 6, 5, 4 ]

lsta.sort()
print(lsta)

lsta = [0, 1, 2, 3, 4, 5, 6]
lsta.remove(0)
print(lsta)

# 5 Folosind un if verificati lista generata la ex3 si afisati
# Lista este goala
# Lista nu este goala

lsta = [3, 1, 0, 2, 6, 5, 4]
if len(lsta)==0:
    print('Lista: lsta este goala')
else:
    print('Lista: lsta nu este goala')

# 6 Folositi o functie care sa goleasca lista de la ex3

lsta = [3, 1, 0, 2, 6, 5, 4]
print(len(lsta))
lsta.clear()
print(lsta)
#metoda clear() goleste o lista, sterge toate elementele

# 7Copy paste la ex 5. Verificati inca o data.
# Acum ar trebui sa se afiseze ca lista e goala

lsta = []
if len(lsta)==0:
    print('Lista: lsta este goala')
else:
    print('Lista: lsta nu este goala')

# 8   Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folositi o functie ca sa afisati Elevii (cheile)

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

#9 Printati cei 3 elevi si notele lor
#Ex: ‘Ana a luat nota {x}’
#Doar nota o veti lua folosindu-va de cheie

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.get('Gigel'))#doar am extras nota lui Gigel


#10 Dorel a facut contestatie si a primit 6
#Modificati nota lui Dorel in 6
#Printati nota dupa modificare

dict1['Dorel'] = 6
print(dict1)

#11
#Gigel se transfera din clasa
#Cautati o functie care sa il stearga
#Vine un coleg nou. Adaugati Ionica, cu nota 9
#Printati noii elevi

del dict1['Gigel']
dict1 ['Ionica'] = 9
print(dict1)

#12Set
#zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
#weekend = {'sambata', 'duminica'}
#Adaugati in zilele_sapt ‘luni’
#Afisati zile_sapt. Ce observati?

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)#se afiseaza o sngra data valoarea 'luni' pentru ca setul nu contine duplicate

#13Folositi un if si verificati daca
#Weekend este un subset al zilelor din sapt
#Weekend nu este un subset al zilelor din sapt

if weekend.issubset(zile_sapt):#se foloseste metoda issubset()
    print('Weekend este un subset al zilelor din sapt')
else:
    print('Weekend nu este un subset al zilelor din sapt')

#14.
#Afisati diferentele dintre aceste 2 seturi
print('Diference:')
print(zile_sapt - weekend)

#15Afisati intersectia elementelor din aceste 2 seturi
print('Intersection:')
print(zile_sapt & weekend)

#16
#Ne imaginam o echipa de fotbal pt teren sintetic.
#3 Schimbari maxime admise

#Declara o Lista cu 5 jucatori
#Schimbari_efectuate = va jucati voi cu valori diferite
#Schimbari_max = 3

#Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
#Efectuam schimbarea
#Stergem jucatorul scos din lista
#Adaugam jucatorul intrat
#Afisam a intra x, a iesit y, mai aveti z schimbari
#Daca jucatorul nu e in teren:
#Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
#Afisati ‘mai aveti z schimbari’

#Testati codul cu diferite valori

echipa = ['a', 'b', 'c', 'd', 'e']


# TODO_1: Avand dictionarul:
my_d = {'a': {'aa': 11, 'ab': 12}, 'c': {'ca': 31}}
# 1. Cum putem returna valoarea cheii 'ab' din interiorul cheii 'a', iar daca nu exista sa afisam 'Cheia nu exista!'?
# 2. Cum putem returna valoarea cheii 'b', iar daca nu exista sa afisam 'Cheia nu exista!'?
# 3. Cum putem returna valoarea cheii 'cb' din interiorul cheii 'c', iar daca nu exista sa afisam 'Cheia nu exista!'?
# 4. Cum putem returna valoarea cheii 'ba' din interiorul cheii 'b', iar daca nu exista sa afisam 'Cheia nu exista!'?


# TODO_2: Avand lista l=[1,1,2,3,1,4,4,5,6,2], cum facem sa
# eliminam duplicatele?

l=[1,1,2,3,1,4,4,5,6,2]
l =list(set (l))
print(l)

# TODO_3: Given the set: animals1 = {"wolf", "cheetah", "elephant", "crocodile"}:
# 1. Add the following list of animals to it: lst1 = ["horse", "chimpanzee"]
# 2. print only elements from set animals1 that are not found in set

#lista nu poate fi adaugata la un set (lista este indexata, mutabila si ordonata,
# iar setul setul este neindexat,, imutabil,neordonat)

animals1 = {"wolf", "cheetah", "elephant", "crocodile"}
lst1 = ["horse", "chimpanzee"]
animals2 = {"jaguar", "horse", "wolf", "crocodile"}

print('Diference:')
print(animals1-animals2)