#EJERCICIO GRADOS A C° F° K°
import math

# ENTRADAS DE DATOS
# Declaración o creación de variables

celsius= float(input('Escribe los grados C°'))
fahrenheit= float(input('Escribe los grados F°'))
kelvin= float(input('Escribe los grados K°'))

#PROCESOS

#Celsius
celsisus_Kelvin= celsius + 273.15
celsisus_fahrenheit = ((9 * celsius) / 5 ) + 32 

#Fahrenheit

fahrenheit_celsius = ( 5 * (fahrenheit - 32) ) / 9
fahrenheit_kelvin = (( 5 * (fahrenheit - 32) ) / 9) + 273.15

#Kelvin

kelvin_celsius = kelvin - 273.15
kelvin_fahrenheit = (9 * (( kelvin-273.15)/5)) + 32


#SALIDAS DE DATOS

print(f'De celsius a fahrenheit = {celsisus_fahrenheit}')
print(f'De celsius a kelvin = {celsisus_Kelvin}')

print(f'De fahrenheit a celsius = {fahrenheit_celsius}')
print(f'De fahrenheit a kelvin = {fahrenheit_kelvin}')

print(f'De kelvin a celsius = {kelvin_celsius}')
print(f'De kelvin a fahrenheit = {kelvin_fahrenheit}')