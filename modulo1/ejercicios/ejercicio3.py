#5 mostrar lista de alumnos aprobados y desaprobados
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


