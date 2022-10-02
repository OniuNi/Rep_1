#Exercitiul 1.
#Avand lista
#masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

#Folositi un for ca sa iterati prin toata lista si sa afisati
#‘Masina mea preferata este x’
#Faceti acelasi lucru cu un for each
#Faceti acelasi lucru cu un while

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for x in masini:
    print(f'Masina mea preferata este: {x}')
#for each
for masina in masini:
    print(f'Masina mea preferata este: {masina}')


#3
#Aceeasi lista,
#Vine un cumparator care doreste sa cumpere un Mercedes
#Iterati prin ea prin for each
#Daca masina e mercedes (if)
# #Printam ‘am gasit masina dorita de dvs’
#Iesim din ciclu folosind un cuvant cheie care face acest lucru
#Altfel:
#Printam Am gasit masina X. Mai cautam

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Mercedes':
        print("Am gasit masina dorita de dvs!")
        break
    else:
        print(f"Am gasit masina {masina}. Mai cautam...")

# 4.Aceasi lista
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# Printati S-ar putea sa va placa masina x


for masina in masini:
    if masina == 'Lastun' or masina == 'Trabant':
        continue
    print(f'S-ar putea sa va placa masina {masina}')



#5Modernizati parcul de masini
#Creati o lista goala, masini_vechi
#Iterati prin masini
#Cand gasiti Lastun sau Trabant:
#Salvati aceste masini in masini_vechi
#Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
#Printati Modele vechi: x
#Modele noi: x

masini_vechi = []


#6Avand dict

pret_masini = {'Dacia': 6800, 'Lastun': 500, 'Opel': 1100, 'Audi': 19000, 'BMW': 23000}

#Vine un client cu un buget de 15000 euro
#Prezentati doar masinile care se incadreaza in acest buget
#Iterati prin dict.items() si accesati masina si pretul
#Printati Pentru un buget de sub 15000 euro puteti alege masina x
#Iterati prin lista

#7Avand lista
#numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#Iterati prin ea
#Afisati de cate ori apare 3
#(nu aveti voie sa folositi count)

#8Aceeasi lista
#Iterati prin ea
#Calculati si afisati suma numerelor
#(nu aveti voie sa folositi sum)

#9. Aceeasi lista
#Iterati prin ea
#Afisati cel mai mare numar
#(nu aveti voie sa folositi max)


#10.Aceeasi lista
#Iterati prin ea
#Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
#Ex: daca e 3, sa devina -3
#Afisati noua lista


#c. Optionale (may need google)

#11.alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
#numere_pare = []
#numere_impare = []
#numere_pozitive = []
#numere_negative = []
#Iterati prin lista alte_numere
#Populati corect celelalte liste
#Afisati cele 4 liste la final

#12.Aceeasi lista
#Ordonati crescator lista fara sa folositi sort
#Va puteti inspira vizual de aici
#https://www.youtube.com/watch?v=lyZQPjUT5B4


#13.Ghicitoare de numar
#numar_secret = Generati un numar random intre 1 si 30
#3Numar_ghicit = None
#Folosind un while
#User alege un numar
#Programul ii spune:
#Nr secret e mai mare
#Nr secret e mai mic
#Felicitari! Ai ghicit!

#14. Alegeti un numar de la tastatura
#Ex:7
#Scrieti un program care sa genereze in consola urmatoarea piramida
#1
#22
#333
#4444
#55555
#666666
#7777777

#Ex:3
#1
#22
#333

x = int(input("Introduceti un numar pentru a genera piramida: "))
for i in range(1,x+1):
    print(i*str(i))

#15.tastatura_telefon = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[0]]
#Iterati prin lista 2d
#Printati ‘Cifra curenta este x’
#(hint: nested for - adica for in for)
