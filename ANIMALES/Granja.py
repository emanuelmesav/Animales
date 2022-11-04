from Animal import Animal
from Perro import Perro
from Bovino import Bovino

class Granja:
    def __init__(self):
        self.Perros=[]
        self.Bovinos=[]
        self.misAnimales=Animal()
    def agregar_perro(self, edad, raza, peso, propietario, fecha_vacunacion):
        misPerros=Perro()
        misPerros.edad=edad
        misPerros.raza=raza
        misPerros.peso=peso
        misPerros.fecha_vacunacion=fecha_vacunacion
        misPerros.propietario=propietario
    def agregar_Bovino(self, edad, raza, peso, propietario, fecha_vacunacion):
        misBovinos=Bovino()
        misBovinos.edad=edad
        misBovinos.raza=raza
        misBovinos.peso=peso
        misBovinos.fecha_vacunacion=fecha_vacunacion
        misBovinos.propietario=propietario
    def obtener_Perros(self, indice):
        return self.Perros[indice]
    def obtener_Bovinos(self, indice):
        return self.Bovinos[indice]

