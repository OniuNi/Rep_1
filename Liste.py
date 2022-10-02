my_list = [1, "doi", 100, True, 8.1, 3, 5,  [100, 200, 300], (5, 6, 9), {5, 99, 5}]
print (my_list)
print (my_list[1])
my_list[0]=100
print(my_list)
my_list.append(None)
print(my_list)

s='abc'
s+='d'
print(s)

my_list.insert(5, 'avion')
print(my_list)
my_list.remove(8.1)
print(my_list)
del my_list[-1]
print(my_list)
my_list.copy()