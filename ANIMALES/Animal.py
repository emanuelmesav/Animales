

class Animal:
    def __init__(self):
        self.peso=""
        self.edad=""
        self.raza=""
        self.fecha_vacunacion=""
        self.propietario=""
    def correr(self):
     if self.edad>=5:
        print("RAPIDO")
     else:
        print("LENTO")
    def emitir_sonido(self):
     pass
    def Obtener_edad(self):
      self.edad=int(input("INGRESE LA EDAD DEL ANIMAL"))


