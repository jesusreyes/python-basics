elementos = {}
elementos['nombre']= 'Cody'
elementos[(1,2,3)]= 'La llave es una tupla'
elementos['nombre']= 'Otro Nombre modificado'

print(elementos)
print(len(elementos))

#obtener elementos
diccionario = {'a':1, 'b':2, 'c':3, 'd':4}
valor = diccionario['d']
print(valor)

print('a' in diccionario) 

#get
valor = diccionario.get('d')
print(valor)

#cuando la llave no existe en el diccionario
valor = diccionario.get('z')
print(valor)

valor = diccionario.get('z','La llave no existe en el diccionario')
print(valor)

#setdefault, Intenta obtener el valor de la llave, si no existe le agrrega valor default
print(diccionario)
valor = diccionario.setdefault('z',5)
print(diccionario)

#keys
#values
#items

llaves = tuple(diccionario.keys())
print(llaves)

valores = tuple(diccionario.values())
print(valores)

elementos = tuple(diccionario.items())
print(elementos)

# Eliminar elementos
print(diccionario)
del diccionario['a']
print(diccionario)

valor = diccionario.pop('b')
print(valor)
print(diccionario)

diccionario.clear()
print(diccionario)
