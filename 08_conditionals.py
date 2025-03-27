# conditionals

a = int(input("Introduce un numero: "))
b = int(input("Introduce otro numero: "))

if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else:
    print("a es igual que b")

c = int(input("Introduce un numero: "))
d = int(input("Introduce otro numero: "))

if c > d and a > b:
    print("c es mayor que d y a es mayor que b")
elif c < d and a < b:
    print("c es menor que d y a es menor que b")
elif c > d and a < b:
    print("c es mayor que d y a es menor que b")
elif c < d and a > b:
    print("c es menor que d y a es mayor que b")
elif c > d and a == b:
    print("c es mayor que d y a es igual que b")
elif c < d and a == b:
    print("c es menor que d y a es igual que b")
elif c == d and a > b:
    print("c es igual que d y a es mayor que b")
elif c == d and a < b:
    print("c es igual que d y a es menor que b")
else:
    print("c es igual que d y a es igual que b")


my_string = ""

if my_string:
    print("my_string tiene contenido")
else:
    print("my_string esta vacio")

my_string = "hola"

if my_string:
    print("my_string tiene contenido")
else:    
    print("my_string esta vacio")

if my_string == "hola":
    print("my_string es hola")
else:    
    print("my_string no es hola")

if my_string != "hola":
    print("my_string no es hola")
else:    
    print("my_string es hola")

if my_string and my_string == "hola":
    print("my_string existe y es hola")
else:    
    print("my_string no es hola")