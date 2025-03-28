# dicts

# Un diccionario es una estructura de datos que permite almacenar valores asociados a claves.

my_dict = {}
my_dict = {"name": "Pedro", "surname": "Perez", "age": 20}
print(my_dict)
print(type(my_dict))

my_dict["name"] = "Juan"
print(my_dict["name"])
print(my_dict)

print("name" in my_dict)
print("name" not in my_dict)

print(len(my_dict))

my_other_dict = dict(name="Pedro", surname="Perez", age=20)
print(my_other_dict)
my_dict = {"name": "Pedro", "surname": "Perez", "age": 20, 1: "hola", "languages": {"HTML", "CSS", "JS"}}
print(my_dict)

my_dict["nationality"] = "Spanish"
print(my_dict)

del my_dict["nationality"]
print(my_dict)

my_dict["languages"].add("Python")
print(my_dict)

my_other_dict.clear()
print(my_other_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys([1, 2, 3], "hola")) # crea un diccionario con las claves indicadas y el valor indicado
print(my_dict)

my_list = [1, 2, 3]
my_new_dict = dict.fromkeys(my_list, "hola") # crea un diccionario con las claves que son los valores de la lista y el valor indicado
print(my_new_dict)