"""Escribir una función que solicite ingresar una serie de números entre a y b y guardarlos en una lista. En caso de ingresar un valor fuera de rango el programa mostrará un mensaje de error y solicitará un nuevo número. Para finalizar la carga se deberá ingresar -1. La función no recibe ningún parámetro, y devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como valor de retorno."""
import random


listaDos =[]
listaUno = []

def funcionUno():
    inicioSerie = int(input("ingrese el punto inicial"))
    finSerie = int(input("ingrese el punto final")) 
    numeros = int(input("ingrese números dentro del rango"))
    while numeros != -1:
        numeros = int(input("ingrese números dentro del rango"))
        if numeros >= inicioSerie and numeros <= finSerie:
            listaUno.append(numeros)
        elif numeros <= inicioSerie or numeros >= finSerie:
            print("numero fuera de rango")
    print(listaUno)

funcionUno()

"""Escribir una función para crear una lista con N números al azar en un rango de valores que se recibe por parámetro. La función devuelve la lista cargada (o vacía si el rango indicado no es válido)."""


iteracionSumaLista = 0

def funcionDos():
    iteracionSumaLista = 0
    rangoDeValores1 = int(input("ingrese el inicio del rango de valores"))
    rangoDeValores2 = int(input("ingrese el ifn del rango de valores"))
    i = 0
    while i < rangoDeValores2:
        numerosParaLista = random.randint(rangoDeValores1, rangoDeValores2)
        listaDos.append(numerosParaLista)
        iteracionSumaLista += numerosParaLista
        i +=1
    print(listaDos)
    print("suma num en la lista", iteracionSumaLista)
funcionDos()
"""Calcular la suma de los números de una lista."""

"""Desarrollar un algoritmo que permita crear al azar 5 números pertenecientes a la lista A y otros 5 números pertenecientes a la lista B. Crear una lista C, donde cada posición es el resultado de la suma del número en la misma posición en la lista A con el número en la misma posición en la lista B. Ejemplo: Se crea A = [1, 2, 3, 4, 5] y B = [4, 7, 1, 3, 6] → C = [5, 9, 4, 7, 11]"""


listaA = []
listaB = []
listaC = []
contadorA = 0
contadorB = 0

for i in range(5):
    numerosListaA = random.randint(1,10)
    listaA.append(numerosListaA)
    contadorA += 1
    numerosListaB = random.randint(1,10)
    listaB.append(numerosListaB)
    contadorB += 1

for i in range(len(listaA)):
    listaC.append(listaA[i]+listaB[i])
    
print(listaA)
print(listaB)
print(listaC)