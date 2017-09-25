print("Por")
limites_mensuales = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

#*Dado un año perteneciente al rango permitido, determinar si este es bisiesto. El
#resultado debe ser un valor booleano, True o False.
def bisiesto(anio):

    return (anio % 4 == 0) and (anio % 100 == 0) or (anio % 400 == 0)

#Dada una fecha, determinar si ésta es válida. El resultado debe ser un
#valor booleano, True o False.
def fecha_es_valida(fecha):


    return True

#Dada una fecha válida, determinar la fecha del día siguiente. El resultado
#debe ser una fecha válida (tupla de tres números enteros positivos que corresponde a una fecha
#en el Calendario gregoriano.

def dia_siguiente(fecha):


    return True

#
#Dada una fecha válida, determinar el número de días
#transcurridos desde el primero de enero de su año (el número de días transcurridos entre el
#primero de enero y el primero de enero, dentro de un mismo año, es 0). El resultado debe ser un
#número entero.
#
def dias_desde_primero_enero():

    return True

#Dado un año perteneciente al rango permitido, determinar el día de la
#semana que le corresponde, con la siguiente codificación: 0 = domingo, 1 = lunes, 2 = martes, 3 =
#miércoles, 4 = jueves, 5 = viernes, 6 = sábado. El resultado debe ser un número entero, conforme
#a la codificación indicada.
def dia_primero_enero():

    return 0

