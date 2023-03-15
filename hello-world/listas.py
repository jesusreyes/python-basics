lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']

print(lista_cursos)

primer_curso = lista_cursos[0]
print(primer_curso)

#Reemplazar Java por Rust
lista_cursos[4] = 'Rust'
print(lista_cursos)


#sublistas
#[start:end]
#[start:] -> Obtenemos los ultimos elementos a partir del indice start
#[:end] -> Obtenemos los primeros elementos hasta el indice end
#[start:end:skip] Obtenemos elementos en la lista con saltos 
sub_lista = lista_cursos[1:4]
print(sub_lista)

sub_lista = lista_cursos[2:]
print(sub_lista)

sub_lista = lista_cursos[:2]
print(sub_lista)

sub_lista = lista_cursos[0::2]
print(sub_lista)

#Añadir elementos a la lista
lista_cursos.append('Java')
lista_cursos.append('C#')
lista_cursos.append('MongoDB')
print(len(lista_cursos)) #Obtiene la longitud de la lista
print(lista_cursos)

#insertar elemento a partir de un indice
lista_cursos.insert(2, 'JavaScript')
print(lista_cursos)

#insertar elementos desde otra lista
lista_cursos_2 = ['C', 'C++', 'Docker']

lista_cursos.extend(lista_cursos_2)
print(lista_cursos)

#Eliminar elementos de la lista
#por nombre
lista_cursos.remove('C')
print(lista_cursos)

#por indice
del lista_cursos[9]
print(lista_cursos)

#eliminar todos
lista_cursos.clear()
print(len(lista_cursos))