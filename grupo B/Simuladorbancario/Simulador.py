__autor__="juliana penafiel"
__license__="gpl"
__version__="1.0.0" 
__email__="juliana.penafiel@campusucc.edu.co"

from CuentaDeAhorros import CuentaDeAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class Simulador:
    #AQUI COMIENZA LA CLASE
    '''#___________________________________________________________________________
    # Atributos
    #______________________________________________________________________________'''

    nombre= "" ""
    documento= ""
    mesactual= 0

    '''#__________________________________
    #asociasiones
    ________________________#'''

    __cuentaAhorros=CuentaDeAhorros()
    __cuentaCorriente=CuentaCorriente()
    __cdt=CDT()

    '''_____________________________________________________________________________
    #METODOS
    ________________________________________________________________________________#'''


    __method__ = "DepositarCuentaCorriente"
    __parameter__ = "monto"
    __returns__ = "ninguno"
    __Description__= " metodo que permite depositar en la cuenta corriente"
    def DepositarCuentaCorriente(self, monto):
       self._CuentaCorriente.Consignarsaldo(monto)

    __method__ = "DepositarCuentaAhorros"
    __parameter__ = "monto"
    __returns__ = "ninguno"
    __Description__= " metodo que permite depositar en la cuenta de ahorros"
    def DepositarCuentaDeAhorros(self, monto):
       self._CuentaDeAhorros.Consignarsaldo(monto)
   
    __method__ = "Cambiarsaldo"
    __parameter__ = "ninguno"
    __returns__ = "saldo"
    __Description__= " metodo que actualiza el saldototal del cliente"
    
    def Darsaldo(self):
        #aqui inicia el metodo
        return self.saldo
    

    __method__ = "Calcularsaldototal"
    __parameter__ = "ninguno"
    __returns__ = "Saldo total de todas las cuentas"
    __Description__= " metodo que permite calcular el saldo total en todas las cuentas"
    def CalcularSaldototal(self):
       return self._CuentaCorriente.Darsaldo()+self._CuentaDeAhorros.DarSaldo
    

    __method__ = "PasarAhorrosACorriente"
    __parameter__ = "ninguno"
    __returns__ = "ninguno"
    __Description__= " metodo que permite pasar saldo de la cuenta de ahorros a la cuenta corriente"
    def PasarAhorrosaCorriente(self):
        #aqui inicia el metodo
        saldoAhorros = self.__cuentaAhorros.Darsaldo
        self.__cuentaAhorros.Retirarvalor(saldoAhorros)
        self.__cuentaCorriente.Consignarvalor(saldoAhorros)

    __method__ = "PasarCorrienteAAhorros"
    __parameter__ = "ninguno"
    __returns__ = "ninguno"
    __Description__= " metodo que permite pasar saldo de la cuenta corriente a la cuenta de ahorros"
    def PasarCorrienteAAhorros(self):
        #aqui inicia el metodo
        saldoCorriente = self.__cuentaCorriente.Darsaldo
        self.__cuentaCorriente.Retirarvalor(saldoCorriente)
        self.__cuentaAhorros.Consignarvalor(saldoCorriente)



    __method__ = "RetirarSaldoTotal"
    __parameter__ = "ninguno"
    __returns__ = "SaldoTotal"
    __Description__= " metodo que permite retirar saldo total"
    def RetirarSaldoTotal(self):
      saldoTotal = self.__CalcularSaldototal.Darsaldo
      self.__saldoTotal.Retirarvalor(saldoTotal)
      self.__cuentaAhorros.Consignarvalor(saldoTotal)
   
    
    __method__ = "DuplicarAhorro"
    __parameter__ = "ninguno"
    __returns__ = "CuentaDeAhorros"
    __Description__= " metodo que permite retirar saldo total"
    def DuplicarAhorro(self):
        saldoAhorros = self.__cuentaAhorros.Darsaldo
        self.__cuentaAhorros.Retirarvalor(saldoAhorros)
        self.__cuentaAhorros.Consignarvalor(saldoAhorros)
    

   
    '''#
    Metodo del codigo
    #'''
    __method__ = "Cambiardocumento"
    __parameter__ = "ninguno"
    __returns__ = "documento"
    __Description__= " metodo que actualiza el documento del cliente"
    def Dardocumento(self):
        #aqui inicia el metodo
        return self.documento