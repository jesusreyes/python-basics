class Animal():
    def comer(self):
        print('El animal come.')
    
    def dormir(self):
        print('La animal duerme.')

class Mascota(Animal): 
    pass

class Felino(): 
    def cazar(self):
        print('El felino caza')

class Gato(Mascota, Felino): #Herencia multiple
    pass

morris = Gato()
morris.comer()
morris.dormir()
morris.cazar()