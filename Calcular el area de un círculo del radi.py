#Calcular el area de un círculo del radio ingresado

import math

#Pedido del radio al usuario
rad = float (input ("Bienvenido, por favor ingrese el radio del círculo del cual desea calcular el Area: r= "))

#Cálculo del Area del círculo

A = (math.pi)*(rad**2)

#Devolucion de resultados

print ("El Area del círculo con radio r= ",rad," es A= ",A)
