# problema:masina merge cat timp inca are benzina

litri_benzina = 10
while litri_benzina < 10 :
#acceleram
    print('Vruum Vruum')
#scadem benzina
    litri_benzina = litri_benzina - 1
    if litri_benzina <= 3 :
        print("beculetul rosu")
print("Stop")

import random
dice_roll = 0
while dice_roll != 3 and dice_roll !=6:
    dice_roll = random.randint(1, 6)
    print(f'Dice rolled: {dice_roll}')



for tura in range(5):
    print(f'Am mai alergat o tura:{tura}')


country ={'name': 'Romania', 'population': '19.Smil', 'continent':'Europe'}
print(country['name'])

for key in country:
    print(country[key])

for key, val in country.items():
    print(f"key={key}, value={val}")



#exercitiu

#Print all even natural numbers lower than a keyboard imputed one e.g. in=9 0 2 4 6 8

nr = int(input('Alege un numar: '))
for nr in range (0, nr):
    if ( nr % 2 == 0 ):
        print(nr)


#ex 2 given a number n=15, write a loop that prints the number and decreases it
#until it hits 0 by
# - 2 in case the numaber is divisible by 5
# - 3 if it is even
# - 1 if it is odd

    n =15
    while n > 0:
        print(n)
        if (n % 5 == 0):
            n -= 2
        elif (n % 2 == 0):
            n -= 3
        else:
            n -= 1
