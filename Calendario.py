
LIMITES_MENSUALES = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
VIGENCIA_CALENDARIO_GREGORIANO = 1582
DIAS_DE_SEMANA = {0: "domingo", 1: "lunes", 2: "martes", 3: "miercoles", 4: "jueves", 5: "viernes", 6: "sabado"}

#*Dado un año perteneciente al rango permitido, determinar si este es bisiesto. El
#resultado debe ser un valor booleano, True o False.

def bisiesto(año):
    if año % 100 == 0:
        return (año % 4 == 0) and (año % 400 == 0)
    else:
        return año % 4 == 0


#Dada una fecha, determinar si ésta es válida. El resultado debe ser un
#valor booleano, True o False.
def fecha_es_valida(fecha):
    dia = fecha[2]
    mes = fecha[1]
    año = fecha[0]
    if año >= VIGENCIA_CALENDARIO_GREGORIANO and mes <= 12:
        if bisiesto(año) and mes == 2:
            return dia <= 29
        else:
            return dia <= LIMITES_MENSUALES[mes]
    return False


#Dada una fecha válida, determinar la fecha del día siguiente. El resultado
#debe ser una fecha válida (tupla de tres números enteros positivos que corresponde a una fecha
#en el Calendario gregoriano.

def dia_siguiente(fecha):
    if fecha_es_valida(fecha):
        dia = fecha[2]
        mes = fecha[1]
        año = fecha[0]

        if fecha_es_valida( ( año, mes, dia +1 ) ):
            x = ( año, mes,dia + 1)
            return x
        elif dia == 31 and mes == 12:
            x = (año +1, 1, 1)
            return x
        else:
            return (año, mes + 1, 1)



#
#Dada una fecha válida, determinar el número de días
#transcurridos desde el primero de enero de su año (el número de días transcurridos entre el
#primero de enero y el primero de enero, dentro de un mismo año, es 0). El resultado debe ser un
#número entero.
#
def dias_desde_primero_enero(fecha):
    dia = fecha[2]
    mes = fecha[1]
    año = fecha[0]

    if mes <= 1: #Si el mes es Enero solo es necesario contar los dias
        return dia - 1
    elif bisiesto(año) and mes >=3: #La variable principal para el calculo se si el año es bisiesto
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
#Se toma de referencia el primer día válido viernes 1 enero 1582
#
#Se toma la premisa que un bisiesto se da cada 4 años
def dia_primero_enero(año):
    
    if(año >= 1582):
        
        cantidad_de_dias_movidos_por_año = 0

        numero_de_años = año-1581
        
        cantidad_de_dias_movidos_por_año += numero_de_años

        cantidad_de_dias_movidos_por_año += (numero_de_años%4)

        valor_viernes = 5

        cantidad_de_dias_movidos_por_año += valor_viernes

        dia_correspondiente = (cantidad_de_dias_movidos_por_año % 7)
        
        print("El dia del primero de enero del año: "+str(año)+ " es "+ str(dia_correspondiente))

    else:
        print("Año introducido no válido")

    return 

