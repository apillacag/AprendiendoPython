#Como es una funcion con retorno se puede almacenar dentro de una variable
def suma(a,b): #parametros
    suma = a + b
    return suma

def resta(a,b):
    resta = a - b
    return resta

def multiplicacion(a,b):
    multiplicacion = a * b
    return multiplicacion

sumatoria = suma(5,7)
print(sumatoria)

resta_resultado = resta(10,2)
print(resta_resultado)

multi = multiplicacion(10,5)
print(multi)