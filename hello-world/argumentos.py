# argumentos
# argumentos mandando un listado
print('agrgumentos')
def promedio(listado):
    return sum(listado) / len(listado)

resultado = promedio([10, 10, 5, 7, 10])
print (resultado)

# argumentos mandando solo los valores
print('agrgumentos 2')
def promedio(*args):
    return sum(args) / len(args)


resultado = promedio(10, 10, 5, 7, 10)
print (resultado)

print('agrgumentos 3')
# Al utilicar el "*" antes de args nos permite obtener los valores restantes en una tupla
def promedio(*args):
    return sum(args) / len(args)

def combinacion(p1, p2, *args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)

combinacion(10, 20, 1, 2, 3, 4, 5, 6, 7, 8, p4=1000)

print('agrgumentos 4')
# Al utilicar los "**" antes de kwargs nos permite obtener los valores restantes en un diccionario
def promedio(*args):
    return sum(args) / len(args)

def usuarios(**kwargs):
    print(kwargs)
    print(type(kwargs))

usuarios(eduardo=[10, 10, 8], fernando=[10, 9, 9])

# funciones con "*" y "**"

def combinacion(*args, **kwargs):
    print(args)
    print(kwargs)

combinacion(1, 2, 3, 4, 5, cody=True, curso='Python')