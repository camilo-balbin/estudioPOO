class persona():
    def __init__(self,nombre : str, edad : int):
        self.__nombre = nombre # atributo encapsulado
        self.__edad = edad
        
        
     # convierte un atributo encapsulado en solo lectura para poder acceder a el    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
     
        
    def saludar(self):
        return f"hola mi nombre es: {self.nombre} y mi edad es: {self.edad}"
    
    def caminar(self):
        return f"hola {self.nombre} tu puedes caminar"

    
    #sirve para modificar un atributo encapsulado
    @edad.setter
    def edad(self, nuevaEdad : int):
        
        if  nuevaEdad >= 0:
            self.__edad = nuevaEdad
            
            
    @nombre.setter
    def nombre(self, NuevoNombre : str):
        self.__nombre = NuevoNombre
        
            
        
    


camilo = persona("camilo" , 23)

print(camilo.saludar())
#print(camilo.caminar())

camilo.edad = 30
print(camilo.saludar())

camilo.nombre = "arnulfo"
print (camilo.saludar())
