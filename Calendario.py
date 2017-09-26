
LIMITES_MENSUALES = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
VIGENCIA_CALENDARIO_GREGORIANO = 1582

#*Dado un año perteneciente al rango permitido, determinar si este es bisiesto. El
#resultado debe ser un valor booleano, True o False.

def bisiesto(año):

    return (año % 4 == 0) and (año % 100 == 0) or (año % 400 == 0)

#Dada una fecha, determinar si ésta es válida. El resultado debe ser un
#valor booleano, True o False.
def fecha_es_valida(fecha):
    dia = fecha[3]
    mes = fecha[2]
    año = fecha[1]
    if año >= VIGENCIA_CALENDARIO_GREGORIANO and mes <= 12:
        if bisiesto(año) and mes == 2:
            return dia <= 29
        else:
            return dia <= LIMITES_MENSUALES[mes]


#Dada una fecha válida, determinar la fecha del día siguiente. El resultado
#debe ser una fecha válida (tupla de tres números enteros positivos que corresponde a una fecha
#en el Calendario gregoriano.

def dia_siguiente(fecha):
    if fecha_es_valida(fecha):
        dia = fecha[3]
        mes = fecha[2]
        año = fecha[1]

        if fecha_es_valida(  dia + 1, mes, año ):
            return dia + 1, mes, año
        elif dia == 31 and mes == 12:
            return 1, 1, año +1
        else:
            return 1, mes + 1, año

    else:
        print("La fecha ingresada no es valida")


#
#Dada una fecha válida, determinar el número de días
#transcurridos desde el primero de enero de su año (el número de días transcurridos entre el
#primero de enero y el primero de enero, dentro de un mismo año, es 0). El resultado debe ser un
#número entero.
#
def dias_desde_primero_enero(fecha):
    dia = fecha[3]
    mes = fecha[2]
    año = fecha[1]

    if mes <= 1:
        return dia - 1
    elif bisiesto(año) and mes >=3:
        cont = 0
        for x in range(mes - 1):
            cont += LIMITES_MENSUALES[x]
        return cont + 1 + dia
    else:
        cont = 0
        for x in range(mes - 1):
            cont += LIMITES_MENSUALES[x]
        return cont + dia



#Dado un año perteneciente al rango permitido, determinar el día de la
#semana que le corresponde, con la siguiente codificación: 0 = domingo, 1 = lunes, 2 = martes, 3 =
#miércoles, 4 = jueves, 5 = viernes, 6 = sábado. El resultado debe ser un número entero, conforme
#a la codificación indicada.
def dia_primero_enero(año):

    return 0

