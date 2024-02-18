## determina el area de un circulo con radio pedido desde teclado

import math # IMPORTAMOS LIBRERIA MATH

PI =math.pi # float
# uniendo declaracion , asignacion y parseado
radio=float(input("ingrese el radio: "))

area = PI*math.pow(radio,2)

print(area)