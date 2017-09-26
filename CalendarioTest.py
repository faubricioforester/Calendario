from Calendario import *

pruebasBisiesto=[2000,2001,2096,2100,2200]

for x in pruebasBisiesto:
    print("Año "+ str(x) + " es Bisiesto? " + str(bisiesto(x)))