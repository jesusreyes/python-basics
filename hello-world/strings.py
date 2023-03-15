lenguajes = 'Python Ruby Java Rust C++ C'

#Split
listado_lenguajes = lenguajes.split(' ')
print(listado_lenguajes)

#Join
lenguajes_2 = ['Python', 'Ruby', 'Java', 'Rust']
string_lenguajes = ' - '.join(lenguajes_2)
print(string_lenguajes)

#Concatenar
nombre = 'Jesus'
apellido = 'Reyes'
nombre_completo = 'Mr. ' + nombre + ' ' + apellido
print(nombre_completo)

nombre_completo = 'Mr. %s %s %s.' %(nombre, apellido, 'Aganza')
print(nombre_completo)

#Placeholders
nombre_completo = 'Mr. {} {} {}'.format(nombre, apellido, 'Aganza')
print(nombre_completo)

nombre_completo = 'Mr. {primer_apellido} {segundo_apellido} {nombre}' .format(
    nombre = nombre,
    primer_apellido = apellido,
    segundo_apellido = 'Aganza')

print(nombre_completo)

#Interpolación
nombre_completo = f'Mr. {nombre} {apellido} {"Aganza"}'
print(nombre_completo)

print(nombre, apellido, 'Aganza')
print(nombre, apellido, 'Aganza', sep=' - ')

#Búsqueda de strings
titulo_curso = 'Curso profesional de Python, donde aprenderemos Python'
contador = titulo_curso.count('Python')
print(contador)

print('python' in titulo_curso)
print('python' in titulo_curso.lower())

print(titulo_curso.startswith('python'))
print(titulo_curso.startswith('Curso'))

print(titulo_curso.endswith('python'))
print(titulo_curso.endswith('Curso'))

#Alinear strings
#ljust -> Alinear a la izquierda
#rjust -> Alinear a la derecha
#center -> Centrar texto
mensaje = 'Hola, este es un mensaje alineado'

mensaje = mensaje.ljust(200)
print(mensaje, '.')

mensaje = mensaje.rjust(200)
print(mensaje)

mensaje = mensaje.center(200)
print(mensaje)

