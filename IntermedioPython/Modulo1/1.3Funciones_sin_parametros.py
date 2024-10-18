def suma():
    a = int(input("Ingresar el numero 1: "))
    b = int(input("Ingresar el numero 2: "))
    suma = a + b
    return suma

print(suma())

def suma():
    a = int(input("Ingresar el numero 1: "))
    b = int(input("Ingresar el numero 2: "))
    suma = a + b
    print(suma)

suma()

def calculadora(x,y):
    suma = x+y
    resta = x-y
    multiplicacion = x*y
    return suma, resta, multiplicacion

a, b , c = calculadora(10,5)
print(a,b,c)