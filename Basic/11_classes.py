# classes

class EmptyPerson:
    pass

empty_person = EmptyPerson()
print(empty_person)

class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.name = name
        self.surname = surname
        self.alias = alias
        self.__fullname = f"{self.name} {self.surname}" # privado

    def walk(self):
        print(f"{self.name} {self.surname} is walking")

    def upperAlias(self):
        return self.alias.upper()
    
    def getFullName(self):
        return self.__fullname
    
    def __setFullName(self, fullname): # privado
        self.__fullname = fullname

    def updateFullName(self, fullname):
        self.__setFullName(fullname) # Al ser privado se accede con self

my_person = Person("Pedro", "Perez")
print(my_person.name)
print(my_person.surname)
print(f"{my_person.name} {my_person.surname} y mi alias es {my_person.alias}")

my_person.walk()

my_person = Person("Pedro", "Perez", "jperez")
print(f"{my_person.name} {my_person.surname} y mi alias es {my_person.alias}")

my_person.alias = "the_jperez"
print(f"{my_person.name} {my_person.surname} y mi alias es {my_person.alias}")

print("upper alias:", my_person.upperAlias())

# print("fullname:", my_person.__fullname) No funciona porque es privado
print("fullname:", my_person.getFullName())

# my_person.__setFullName("Pedro Perez") No funciona porque es privado
my_person.updateFullName("Pedro Updated")
print("fullname:", my_person.getFullName())