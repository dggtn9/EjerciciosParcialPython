"""2) Se solicita al usuario el ingreso de la cantidad de empleados que desea procesar. Luego se ingresan los legajos de 
cada empleado y sus correspondientes sueldos (mayores a cero – VALIDAR EL INGRESO DE ESTE DATO). 
Indicar el nombre del empleado con el sueldo más alto y el del más bajo. Aclaración: todos los empleados
 tienen sueldos distintos."""

cant=0
cantidad_empleados_a_procesar=int(input("Ingrese cantidad de empleados a procesar"))

for i in range (cantidad_empleados_a_procesar):
    cant+=1
    legajo=int(input("Ingrese legajo"))
    sueldo=float(input("Ingrese sueldo"))
    while sueldo<0:
        sueldo=float(input("Ingrese sueldo"))

    if cant==1:
        legajo_sueldo_mas_alto=legajo
        legajo_sueldo_mas_bajo=legajo
        sueldo_mas_alto=sueldo
        sueldo_mas_bajo=sueldo
    else:
        if sueldo>sueldo_mas_alto:
            sueldo_mas_alto=sueldo
            legajo_sueldo_mas_alto=legajo
        if sueldo<sueldo_mas_bajo:
            sueldo_mas_bajo=sueldo
            legajo_sueldo_mas_bajo=legajo

print("legajo con el sueldo mas alto: ",legajo_sueldo_mas_alto)
print("legajo con el sueldo mas bajo: ",legajo_sueldo_mas_bajo)
