from abc import ABC ,abstractmethod

class vehiculo(ABC):
    def __init__ (self,marca :str):
        self.marca = marca
        
    @abstractmethod
    #el metodo obliga a que las clases hijas lo utilicen y solo se define en la clase padre
    def arrancar(self):
        pass
    
    
    def frenar(self):
        return f"este vehiculo puede frenar y pertenece a la marca{self.marca}"
    
    
    
    
class moto(vehiculo):
    def __init__(self, marca , caballosFuerza: int, torque:int):
        super().__init__(marca)
        self.caballosFuerza = caballosFuerza
        self.torque = torque
        
        
        
    def frenar(self):
        return f"{super().frenar()} y tiene {self.caballosFuerza} caballos de fuerza"
    
    def arrancar(self):
        return f"este vehiculo arrancar con un torque de: {self.torque} newtons de metro"

moto1 =moto ("pulsar", 16,12)
print(moto1.frenar())
print(moto1.arrancar())
        
    