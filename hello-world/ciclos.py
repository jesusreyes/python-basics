# while
print('while')
numero = 123456789
contador = 1

while numero >= 1:
    print(contador)
    contador += 1
    numero = numero / 10
else:
    print('Fin del ciclo while')

# for
print('for')
usuarios = ['usuario1', 'usuario2', 'usuario3', 'usuario4']

for usuario in usuarios:
    print(usuario)

# range
print('range')
rango = range(11) # Rango del 0 al 10

for valor in rango:
    print(valor)

print('Otro range')
rango = range(5, 11) # Rango del 0 al 10

for valor in rango:
    print(valor)

print('Otro range con saltos')
rango = range(5, 11, 2) # Rango del 0 al 10

for valor in rango:
    print(valor)

# enumerate
print('enumerate')
numeros = [10, 20, 30, 40, 50]

for indice, numero in enumerate(numeros):
    print(indice, numero)

# break
print('break')
titulo_curso = 'Curso profesional de Python'

for caracter in titulo_curso:
    if caracter == ' ':
        break
    print(caracter)

# continue
print('continue')

for caracter in titulo_curso:
    if caracter == 'o':
        continue
    print(caracter)