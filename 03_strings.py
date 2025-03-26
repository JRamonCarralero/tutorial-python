# Strings

my_string = "hola mundo"
print(my_string)

my_string = 'hola mundo'
print(my_string)

my_string = """hola mundo"""
print(my_string)

print(len(my_string))

print("hola" + " " + "mundo")
print("hola" * 3)
print("hola" in "hola mundo")
print("hola" not in "hola mundo")

# Escapes
print("string con\nsalto de linea")
print("\tstring con tabulacion")
print("\\string con barra invertida")

# Formateo
name, surname, age = "Pedro", "Perez", 20
print(f"Me llamo {name} {surname} y mi edad es {age}")
print("Me llamo %s %s y mi edad es %d" % (name, surname, age))

# Unpacking
a, b, c = "abc"
print(a)
print(b)
print(c)

# Slice de strings
language = "Python"
print(language[0])
print(language[-1])
print(language[0:3])
print(language[:3])
print(language[3:])
print(language[:])
print(language[::-1]) # reverse
print(language[::2]) # salto de 2

# Funciones
print(language.upper())
print(language.lower())
print(language.title())
print(language.swapcase())
print(language.capitalize())
print(language.replace("Py", "JS"))
print(language.count("t"))
print(language.split("t"))
print(language.find("t"))
print(language.find("t", 1))
print(language.isnumeric())
print(language.startswith("Py"))