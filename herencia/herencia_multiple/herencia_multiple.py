class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad   
    
    def hablar(self):
        print("hola como estas?")
        
class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
    def mostrar_habilidad(self):
        return f"Mi hablidad es {self.habilidad}"
        
class EmpleadoArtistas(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)    
        self.salario = salario
        self.empresa = empresa 
    def presentarse(self):
        print( f"hola soy {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}")
        
roberto = EmpleadoArtistas("roberto",43,"argentino","cantar",20000,"telefe")


herencia = issubclass(EmpleadoArtistas,Persona)
instacia = isinstance(roberto,EmpleadoArtistas)
 
roberto.presentarse()