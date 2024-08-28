class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad   
    
    def hablar(self):
        print("hola como estas?")
       
        
class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,notas,univercidad,):
        super().__init__(nombre,edad,nacionalidad)
        self.notas = notas
        self.univercidad = univercidad
        
roberto = Empleado("roberto",43,"argentino","programador",100000)

print(roberto.nacionalidad)
