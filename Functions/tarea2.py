"""
Solución tarea dos Introducción a la programación
Autor: Harold David Guerrero
Código: 8976203

"""


# Ejercicio 1

from cmath import sqrt

def datos_funcion(x,y,z,w): 
    p1 = pow(x -2,z+1)
    p2 = pow(4*y,4-z)
    p3 = 7 * pow(x,y-1)
    p4 = sqrt(x + 3)/4
    p5 = pow(z,4) * pow(w,y+x)
    p6 = pow(x,3) + 6
    
    R = p1 * p2 + p3 - p4 - p5 * p6
    
    return R 

print(datos_funcion(2, 2, 2, 2))


# Ejercicio 2

def volumen_esfera(r):
    pi = 3.1416
    operacion = 4/3 * pi * float(r)**3
    return operacion

print(volumen_esfera(3))

def volumen_cilindro(r, h):
    pi = 3.1416
    operacion2 = pi * r**2 * h
    return operacion2

print(volumen_cilindro(3, 2))

def volumen_cono(r, h):
    pi = 3.1416
    operacion3 = 1/3 * h * pi * r**2
    return operacion3
    
print(volumen_cono(4,2))


# Ejercicio 3

def sumarMayorMenor(a, b, c, d, e):
    mayor = None
    menor = None
    if(a > b and a > c and a > d and a > e):
        mayor = a
    elif(b > a and b > c and b > d and b > e):
        mayor = b
    elif(c > a and c > b and c > d and c > e):
        mayor = c
    elif(d > a and d > b and d > c and d > e):
        mayor = d
    elif(e > a and e > b and e > c and e > d):
        mayor = e

    if(a < b and a < c and a < d and a < e):
        menor = a
    elif(b < a and b < c and b < d and b < e):
        menor = b
    elif(c < a and c < b and c < d and c < e):
        menor = c
    elif(d < a and d < b and d < c and d < e):
        menor = d
    elif(e < a and e < b and e < c and e < d):
        menor = e
    
    suma = mayor + menor
    
    return suma

print(sumarMayorMenor(6, 9, 7, 2, 3))


# Ejercicio 4

def determinarCuadrante(x, y):
    cuadrante = None

    if (x >= 1 and y >= 1):
        cuadrante = 1
    elif (x <= -1 and y >= +1):
        cuadrante = 2
    elif (x <= -1 and y <= -1):
        cuadrante = 3
    elif (x >= 1 and y <= -1):
        cuadrante = 4

    return cuadrante

print(determinarCuadrante(-1, 1))


# Ejercicio 5

# Se usó el ejercicio 4 para evaluar cada punto en los cuadrantes

def cuantosEnCuadrante (x1, y1, x2, y2, x3, y3, x4, y4, c):
    contador = 0

    if determinarCuadrante(x1, y1) == c:
        contador = contador + 1
    if determinarCuadrante(x2, y2) == c:
        contador = contador + 1
    if determinarCuadrante(x3, y3) == c:
        contador = contador + 1
    if determinarCuadrante(x4, y4) == c:
        contador = contador + 1
    
    return contador


#print(cuantosEnCuadrante(2, 3.4, 3, 1, -2.1, -3, -4, 1, 1))
print(cuantosEnCuadrante (2, 3.4, 3, 1, -2.1, -3, -4, 1, 3))


# Ejercicio 6
   
def tienePoquer (a, b, c, d, e):
    ans = None
    if a == b == c == d:
        ans = True
    elif a == b == c == e:
        ans = True
    elif a == c == d == b:
        ans = True
    elif a == c == d == e:
        ans = True
    elif a == d == e == b:
        ans = True
    elif a == d == e == c:
        ans = True 
    else:
        ans = False
    
    return ans
    
print(tienePoquer ("A", "2", "2", "2", "Q"))


# Ejercicio 7

def jugadoresTenis (jugador1, jugador2):
    ans = None
    jugador1N = "jugador 1 harold"
    jugador2N = "jugador 2 david"

    if jugador1 >= 6 and jugador2 <= 4:
        ans = jugador1N
        #print ("el ganador del partido es jugador1")
    elif jugador1 > jugador2:
        ans = jugador1N
        #print ("el ganador del partido es jugador1")  
    elif jugador1 < 6 and jugador2 >= 7:
        ans = jugador2N
        #print ("el ganador del partido es jugador2")
    elif jugador1 == 7 and (jugador2  == 5 or jugador2 == 6 ):
        ans = jugador1N
        #print ("el ganador del partido es el jugador1")
    elif jugador1 < jugador2:
        ans = jugador2N
        #print ("el ganador del partido es jugador2")  
    elif jugador1 > 6 and jugador2 <= 7:
        ans = jugador2N
        #print ("el ganador del partido es jugador2")
    elif jugador2 == 7 and (jugador1  == 5 or jugador1 == 6 ):
        ans = jugador2N
        #print ("el ganador del partido es el jugador2")
    
    return ans

print(jugadoresTenis (7, 4))


# Ejercicio 8

def almuerzo (proteina, calorias, peso, pesoEnsalada):
    ans = None

    if proteina == "Carne desmechada":
        #print ("Almuerzo permitido")
        ans = True
    elif calorias <= 500:
        #print ("Almuerzo permitido")
        ans = True
    elif (calorias >= 500 and calorias < 700) and (peso < 325 and pesoEnsalada >= 100):
        #print ("Almuerzo permitido")
        ans = True
    elif (pesoEnsalada > peso * 60 / 100):
        #print ("Almuerzo permitido")
        ans = True
    else:
        #print ("Almuerzo no permitido")
        ans = False

    return ans

print(almuerzo ("pollo", 600, 300, 200))


# Ejercicio 9

def casillas (fila_reina, columna_reina, fila_peon, columna_peon):
    op_fila = fila_reina - fila_peon
    op_columna = columna_reina - columna_peon

    ans = None
    if (fila_reina == fila_peon):       
        ans = True
    elif (columna_reina == columna_peon):
        ans = True
    elif (op_fila - op_columna == 0):
        ans = True
    else:
        ans = False
    
    return ans

print(casillas (2, 5, 2, 1))


# Ejercicio 10

def puedeSalir (tipo_vehiculo, placa, dia, hora, minutos):
    ans = None
    if (tipo_vehiculo == "Particular"):
        if ((hora == 10 and minutos > 0) or (hora == 20 and minutos > 0)):
            ans = True
        elif ((hora < 10 and hora >= 6 ) or (hora < 20 and hora >= 16)):
            if (dia == "Lunes" and (placa == 7 or placa == 8)):
                ans = False
            elif (dia == "Martes" and (placa == 9 or placa == 0)):
                ans = False
            elif ( dia == "Miércoles" and (placa == 1 or placa == 2)):
                ans = False
            elif (dia == "Jueves" and (placa == 3 or placa == 4)):
                ans = False
            elif (dia == "Viernes" and  (placa == 5 or placa == 6)):
                ans = False
            elif (dia == "Sábado" or dia == "Domingo" and (placa == None)):
                ans = True
            else:
                ans = True
        else:
            ans = True
    elif (tipo_vehiculo == "Servicio Público"):
        if ((hora == 22 and minutos > 0)):
            ans = True
        if ((hora < 22 and hora >= 5)):
            if (dia == "Lunes" and (placa == 6 or placa == 7)):
                ans = False
            elif (dia == "Martes" and (placa == 7 or placa == 8)):
                ans = False
            elif (dia == "Miércoles" and (placa == 0 or placa == 9)):
                ans = False
            elif (dia == "Jueves" and (placa == 1 or placa == 2)):
                ans = False
            elif (dia == "Vienes" and (placa == 3 or placa == 4)):
                ans = False
            elif (dia == "Sábado" and (placa == 1 or placa == 2 or placa == 3 or placa == 4 or placa == 5)):
                ans = False
            elif (dia == "Domingo" and (placa == 6 or placa == 7 or placa == 8 or placa == 9 or placa == 0)):
                ans = False
            else:
                ans = True
        else:
            ans = True
    else:
        ans = True
    
    return ans

print(puedeSalir("Particular", 1, "Miércoles", 17, 1))


