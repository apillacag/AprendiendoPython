lista_letras = ['a','b','c','d']
variable = 'z'
if variable in lista_letras: #verifico que se encuentre dentro de la lista
    posicion = lista_letras.index(variable) #pido el indice
    print("Esta en la posicion:",posicion)
else:
    print("No hay elementos en la lista")
