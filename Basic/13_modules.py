# modules

# la nomenclatura de los modulos es en minusculas, los ficheros creados como 00_nombre no los reconoce como tal

import module
print(module.sum_value(1, 2))

module.print_values(1, 2, 3)

from module import print_array, print_dict
print_array([1, 2, 3])
print_dict({'a': 1, 'b': 2, 'c': 3})


import math
print(math.pi)

import math as mt
print(mt.pi)

from math import pi
print(pi)

import random
print(random.randint(1, 10))