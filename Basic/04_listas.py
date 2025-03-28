# Listas

my_list = list()
my_list = [1, 2, 3]
print(my_list)

my_list = ["hola", 2, 3.5, True]
print(my_list)

print(len(my_list))

print(my_list[0])
print(my_list[-1]) # muestra el primero por el final
print(my_list[0:2])

text, num, fl, b = my_list
print(text, num, fl, b)

print(my_list.count("hola")) # cuenta cuantas veces aparece el elemento
print(my_list.index("hola")) # devuelve la posicion del elemento

my_list.append("Python") # agrega un elemento al final
print(my_list)

my_list.insert(1, "Python") # agrega un elemento en la posicion indicada
print(my_list)

my_list.remove("Python") # elimina el elemento indicado 1 vez en la lista
print(my_list)

my_list.pop() # elimina el ultimo elemento de la lista y lo devuelve
print(my_list)

my_list.clear() # elimina todos los elementos
print(my_list)

my_list = ["hola", 2, 3.5, True]

del my_list # elimina la lista
# print(my_list) da error, ya que la lista no existe

my_list = ["hola", 2, 3.5, True]

my_list2 = my_list.copy() # copia la lista
print(my_list2)

del my_list2[0] # elimina el primer elemento de la nueva lista 
print(my_list2)

print(len(my_list2)) # muestra la longitud de la lista

print(my_list + my_list2) # concatena las listas

my_int_list = [1, 2, 3]
my_int_list.reverse() # invierte la lista
print(my_int_list)

my_int_list.sort() # ordena la lista
print(my_int_list)