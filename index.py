# -*- coding: utf-8 -*-
"""
@author: Andrés Cámara
"""
#Programa que realiza varias operaciones matemáticas,
#te pide que metas una ocpión y que introduzcas los valores
#de una forma más eficiente

#Importamos la librería math
import math

#Esto es una función que me pide que intriduzca dos valores por pantalla y me devuelve una tupla con esos valores
def introducir():
    a= int(input("Introduce el primer número para la operación:\n"))
    b= int(input("Introduce el segundo número para la operación:\n"))
    return (a,b)
#Esto es una función que me pide que introduzca un dato por pantalla y me devuelve ese dato 
def pedir_dato():
    a= int(input("Introduce un número para la operación:\n"))
    return a
#definimos una variable con valor 0    
op=0
#creamos un blucle while que nos va a permitir ejecutarlo hasta que le digamos al programa que finalice
salir=True
while salir:
    print("     CALCULADORA")
    print("-----------------")
    print("Menu calculadora")
    print("-----------------\n")
    print(" 1. Sumar\n 2. Restar\n 3. Multiplicar\n 4. Dividir\n 5. Exponente\n 6. Area del triángulo\n 7. Area del rectángulo\n 8. Area del cuadrado\n 9. Area del círculo\n 10. Longitud del círculo\n 11. Pasar de grados ºC a grados ºF\n 0. Salir\n")
    
#pedimos que elija una de las opciones con input 
    op= int(input("Introduce la operación que desea realizar: \n"))
#si la opcion es 1 se ejecuta la operación suma
#hace un print con el resultado de la funcion suma con la función introducir
    if (op == 1):
        suma = lambda x: x[0]+x[1]
        print("El resultado de la suma es:\n",suma(introducir()))
#si la opcion es 2 se ejecuta la operación resta
#hace un print con el resultado de la funcion resta con la función introducir
    elif (op == 2):
        resta = lambda x: x[0]-x[1]
        print("El resultado de la resta es:\n",resta(introducir()))
#si la opcion es 3 se ejecuta la operación multiplicacion 
#hace un print con el resultado de la funcion multiplicacion con la función introducir
    elif (op == 3):
        multiplicacion = lambda x: x[0]*x[1]
        print("El resultado de la mulitplicación es:\n",multiplicacion(introducir()))
#si la opcion es 4 se ejecuta la operación division
#hace un print con el resultado de la funcion division con la función introducir
    elif (op == 4):
        division = lambda x: x[0]/x[1]
        print("El resultado de la división es:\n",division(introducir()))
#si la opcion es 5 se ejecuta la operación exponente
#hace un print con el resultado de la funcion del exponente con la función introducir
    elif (op == 5):
        exponente = lambda x: x[0]**x[1]
        print("El resultado del exponente es:\n",exponente(introducir()))
#si la opcion es 6 se ejecuta la operación area de un triangulo
#hace un print con el resultado de la funcion triangulo con con la función introducir
    elif (op == 6):
        triangulo = lambda x: x[0]*x[1]/2
        print("El area del triángulo es:\n",triangulo(introducir()))
#si la opcion es 7 se ejecuta la operación area del rectangulo
#hace un print con el resultado de la funcion multiplicacion con la función introducir
    elif (op == 7):
        multiplicacion = lambda x: x[0]*x[1]
        print("El area del rectángulo es:\n",multiplicacion(introducir()))
#si la opcion es 8 se ejecuta la operación area del cuadrado
#hace un print con el resultado de la funcion multiplicacion con la función introducir
    elif (op == 8):
        multiplicacion = lambda x: x[0]*x[1]
        print("El area del cuadrado es:\n",multiplicacion(introducir()))
#si la opcion es 9 se ejecuta la operación area del circulo
#hace un print con el resultado de la funcion areaCir con la funcion pedir_dato
    elif (op == 9):
        Acirculo = lambda x: (x**2)*math.pi
        print("El area del círculo es:\n",Acirculo(pedir_dato()))
#si la opcion es 10 se ejecuta la operación restar
#hace un print con el resultado de la funcion lonCir con la funcion pedir_dato
    elif (op == 10):
        Lcirculo = lambda x: (2*math.pi)*x
        print("La longitud del círculo es:\n",Lcirculo(pedir_dato()))
#si la opcion es 11 se ejecuta la operación pasar de ºC a ºF
#hace un print con el resultado de la funcion gradFar con la funcion pedir_dato
    elif (op == 11):
        grados = lambda x: x*(9/5)+32
        print("Los grados ºF son:\n",grados(pedir_dato()))
#si la opcion es 0 se acaba el bucle while y se sale del programa
    elif op == 0:
        salir=False
print("Salir del programa")