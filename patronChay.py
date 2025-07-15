# patron chain of responsibility , patron de comportamiento que permite pasar un solicitud por una cadena de manejadores, cada uno decide si se encarga de la solicitud o se la pasa al siguiente
solicitud  = [
    {
    "usuario " : "camilo" ,
    "tienePermiso" : True,
    "VerificacionSeguridad" : True,    
    },
    {
    "usuario ": "laura",
    "tienePermiso": True,
    "VerificacionSeguridad": False,   # Falla verificación en dos pasos
    },
    {
    "usuario ": "david",
    "tienePermiso": False,            # No tiene permisos suficientes
    "VerificacionSeguridad": True,
    
    },
    {
    "usuario ": None,
    "tienePermiso": True,
    "VerificacionSeguridad": True,    # Acceso debería concederse
    }

]


class Manejador():
    def __init__(self):
        self.siguiente = None # no tiene ningun manejador
        
    def establecerSiguiente(self,manejador):
        self.siguiente = manejador
        
    def manejar(self, solicitud):
        raise NotImplementedError("Debes implementar este método")
    
    

    
class VerificadorUsuario(Manejador):
    def manejar(self,solicitud):
        if solicitud.get("usuario ") is None:# get busca la clave en el diccionario si no hay devuleve el mensaje de abajo
            return "acceso denegado: el usuario no existe. "
        
        
        if self.siguiente:
            return self.siguiente.manejar(solicitud)#self.siguiente:“No soy el último. Otro manejador debe revisar la solicitud”.
        
        return "acceso concedido"
    #“Si hay otro verificador después de mí (self.siguiente), pásale la solicitud a él. Si no hay nadie más, yo decido que el acceso está concedido.”
 
class VerificadorPermisos(Manejador):
    def manejar(self, solicitud):
        if solicitud.get("tienePermiso") is False:
            return  "acceso denegado no tiene permiso"
        
        if self.siguiente:
            return self.siguiente.manejar(solicitud)


class VerificadorSeguridad(Manejador):
    def manejar(self,solicitud):
        if solicitud.get("VerificacionSeguridad") is False:
            return  "❌acceso denegado no tiene permiso"
        
        if self.siguiente:
            return self.siguiente.manejar(solicitud)
        return "✅acceso concedido"
    
# Cadena de responsabilidad
verificador_usuario = VerificadorUsuario()
verificador_permisos = VerificadorPermisos()
verificador_seguridad = VerificadorSeguridad()

verificador_usuario.establecerSiguiente(verificador_permisos)
verificador_permisos.establecerSiguiente(verificador_seguridad)

# Lista de solicitudes
solicitudes = [
    {"usuario ": "camilo", "tienePermiso": True, "VerificacionSeguridad": True},
    {"usuario ": "laura", "tienePermiso": True, "VerificacionSeguridad": False},
    {"usuario ": "david", "tienePermiso": False, "VerificacionSeguridad": True},
    {"usuario ": None, "tienePermiso": True, "VerificacionSeguridad": True},
]

# Evaluar cada solicitud
for i, solicitud in enumerate(solicitudes, 1):
    print(f"Solicitud {i}: {verificador_usuario.manejar(solicitud)}")
