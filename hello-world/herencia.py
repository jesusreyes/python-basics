class Mascota: #Clase Padre

    def comer(self):
        print('La mascota come')
    
    def dormir(self):
        print('La mascota duerme.')

class Perro(Mascota): #Clase hija que hereda de (Mascota)
    pass

class Gato(Mascota):
    pass

loki = Perro()
loki.comer()
loki.dormir()

morris = Gato()
morris.comer()
morris.dormir()