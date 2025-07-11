#clase padre
class animal:
    def __init__ (self,nombre:str, edad: int ):# metodo constructor
        self.nombre = nombre
        self.edad = edad 
        
    def mostrarInformacion(self):
        return f"el nombre del animal es: {self.nombre} y la edad es: {self.edad}"
        
    
    
    
# herencia, la clase gato hereda atributos y metodos de la clase padre (animal) y se le puede agregar mas atributos 
# al momento de llamar la clase gato de un vez hereda la metodo del padre
# la clase gato tiene todo lo que tiene la clase animal
#clase hija
class gato(animal):
    def __init__ (self,nombre:str, edad: int,raza: str ):
        super().__init__(nombre,edad) # al añadir super llamamos a los atributos del padre sin tener que reescribir codio
        self.raza = raza 


class perro(animal):
    def __init__(self,nombre:str, edad: int,raza: str, ruido: str ):
        super().__init__(nombre,edad)
        self.raza = raza
        self.ruido = ruido
        
    
    
    
    
    
    
    
animal1=animal("danyer", 7)
gato1 = gato("michi",4,"egipcio")
perro1 = perro ("kira", 12 , "coker", "gua gua")
print(perro1.mostrarInformacion())