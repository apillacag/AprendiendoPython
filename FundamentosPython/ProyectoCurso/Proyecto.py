#Crear un programa para mostrar el promedio de calificacion
#de alumnos, utilizando los fundamentos de Python

N = int(input("Ingrese la cantidad de alumnos: "))
for i in range(N):
    nombreAl = input("Ingrese el nombre del alumno {}: ".format(i+1))
    apellidoAl = input("Ingrese el apellido del alumno {}: ".format(i+1))
    seccionAl = input("Ingrese la seccion del alumno {}: ".format(i+1))
    gradoAl = input("Ingrese el grado del alumno {}: ".format(i+1))
    M = int(input("Ingrese la cantidad de notas: "))

    mayor = 0
    menor = 9999
    sumaNotas = 0
    for j in range(M):
        while(True):
            nota = int(input("Ingrese la nota {} del alumno {}: ".format(j+1,i+1)))
            if nota >= 0 and nota <= 20:
                break
            else:
                print("El valor de la nota no pertenece a un rango valido")
        if nota > mayor:
            mayor = nota
        if nota < menor:
            menor = nota
        sumaNotas += nota
    if sumaNotas/M < 10.5:
        print("Ha desaprobado el curso")
    else:
        print("Felicitaciones, ha aprobado el curso")
        
    print("La mayor nota del alumno {} es: {}".format(i+1,mayor))
    print("La menor nota del alumno {} es: {}".format(i+1,menor))
    


