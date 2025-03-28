# tuplas

# tuplas son inmutables

my_tuple = tuple()
my_tuple = (1, 2, 3)
print(my_tuple)

my_tuple = ("hola", 2, 3.5, True)
print(my_tuple)

print(len(my_tuple))

print(my_tuple[0])
print(my_tuple[-1]) # muestra el primero por el final
print(my_tuple[0:2])

text, num, fl, b = my_tuple
print(text, num, fl, b)

my_tuple.count("hola") # cuenta cuantas veces aparece el elemento
my_tuple.index("hola") # devuelve la posicion del elemento

# my_tuple[1] = 3 no se permite cambiar, son valores inmutables
# my_tuple.append("Python") no se permite

my_copy_tuple = my_tuple
print(my_copy_tuple + my_tuple)

del my_copy_tuple
# print(my_copy_tuple) no se puede, no existe

# Una forma de poder modificar una tupla es convertirla en una lista
my_tuple = list(my_tuple) # convierte la tupla en una lista
my_tuple.insert(1, "Python")
my_tuple = tuple(my_tuple) # convierte la lista en una tupla
print(my_tuple)
print(type(my_tuple))