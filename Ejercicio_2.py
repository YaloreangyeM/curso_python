#EJERCICIO PERÍMETRO Y ÁREA DE UN RADIO DADO
import math

# ENTRADAS DE DATOS
# Declaración o creación de variables

radio= float(input('Escribe el valor del radio'))

#Declarar una constante: Elemento que no cambia
PI = 3.1416

#PROCESOS

perímetro = 2 * PI * radio
cuadrado = pow(radio, 2 )
área = PI * cuadrado

#SALIDAS DE DATOS

print('El perímetro es =', round(perímetro, 2))
print(f'El área es = {área}')
