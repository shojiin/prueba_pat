class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
def estudiar(self):
    print("Estudiando...")
    
nombre = input('digame su nombre: ')
edad = input('Ahora su edad: ')
grado = input('Por ultimo, su grado: ')

estudiante = Estudiante(nombre,edad,grado)

print(estudiante.nombre)