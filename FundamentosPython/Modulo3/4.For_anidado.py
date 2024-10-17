#Crear un programa que permita ingresar lo nombres de N alumnos y la cantidad M de cursos
N = int(input("Ingresar cantidad de alumnos"))
for i in range(N):
    nombre = input("ALUMNO {}: ".format(i))
    M = int(input("Ingresar la cantidad de cursos: "))
    for j in range(M):
        curso_nombre = input(("CURSO {}: ".format(j+1)))