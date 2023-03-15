lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]
print(lista)

#Metodo Ordenar
lista.sort()
print(lista)

#Ordenar de forma descendente
lista.sort(reverse=True)
print(lista)

#Metodo para mínimo y maximo de una lista
print('Número menor: ' + str(min(lista)))
print('Número mayor: ' + str(max(lista)))

#Metodo para saber si existe el elemento en la lista
print(10 in lista)
print(5 in lista)
print(8 not in lista)

#Metodo index nos devuelve el indice del valor del elemento
index = lista.index(44)
print(index)