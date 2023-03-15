class Animal():
    def comer(self):
        print('El animal come.')
    
    def dormir(self):
        print('La animal duerme.')

class Mascota(Animal): 
    def comer(self):
        print('La mascota come.')

class Felino(): 
    def cazar(self):
        print('El felino caza.')

class Gato(Mascota, Felino): #Herencia multiple
    def __init__(self, nombre):
        self.nombre = nombre

    def dormir(self):
        print(f'{self.nombre} duerme.')

morris = Gato('Morris')
morris.comer()
morris.dormir()
morris.cazar()