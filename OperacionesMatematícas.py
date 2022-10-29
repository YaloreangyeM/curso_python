# EJEMPLO 1. Operaciones Matemáticas

#Importar una libreria de funciones matemáticas
import math as  m
from re import M #comodín para abreviar los nombres

# ENTRADA DE DATOS
# Declarar o crear las variables
número_1 = float(input('Escribe el 1er número'))
número_2 = float(input('Escribe el 2do número'))
nombre = 'Angélica'
#Declarar una constante: Elemento que no cambia
PI = 3.1416

#PROCESOS (Calculos y/o Operaciones Matemáticas y Lógicas)
suma = número_1 + número_2
resta = número_1 - número_2

multiplicación = número_1 * número_2
división = número_1 / número_2
potencia_1 = número_1 ** número_2
potencia_2 = pow(número_1,número_2)
cuadrado = número_1 ** 2
cubo = pow(número_2, 3)

raíz_cuadrada_1 = m.sqrt(9)
raíz_cuadrada_2 = pow(9,1/2)
raíz_cúbica = pow(27,1/3)


módulo_residuo = número_1 % número_2

#Salida de datos
print('La suma es =', round(suma, 2)) #Argumentos o Parámetros
print('La suma es = ' + str(suma))  #CONCATENACIÓN: Unión de dos o más textos
#Convertir un tipo de dato en otro tipo de dato (CASTEO)

print(f'La suma es = {suma}') #f: formateo de texto
print(f'La resta es = {resta}')
print(f'La multiplicación es = {multiplicación}')
print(f'La división es = {división}')
print(f'La potencia 1 es = {potencia_1}')
print(f'La potencia 2 es = {potencia_2}')
print(f'La cuadrado es = {cuadrado}')
print(f'La cubo es = {cubo}')
print(f'La raíz cuadrada 1 es = {raíz_cuadrada_1}')
print(f'La raíz cuadrada 2 es = {raíz_cuadrada_2}')
print(f'La raíz cubica es = {raíz_cúbica}')
print(f'El módulo resuduo = {módulo_residuo}')
print(f'Nombre: {nombre}')

