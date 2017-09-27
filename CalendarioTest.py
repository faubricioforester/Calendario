from Calendario import *

pruebasBisiesto=[2000,2001,2096,2100,2200]

for x in pruebasBisiesto:
    print("Año "+ str(x) + " es Bisiesto? " + str(bisiesto(x)))
    
pruebasEsFechaValida =[]

for y in pruebasEsFechaValida:
    print("La fecha: " + str(y[2]) +"/" + str(y[1]) + "/" + str(y[0]) + " es valida?" + str(fecha_es_valida(y)))


pruebasDiaSiguiente = []

for y in pruebasDiaSiguiente:
    print("El dia siguiente a "+ str(y[2]) +"/" + str(y[1]) + "/" + str(y[0])+ " es: " + str(dia_siguiente(y)[2] ) +"/"+ str(dia_siguiente(y)[1] + "/" + str(dia_siguiente(y)[0] ))
