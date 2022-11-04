from Animal import Animal

class Perro(Animal):
        
    def emitir_sonido(self):
     if self.edad>=3:
        print("GUAU GUAU")
     else:
        print("AUF AUF")