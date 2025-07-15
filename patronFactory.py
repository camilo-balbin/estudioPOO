class Vehiculo():
    def mover(self):
        raise NotImplementedError ("debes implementar este metodo")
    
    
class Carro(Vehiculo):
    def mover(self):
        return "moviendo un carro"
    
class Moto(Vehiculo):
    def mover(self):
        return " moviendo una moto"
    
class Bicicleta(Vehiculo):
    def mover(self):
        return "moviendo una bicicleta"
    
# funcion como fabrica  , evitar instanciar demasiadas clases
# como ir a una fabrica y pedir un tipo de carro, la fabrica solo te enetrega el obejto carro 
def crearVehiculo(tipo :str):
    if tipo == "carro":
        return Carro()
    elif tipo == "moto":
        return Moto()
    elif tipo == "bicicleta":
        return Bicicleta()
    else:
        raise ValueError(f"vehiculo no existente: {tipo}")
        # se utiliza para frenar el programa y arrojar un error
        

vehiculo1 = crearVehiculo("carro")
print(vehiculo1.mover())
    