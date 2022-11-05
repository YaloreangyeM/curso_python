#EJERCICIO PROMEDIO DE 3 CALIFICACIONES
import math

# ENTRADAS DE DATOS
# Declaración o creación de variables

calificación_1= float(input('Escribe la 1ra calificación'))
calificación_2= float(input('Escribe la 2da calificación'))
calificación_3= float(input('Escribe la 3ra calificación'))




#PROCESOS
suma= calificación_1 + calificación_2 + calificación_3
promedio = suma / 3


#SALIDAS DE DATOS

print(f'El promedio es = {promedio}')
print('El promedio es', round(promedio, 0))



