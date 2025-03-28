# functions

def my_function():
    print("Hello from a function")

my_function()

def my_function(name):
    print("Hello from a function", name)

my_function("Pedro")

def my_function(name, surname):
    print("Hello from a function", name, surname)

my_function("Pedro", "Perez")

def my_function(name, surname, age):
    resp = {
        "name": name,
        "surname": surname,
        "age": age
    }
    return resp

person = my_function("Pedro", "Perez", 20)
print(person)

def sum(num1, num2):
    return num1 + num2

print(sum(1, 2))

def printName(name, surname, alias="Sin alias"):
    print(name, surname, alias)

printName("Pedro", "Perez")

def printTexts(*text):
    print(text)

printTexts("Hello", "World")