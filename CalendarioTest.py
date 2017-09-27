from Calendario import *

pruebasBisiesto = [2000, 2001, 2096, 2100, 2200]


def print_fecha(fecha):
    return str(fecha[2]) + "/" + str(fecha[1]) + "/" + str(fecha[0])


for x in pruebasBisiesto:
    print("Año " + str(x) + " es Bisiesto? " + str(bisiesto(x)))

pruebasEsFechaValida = [(2010, 3, 15), (1582, 3, 15), (1581, 3, 15), (2010, 13, 15), (2004, 2, 29), (2005, 2, 29)]

for y in pruebasEsFechaValida:
    print("La fecha: " + print_fecha(y) + " es valida? " + str(fecha_es_valida(y)))

print("-------------")
pruebasDiaSiguiente = [(2010, 3, 15), (1582, 3, 15), (1581, 3, 15), (2010, 13, 15), (2004, 2, 29), (2005, 2, 29)]

for y in pruebasDiaSiguiente:
    if fecha_es_valida(y):
        print("El dia siguiente a " + print_fecha(y) + " es: " + print_fecha(dia_siguiente(y)))
    else:
        print("Fecha no valida")

pruebasDesdePEnero = []

for i in pruebasDesdePEnero:
    print("El número de dias que han pasado desde " + print_fecha(i) + "es" + print_fecha(dias_desde_primero_enero(i)))
