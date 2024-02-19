## 1 Hola a todos buenas tarde, rellena tus datos
print("1 Hola a todos buenas tardes, rellena tus datos")
Nombres=input("Ingrese tus Nombres: ")
Apellidos=input("Ingrese tus Apellidos: ")
DNI=input("Ingrese tu número de DNI: ")

# 2 Halle el area de un triángulo, si tenemos los siguientes datos
print("2 Halle el area de un triángulo, si tenemos los siguientes datos")
Base=float(input("Ingrese Base del Triángulo: "))
Altura=float(input("Ingrese Altura del Triángulo: "))
Area_triángulo= Base*Altura/2
print(Area_triángulo)

# 3 Agregar a lista un diccionario que tenga (nombre, edad, correo, cursos)
usuarios=[]
def agregar_usuario():
    name=input("Ingrese su Nombre: ")
    print(saludar(name))
    edad=input("Ingrese su edad: ")
    correo=input("Ingrese su correo: ")
    datos={
        'name':name,
        'edad':edad,
        'correo':correo,
        'cursos':[{'nombrecurso':"matematica",
                   'notas':[10,15,18]},
                   {'nombrecurso':"comunicacion",
                   'notas':[6,10,12]}
                   ]
    }
    print(['name'],['edad'],['correo'],['cursos'],['notas'])

    usuarios.appened(datos)



# 4 clacular promedio de las notas y agregar notas finales
print("ingrese notas")
a=float(input("Primera nota: "))
b=float(input("Segunda nota: "))
c=float(input("Tercera nota: "))
print("Calcularemos el promedio de las notas")
promedio=float((a+b+c) / 3)
print(promedio)


# 5,6 mostrar lista de alumnos aprobados y desaprobados
notas=int(input("Ingrese la cantidad de notas"))
vec=[]
n=0

for i in range(1,notas+1):
    nota=int(input("Nota: "))
    n=n+nota
    vec.append(nota)

promedio=n/len(vec)

npromedio=0
for j in vec:
    if j>promedio:
        npromedio=npromedio+1

aprobado=0
for h in vec:
    if h>10:
     aprobado=aprobado+1

reprobado=0
for k in vec:
    if k<11:
        reprobado=reprobado+1

print("Aprobado:",aprobado)
print("Desaprobado:",reprobado)

#7Generar una funcion rango hasta un n umero grande 10000
for i in range(1,10000):
    if i % (2, 5, 7) ==0:
        print(i)

#8 llamar una funcion que devuelva el mayor de 2 numeros
a = int(input("Ingresa un numero a: "))
b = int(input("Ingresa un numero b: "))

if a == b:
    print("Los numeros son iguales")
else:
    if a > b:
        print(f"El numero mayor es: {a}")
    else:
        print(f"El numero mayor es: {b}")

