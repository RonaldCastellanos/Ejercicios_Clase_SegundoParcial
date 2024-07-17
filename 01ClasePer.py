
class Persona:
#Atributos Clases
    especie ="Humano"
def __init__(self, nombre, edad):
     self.nombre = nombre
     self.edad = edad

#Metodo de instancia
def saludar(self):
    print(f'Hola, mi nombre es {self.nombre}')
def cumplir_anios(self, estado_humor):
    print(f'Cumplir {self.edad + 1} años me pone {estado_humor}')

juan = Persona("Juan", 20)

juan.saludar()
juan.complir_anios("feliz")
