from Animal import Animal

class Bovino(Animal):
    def __init__(self):
        self.propietario=""
        self.fecha_de_vacunacion=""
        self.establo=0
    
    def Pastar(self):
        if self.establo<=5:
            print("PASTAR")
        else:
            print("NO PASTAR")
    def emitir_sonido(self):
      print("MUUU")