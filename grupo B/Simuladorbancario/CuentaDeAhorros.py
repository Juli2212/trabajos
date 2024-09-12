__autor__="juliana penafiel"
__license__="gpl"
__version__="1.0.0" 
__email__="juliana.penafiel@campusucc.edu.co"

class CuentaDeAhorros:
    #AQUI COMIENZA LA CLASE
    '''#___________________________________________________________________________
    # Atributos
    #______________________________________________________________________________'''

    saldo = 0
    interes = 0
    deposito = 0
    retiro = 0


    '''#_______________________________________________________________________________
    Metodo
    _________________________________________________________________________________#'''

    __method__ = "Darsaldo"
    __parameter__ = "ninguno"
    __returns__ = "saldo de la cuenta"
    __Description__= " metodo que retorna el saldo del cliente"
    def Darsaldo(self): 
        #aqui inicia el metodo 
        return self.saldo 
    
    
    __method__ = "Consignarvalor"
    __parameter__ = "Monto"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que Permite consignar un monto a la cuenta"
    def Consignarvalor(self, monto):
        # Aqui inicia mi codigo
        self.__saldo = self.__saldo+monto
    
    
    __method__ = "Retirarvalor"
    __parameter__ = "Monto"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que Permite retirar un monto a la cuenta"
    def Retirarvalor(self, monto):
        # Aqui inicia mi codigo
        self.__saldo = self.__saldo-monto
      
    __method__ = "Cambiarinteres"
    __parameter__ = "ninguno"
    __returns__ = "nuevointeres"
    __Description__= " metodo que actualiza el valor del interes del cliente"
    def Darinteres(self):
        self._interes
        