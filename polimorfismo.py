class Persona:
    def __init__(self, nombre : str,cedula : int ,edad : int ):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        
        
    def hablar(self):
        return f"hola mi nombre es: {self.nombre}, mi cedula es: {self.cedula} y mi edad es de:{self.edad} y yo puedo hablar"
        
        
        
        
class hombre(Persona):
    def __init__(self, nombre, cedula, edad,genero:str):
        super().__init__(nombre, cedula, edad,)
        self.genero = genero
    
    #polimorfismo: era el metodo de la clase padre (hablar) pero en la clase hija se utiliza el metodo de difernte forma o se sobreescribe el metodo
    
    
    def hablar(self):
        return f"{super().hablar()} y mi genero es: {self.genero}"
    # con el super() traemos el constructor del metodo padre y solo sobreescribimos lo que queremos
        
        
        
        
class mujer(Persona):
    def __init__(self, nombre, cedula, edad,trabajo:str):
        super().__init__(nombre, cedula, edad,)
        self.trabajo = trabajo 
        
        
    def hablar(self):
        return f"{super().hablar()} y trabajo como:{self.trabajo}"
        
        
        
        
        
        
        
persona1 = Persona("yamile", 39575225, 48)

hombre1 = hombre("cristian", 1193265503, 23," masculino")
mujer1 = mujer ("valentina" , 1000287703, 22 , "veterinaria")
print(mujer1.hablar())