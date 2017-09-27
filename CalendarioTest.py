from Calendario import *

pruebasBisiesto = [2000, 2001, 2096, 2100, 2200]


def print_fecha(fecha):
    return str(fecha[0]) + "/" + str(fecha[1]) + "/" + str(fecha[2])


for x in pruebasBisiesto:
    print("Año " + str(x) + " es Bisiesto? " + str(bisiesto(x)))
print("-------------")
pruebasEsFechaValida = [(2010, 3, 15), (1582, 3, 15), (1581, 3, 15), (2010, 13, 15), (2004, 2, 29), (2005, 2, 29)]

for y in pruebasEsFechaValida:
    print("La fecha: " + print_fecha(y) + " es valida? " + str(fecha_es_valida(y)))

print("-------------")
pruebasDiaSiguiente = [(2010, 3, 15), (1582, 3, 15), (1581, 3, 15), (2010, 13, 15), (2004, 2, 29), (2005, 2, 29)]

for y in pruebasDiaSiguiente:
    if fecha_es_valida(y):
        print("El dia siguiente a " + print_fecha(y) + " es: " + print_fecha(dia_siguiente(y)))
    else:
        print("Fecha no valida :" + print_fecha(y))
print("-------------")
pruebasDesdePEnero = [(2010, 3, 15), (1582, 3, 15), (1581, 3, 15), (2010, 13, 15), (2004, 2, 29), (2005, 2, 29), (2004, 5, 2)]

for i in pruebasDesdePEnero:
    if fecha_es_valida(i):
        print("El número de dias que han pasado desde " + print_fecha(i) + " es " + str(dias_desde_primero_enero(i)))
    else:
        print("Fecha no valida :" + print_fecha(i))

print("-------------")
pruebasDiaPrimeroEnero = [2000, 2012, 1997, 1823, 2200]
for c in pruebasDiaPrimeroEnero:
    if c >= VIGENCIA_CALENDARIO_GREGORIANO:
        print("El primero de enero del año " + str(c) + " es " + str(DIAS_DE_SEMANA[dia_primero_enero(c)]))
    else:
        print( "Año " + str(c) + "no valido")
