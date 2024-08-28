class Celular:
    #creamos la funcion contructora 
    def __init__(self,marca,modelo,camara):
        #esto se va ajecutar simpre
        #cada vez que instanciemos la clase dentro del objeto
        #almacenamos los parametros pasados dentro del mismo 
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self):
            print(f"estas haciendo un llamado desde un: {self.modelo}")
            
    def cortar(self):
            print(f"cortaste la llamada desde tu: {self.modelo}")
        
        
    
celular1 = Celular("Samsung","S23","48MP")
celular2 = Celular("apple","iPhone 15 Prop","98MP")


celular2.llamar()
