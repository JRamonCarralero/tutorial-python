# exceptions

try:
    print("Hace lo correcto")
except:
    print("Ocurrio un error")
else:
    print("Todo salio bien")
finally:
    # se ejecuta siempre
    print("Se ejecuto el finally")

try:
    print(10/0)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except:
    print("Ocurrio un error")

number_one = 10
number_two = 3
number_two = "3"

try:
    print(number_one + number_two)
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la información de la excepción
try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)
    print(type(my_random_error_name))