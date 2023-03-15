tupla = ('String', 10, 15.4, True, [1, 2, 3], (4, 5, 6))

#print(tupla)

cursos = ('Python', 'Flask', 'Django', 'Rails', 'MongoDB')

primer_curso = cursos[0]
print(primer_curso)

ultimo_curso = cursos[-1]
print(ultimo_curso)

sub_tupla = cursos[0:3]
print(sub_tupla)

#crear tupla a partir de lista
cursos_tupla = tuple(cursos)
print(cursos_tupla)

#Crear Lista a partir de tupla
niveles = ('Basico', 'Intermedio', 'Avanzado')
niveles_lista = list(niveles)
print(niveles_lista)

#Asignar valor descomprimiendo tupla
uno, dos, tres, cuatro, cinco = cursos
print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)

#Asignar valor desempaquetando tupla pero con tupla de mas valores
#al último variable se le antepone "*" (el asterisco significa Lista) para indicarle que esa variable recibirá el resto de los valores
#Si no vamos a utilizar el resto de valores, entonces se pone "*_" para descartar la asignación del resto de valores
uno, dos, tres, *resto_valores = cursos
print(uno)
print(dos)
print(tres)
print(resto_valores)

##Comprimiendo tuplas y listas (las listas y/o tuplas deben de contener la misma cantidad de elementos, sino no las combina)
lista = [1, 2, 3, 4, 5, 6, 7]
tupla = (10, 20, 30, 40, 50)
lista_2 = [100, 200, 300, 400, 500]
tupla_2 = (1000, 2000, 3000, 4000, 5000)

resultado = zip(lista, tupla, lista_2, tupla_2)
resultado = tuple(resultado)

print(resultado)
