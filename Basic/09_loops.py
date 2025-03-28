# loops

# FOR

my_list = [1, 2, 3, 4, 5]

for num in my_list: # recorre la lista
    print(num)

for num in range(10): # de 0 a 9
    print(num)

for num in range(1, 10): # de 1 a 9
    print(num)

for num in range(1, 10, 2): # salta de 2 en 2
    print(num) 

my_tuple = (1, 2, 3, 4, 5)

for num in my_tuple: # recorre la tupla
    print(num)

my_set = {1, 2, 3, 4, 5}

for num in my_set: # recorre el conjunto
    print(num)

my_dict = {"name": "Pedro", "surname": "Perez", "age": 20}

for key in my_dict: # recorre el diccionario
    print(key)
    print(my_dict[key])

for key, value in my_dict.items(): # recorre el diccionario
    print(key)
    print(value)
else:
    print("salimos del bucle")

for element in my_dict.values(): # recorre los valores del diccionario
    if element == "Perez":
        print("El apellido es Perez")
        break # rompe el bucle
    if element == "Pedro":
        continue # salta a la siguiente iteracion sin ejecutar el codigo que continua
    print(element)


# WHILE

my_condition = 0

while my_condition < 10: # mientras la condicion sea verdadera
    print(my_condition)
    my_condition += 1
else: # si la condicion es falsa
    print("my_condition es mayor o igual a 10")


my_condition = 0

while my_condition < 10: # mientras la condicion sea verdadera
    my_condition += 2
    if my_condition == 8:
        print("my_condition es 8")
        break # rompe el bucle
    print(my_condition)

