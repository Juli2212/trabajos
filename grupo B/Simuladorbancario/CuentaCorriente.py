__autor__="juliana penafiel"
__license__="gpl"
__version__="1.0.0" 
__email__="juliana.penafiel@campusucc.edu.co"

class CuentaCorriente:
    #AQUI COMIENZA LA CLASE
    '''#___________________________________________________________________________
    # Atributos
    #______________________________________________________________________________'''

    saldo = 0
    deposito = 0
    retiro = 0

    '''#
    Este metodo retorna el nombre del empleado
    #'''
    __method__ = "Darsaldo"
    __parameter__ = "ninguno"
    __returns__ = "saldo de la cuenta"
    __Description__= " metodo que muestra el saldo del cliente"
    def Darsaldo(self):
        return self._saldo
  
    
    __method__ = "Consignarsaldo"
    __parameter__ = "monto"
    __returns__ = "nuevosaldo"
    __Description__= " metodo que permite depositar al monto de la cuenta"

    def Consignarvalor(self, monto):
        #aqui inicia el metodo 
        self._saldo = self._saldo+monto

    __method__ = "Reatirarsaldo"
    __parameter__ = "monto"
    __returns__ = "ninguno"
    __Description__= " metodo que permite retirar al monto de la cuenta"

    def Retirarvalor(self, monto):
        #aqui inicia el metodo 
        self._saldo = self._saldo-monto
    

    