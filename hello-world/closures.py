# Closure es una función que retorna otra función que puede acceder a las variables locales aún cuando hayan finalizado
def saludar(username):
    mensaje = f'Hola {username}' #Variable local

    def mostrar_mensaje(): # Anidada
        print(mensaje)

    return mostrar_mensaje

username = 'Cody'
respuesta = saludar(username)
username = 'Jesus'
respuesta()