#1. Clasa Cerc
#Atribute: raza, culoare
#Constructor pt ambele atribute
#Metode:
#descrie_cerc() - va PRINTA culoarea si raza
#aria() - va RETURNA aria
#diametru()
#circumferinta()

class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare
    def descrie_cerc (self):
        print(f'{self.culoare} , {self.raza}')
    def aria_cerc(self):
        return aria
    def diametru_cerc(self):
        print("a")
    def circumferinta_cerc(self):
        print("b")
#4.Clasa Cont
#Atribute: iban, titular_cont, sold
#Constructor pentru toate
#Metode:
#afisare_sold() - Titularul x are in contul y suma de n lei
#debitare_cont(suma)
#creditare_cont(suma)

class Cont:
    def __int__(self, titular_cont, iban, sold):
        self.titular_cont = titular_cont
        self.iban = iban
        self.sold = 100

    def afisare_sold(self, sold):
        print(f'Titularul {self.titular_cont}')
        print(f'iban {self.iban}')
        print(f'sold {self.sold}')

    def debitare_cont(self, suma):
        self.sold += suma
        print(f'Contul dvs a fost debitat cu {suma}')
        print(f'Aveti in cont {self.sold}')

    def creditare_cont(self, suma):
        if suma <= self.sold:
            self.sold -=suma
            print(f'Soldul dvs a fost cu creditat cu {suma}')
            print(f'Noul dvs sold este{self.sold}')
        else:
            print(f'Fonduri insuficiente')


