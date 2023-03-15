# Attrs de clase
# Attrs de instancia

class Usuario:
    # Attrs de clase
    username = 'Username por default'
    email = ''

# __dict__
user1 = Usuario() # Se instancia la clase
user2 = Usuario() # Se instancia la clase

# 1.- Verifica si el attr existe dentro del objeto
# 2.- Verifica si el attr existe dentro de la clase -> solo lectura
# 3.- Lanzará error

user1.username = 'Cody' 
user1.password = '1234'# Este atributo no esta definido en la clase y se puede agregar porque python permite agregar atributos dinamicamente

print(user1.username) # username desde objeto instanciado
print(Usuario.username) # username desde la clase

print(user1.__dict__) #nos muestra los atributos del objeto
