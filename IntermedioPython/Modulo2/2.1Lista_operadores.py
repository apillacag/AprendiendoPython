#Sumatoria listas: Crea una sola lista con todos los elementos que se estan sumando
padres = ["mama","papa"]
abuelos = ["abuelo","abuela","hijos"]
numeros = [1,2,3]
familia = numeros + abuelos + padres
print(familia)

#multiplicacion
lista_numeros = [1,2,3,4,5] * 6 #Crear una sola lista con la cantidad de elementos repetidos
print(lista_numeros)

#IN (Se encuentra en la lista)
lista = ["Juan", "Luis", "Almendra", "Jorlan", "Maria", "Luisa"]
print( "Juan" in lista)
print( "Pedro" in lista)

#NOT IN
lista = ["Juan", "Luis", "Almendra", "Jorlan", "Maria", "Luisa"]
print( "Juan" not in lista)
print( "Pedro" not in lista)
