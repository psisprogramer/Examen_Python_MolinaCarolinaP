from datetime import *
from calculo import calculo_nomina

#Diccionarios para almacenar los datos
registros_empleados = {}
registros_empleados_asistencia = {}
registros_bonos_extra = []

#Función para registrar un empleados
def registrar_empleado():
    try:
        identificacion = input("Ingrese el numero de identificacion del empleado: ")
        if identificacion in registros_empleados: #verificación que el numero de identificación ya existe
            print("Empleado ya registrado")
            return
        else:
            nombre = input("Ingrese el nombre del empleado: ")  
            cargo = input("Ingrese el cargo del empleado: ")
            salario = float(input("Ingrese el salario del empleado: ")) #entradas
            registros_empleados[identificacion] = {"name": nombre, "position": cargo, "salary": salario,} #Registro en el diccionario de empleados
            print("Empleado registrado exitosamente")
            # prrint(registros_empleados[identificacion])
    except ValueError : 
        print("Ingrese una cantidad valida")
#Función para registrar asistencia, permite registrar la cantidad de faltas por empleado y por día
def registrar_asistencia():
    try:
        identificacion = input("Ingrese el numero de identificacion del empleado: ")
        if identificacion not in registros_empleados: # type: ignore #verificación que el numero de identificación existe
            print("Empleado no registrado")
            return
        else:
            registros_empleados_asistencia = {"id":identificacion}
            faltas = int(1)
            fecha = datetime.now().strftime("%Y-%m-%d") #fecha actual en formato yyyy-mm-dd
            if fecha not in registros_empleados_asistencia:
                registros_empleados_asistencia[identificacion] = {fecha: faltas}
                print("Falta registrada exitosamente")
                # print(registros_empleados_asistencia[identificacion])
            else:
                print("Falta registrada anteriormente")
                falta += 1
    except ValueError : 
        print("Ingrese una cantidad válida")
#funcion para registrar bonos extra legales, se registran con la fecha de ese mismo día 
def registrar_bonos_extra():
    try:
        identificacion = input("Ingrese el numero de identificación del empleado: ")
        if identificacion not in registros_empleados: #verificación que el numero de identificación existe
            print("Empleado no registrado")
            return
        else:
            fecha = datetime.now().strftime("%Y-%m-%d") #fecha actual en formato yyyy-mm-dd
            valor = float(input("Ingrese el valor del bono extra legal: "))
            if valor <= 0: # Validación para asegurarse de que la cantidad no sea negativa
                    print("La cantidad no puede ser negativa ni cero. Intente de nuevo.")
                    return
            concepto = input("Ingrese el concepto del bono extra legal: ")
            bonos_empleado = {"id": identificacion, "date": fecha, "value": valor, "concept": concepto}
            registros_bonos_extra.append(bonos_empleado)
            print("Bono extra legales registrado exitosamente")
    except ValueError :
        print("Ingrese una cantidad válida")       

#función menú principal.
def menu (): 
    try:   
        while True:
            print("\nMenú")
            print("1. Registrar empleado")
            print("2. Registrar asistencia")
            print("3. Registrar bonos extra legales")
            print("4. Calcular nomina")
            print("5. Generar reporte por empleado")
            print("0. Salir")
            opcion = int(input("Ingrese su opción: "))
            if opcion == 1:
                registrar_empleado()
            elif opcion == 2:
                registrar_asistencia()
            elif opcion == 3:
                registrar_bonos_extra()
            elif opcion == 4:
                calculo_nomina()
            elif opcion == 5:
                print ("Generar reporte por empleado")
                break
            elif opcion == 0:
                break
    except ValueError : 
        print("Ingrese una opción válida")        
menu()
__name__ == "__main__"  