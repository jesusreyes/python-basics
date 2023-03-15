def pares():
    for numero in range(0, 100, 2):
        yield numero # Pausa la iteración, retorna numero y luego reanuda

        print('Se reanuda la iteración')
"""
for par in pares():
    print(par)

"""

generador = pares()

while True:
    try:
        par = next(generador) # Obtiene el siguiente elemento del generador
        print(par)
    except StopIteration:
        print('El generador finalizó')
        break
    