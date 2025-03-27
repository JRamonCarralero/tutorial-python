# sets

# conjunto de datos no ordenados que no permiten elementos duplicados

my_set = set()
my_set = {1, 2, 3}
print(my_set)

my_set.add(4)
print(my_set)

my_set.remove(4)
print(my_set)

print(1 in my_set)
print(4 in my_set)

my_other_set = {}
print(type(my_other_set)) # originalmente lo identifica como diccionario
my_other_set = {1, 2, 3}
print(type(my_other_set)) # ahora ya es un set

my_set.add("hola")
print(my_set)

my_set.add("hola")
print(my_set) # no se puede agregar dos veces el mismo elemento

my_set.add("bola")
print(my_set) # no es una estructura ordenada

my_other_set.clear()
print(len(my_other_set))

del my_other_set # elimina la variable

my_other_set = {"hola", "mundo"}
my_list = list(my_other_set)
print(my_list) # esto es arriesgado por no conocer el orden de la lista

my_set_union = my_set | my_other_set # Esto es igual a my_set.union(my_other_set)
print(my_set_union) # unir dos conjuntos

my_set_intersection = my_set & my_other_set # Esto es igual a my_set.intersection(my_other_set)
print(my_set_intersection) # intersección de dos conjuntos (elementos comunes de 1 y 2)

my_set_difference = my_set - my_other_set # Esto es igual a my_set.difference(my_other_set)
print(my_set_difference) # diferencia de dos conjuntos (elementos de 1 que no están en 2)

my_set_symmetric_difference = my_set ^ my_other_set # Esto es igual a my_set.symmetric_difference(my_other_set)
print(my_set_symmetric_difference) # diferencia simétrica de dos conjuntos (elementos distintos de 1 y 2)