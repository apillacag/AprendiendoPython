print("Ejemplo con REMOVE") #Verificar si esta en la lista, y eliminar
lista_letras = ['a','b','c','d','e','f','g','h','i','j','k','l']
print(lista_letras)
if 'z' in lista_letras:
    lista_letras.remove('z')
else:
    print("No esta dentro ee la lista")

print(lista_letras)