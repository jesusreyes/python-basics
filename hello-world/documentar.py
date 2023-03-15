#Docstring
#__doc__ Objeto de python que guarda lo documentado. Se puede documentar(Módulos, clases, métodos y funciones)

def suma(n1, n2):
    """
    La función suma 2 números enteros.

    Argumentos:
    n1 (int)
    n2 (int)

    Se retorna la suma de los parámetros.

    >>> suma(20, 30)
    50

    python3 -m doctest <nombre_archivo.py>
    """

    return n1 + n2

#print(suma.__doc__)
#print(help(suma))