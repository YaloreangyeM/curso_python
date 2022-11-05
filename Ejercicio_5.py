#EJERCICIO formula general
import math as m

# ENTRADAS DE DATOS
# Declaración o creación de variables

a= float(input('Escribe el valor de a: '))
b= float(input('Escribe el valor de b: '))
c= float(input('Escribe el valor de c: '))


#PROCESOS

x1 = (-(b)-(m.sqrt(pow(b,2)-(4*a*c)))) / (2*a)
x2 = (-(b)+(m.sqrt(pow(b,2)-(4*a*c)))) / (2*a)

#SALIDAS DE DATOS

print(f'El valor de x1 es = {x1}')
print(f'El valor de x2 es = {x2}')

