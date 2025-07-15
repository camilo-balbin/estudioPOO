# se utiliza cuando no se puede modificar un codifo viejo(pertenece a patrones de diseño = patron adaptador) 


#clase esperada por el sistema
'''class Reproductor():
 def reproducir(self):
        raise NotImplementedError("debes implementar este metodo")
        # se utiliza para que las clases hijas si o si lo utilicen
    
    
#clase que no se puee modificar
class ReproductorMP3():
    def playAudio(self):
        return "reproduciendo archivo mp3"
    
    
    
class Adaptadora(Reproductor):
    
    def __init__(self,ReproductorMP3):
        self.ReproductorMP3 = ReproductorMP3
    
    def reproducir(self,):
        return self.ReproductorMP3.playAudio()
        
    
        
        
#crear objeto externo  
mp3 = ReproductorMP3()

#se adapta a la interfaz requerida
adaptador = Adaptadora(mp3)

#ahora sse puede utilizar como si fuera reproducir en vez de play audio
print(adaptador.reproducir())'''

'''class impresora():
    
    def imprimir(self):
        raise NotImplementedError("Debes implementar el método imprimir()")
    

class impresoraLaser():
    
    def printDocument(self):
        return "imprimiendo docuemnto con impresora laser"
    
    
class adapatadora(impresora):
    def __init__(self,impLaser):
        self.impLaser = impLaser
        
    def imprimir(self):
        return self.impLaser.printDocument()
        
        
imp = impresoraLaser()
adapater = adapatadora(imp)
print(adapater.imprimir())'''
        
