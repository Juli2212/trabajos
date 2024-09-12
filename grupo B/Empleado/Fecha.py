__autor__="juliana penafiel"
__license__="gpl"
__version__="1.0.0" 
__email__="juliana.penafiel@campusucc.edu.co"

class Fecha:
    #AQUI COMIENZA LA CLASE
    '''#___________________________________________________________________________
     Atributos
    #______________________________________________________________________________'''

    anio = 0 
    mes = 0
    dia = 0

    '''#___________________________________________________________________________
     Metodos
    #______________________________________________________________________________'''

    __method__ = "Cambiardia"
    __parameter__ = "ninguno"
    __returns__ = "dia"
    __Description__= " metodo que actualiza el dia del empleado"

    def Dardia(self):
        #aqui inicia el codigo
        return self.dia 

    __method__ = "Cambiarmes"
    __parameter__ = "ninguno"
    __returns__ = "mes"
    __Description__= " metodo que actualiza el mes del empleado"

    def Darmes(self):
        #aqui inicia el codigo
        return self.mes 

    __method__ = "Cambiaranio"
    __parameter__ = "ninguno"
    __returns__ = "anio"
    __Description__= " metodo que actualiza el anio del empleado"


    def Daranio(self):
        #aqui inicia el codigo
        return self.anio
    
    __method__ = "Cambiarfecha"
    __parameter__ = "ninguno"
    __returns__ = "fecha"
    __Description__= " metodo que actualiza la fecha del empleado"

    def Darfecha(self):
        #aqui inicia el codigo
        return self.dia+"/"+ self.mes+"/"+ self.anio