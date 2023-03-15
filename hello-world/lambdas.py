def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32


mi_funcion = centigrados_a_farhenheit
print(type(mi_funcion))
print(mi_funcion(10))

# funcion lambda
print('funcion lambda')
funcion_grados = lambda grados : grados * 1.8 + 32

print(funcion_grados(10))

#Sin parametros
sin_parametros = lambda : 2 + 3

#parámetros default
parametros_default = lambda p1=10, p2=20, p3=30 : p1 + p2 + p3

#parametros con asterisco
asterisco = lambda *args, **kwargs: len(args) + len(kwargs)