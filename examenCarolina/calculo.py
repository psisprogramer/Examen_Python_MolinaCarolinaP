from main import registros_empleados, registros_empleados_asistencia, registros_bonos_extra

#Función para calcular la nomina          
def calculo_nomina():
    identificacion = input("Ingrese el numero de identificación del empleado: ")
    if identificacion not in registros_empleados:
        print("Empleado no registrado")
        return
    
    salario = registros_empleados[identificacion]['salary']
    print(f"Su salario base es {salario}")

    # Calcular faltas
    faltas = registros_empleados_asistencia.get(identificacion, {}).values()
    if faltas > 0:
        total_faltas = sum(faltas) 
    else:
        total_faltas = 0
        return total_faltas
    # print(f"Total de faltas: {total_faltas}")
    #Descuento por faltas
    salario_descuento_faltas = total_faltas * (salario / 30)  # Un día de trabajo, considerando 30 días en un mes


    #Descuento por transporte
    if salario >= 2000000:
        salario_descuento_transporte = salario * 0.10
    else:
        salario_descuento_transporte = 0
    #Descuento por salud
        salario_descuento_salud = salario * 0.04
    #Descuento por pension
        salario_descuento_pension = salario * 0.04
    

    # Calculo de bonos extra legales
    bonos_extra_total = sum(bono["value"] for bono in registros_bonos_extra if bono["id"] == identificacion)
    
    # Calculo total
    total_descuentos = salario_descuento_transporte + salario_descuento_salud + salario_descuento_pension + salario_descuento_faltas
    salario_neto = salario + bonos_extra_total - total_descuentos

    print(f"Total de descuentos: {total_descuentos}")
    print(f"Bonos extra legales: {bonos_extra_total}")
    print(f"Salario neto: {salario_neto}")
