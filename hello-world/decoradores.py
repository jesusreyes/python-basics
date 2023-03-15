"""
a-> La función principal (Decorador)
b-> La función a decorar
c-> La función decorada

a(b) -> c
"""

def funcion_a(funcion_b):
    def funcion_c():
        print('>>> Antes del llamado')
        funcion_b()
        print('>>> Después del llamado')

    return funcion_c

@funcion_a
def saludar():
    print('Hola, nos encontramos en una funcion a decorar')

saludar()

# Decorador con argumentos
def funcion_d(funcion_e):
    
    def funcion_f(*args):
        print('>>> Antes del llamado')
        resultado = funcion_e(*args)
#        print('>>> Después del llamado')

        return resultado

    return funcion_f

@funcion_d
def suma(numero_1, numero_2):
    return numero_1 + numero_2

resultado = suma(15, 80)
print(resultado)