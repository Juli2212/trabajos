__autor__="juliana penafiel"
__license__="gpl"
__version__="1.0.0" 
__email__="juliana.penafiel@campusucc.edu.co"


from Empleado.Fecha import Fecha 


class Empleado:
    #AQUI COMIENZA LA CLASE
    '''#___________________________________________________________________________
    # Atributos
    #______________________________________________________________________________'''

    nombre="" ""
    apellido="  "
    salario= 0

    '''#___________________________________________________________________________
        # 1 = masculino 2 = femenino
        ____________________________________________________________________________#'''
    sexo = 0
    '''#__________________________________
    #asociasiones
    ________________________#'''

    fechadenacimiento= Fecha()
    fechaingreso= Fecha()
    '''_____________________________________________________________________________
    #METODOS
    ________________________________________________________________________________#'''

    '''#
    Este metodo retorna el nombre del empleado
    #'''
    def Darnombre(self):
        #aqui inicia el codigo
        return self.nombre
    
    __method__ = "ConsultarFechadeingreso"
    __parameter__ = "ninguno"
    __returns__ = "Fecha de ingreso"
    __Description__= " metodo que actualiza la fecha de ingreso del empleado"
    def ConsultarFechaIngreso(self):
        return self.fechaingreso.Darfecha()
    
    __method__ = "ConsultarFechadenacimiento"
    __parameter__ = "ninguno"
    __returns__ = "Fecha de nacimiento"
    __Description__= " metodo que actualiza la fecha de nacimiento del empleado"
    def ConsultarFechaNacimiento(self):
        return self.fechadenacimiento.Darfecha()

    __method__ = "CambiarSalariomensual"
    __parameter__ = "nuevoSalario"
    __returns__ = "Salario mensual"
    __Description__= " metodo que actualiza el salario mensual del empleado"

    def cambiarsalario(self,nuevosalario):
        #aqui inicia el metodo 
        self.salario = nuevosalario
    
    def Darsalario(self):
        #aqui inicia el metodo 
        return self.salario 
    
    __method__ = "CalcularImpuestoDelSalariomensual"
    __parameter__ = "ninguno"
    __returns__ = "Impuesto del salario mensual"
    __Description__= "Muestra el impuesto del salario mensual del empleado"
    
    def CalcularimpuestoSalarioMensual(self):
      return self.Darsalario()*0.19
    
    __method__ = "CalcularSalarioAnual"
    __parameter__ = "ninguno"
    __returns__ = "Salario Anual"
    __Description__= "Muestra el salario anual del empleado"
    def CalcularSalarioAnual(self):
        return self.salario*12()

    
    __method__ = "CalcularImpuestoDelSalarioAnual"
    __parameter__ = "ninguno"
    __returns__ = "Impuesto del salario anual"
    __Description__= "Muestra el impuesto del salario anual del empleado"
    
    def CalcularimpuestoSalarioAnual(self):
      return self.CalcularSalarioAnual()*0.19