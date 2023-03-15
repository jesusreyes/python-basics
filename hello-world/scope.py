animal = 'León' #Variable Global

def imprimir_animal():
    animal = 'Ballena' #Variable Local
    print(animal)
    print(id(animal))

imprimir_animal()
print(animal)
print(id(animal))

# Modificar variable global dentro de una funcion
print('Modificar variable global')
def imprimir_animal():
    global animal 
    animal = 'Ballena' #Variable Local
    print(animal)
    print(id(animal))

imprimir_animal()
print(animal)
print(id(animal))