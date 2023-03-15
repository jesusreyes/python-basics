def suma(n1, n2):
    return n1 + n2, 'El resultado es:'

numero_uno = int(input('Ingresa el primer número entero: '))
numero_dos = int(input('Ingresa el segundo número entero: '))

resultado, mensaje = suma(numero_uno, numero_dos)
print(mensaje,resultado)

# parametros opcionales
print('Parámetros opcionales')
def area_circulo(radio, pi=3.1416):
    return pi * (radio ** 2)

resultado = area_circulo(11)
print(resultado)

