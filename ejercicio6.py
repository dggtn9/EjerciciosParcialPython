"""Un centro de atención telefónica de soporte técnico desea realizar un informe de los tiempos de atención de sus empleados. 
Por cada empleado se ingresa el número de identificación (legajo), el tiempo de atención en minutos
 (mayor a cero – VALIDAR EL INGRESO DE ESTE DATO) y la categoría del empleado (S = Senior, J = Junior y T = Trainee). """
"""El programa iniciará preguntando el ingreso por teclado de la categoría del empleado, 
pudiendo finalizar la ejecución mediante la letra F en dicho ingreso de dato. Se desea conocer:

A) El promedio de tiempo de atención por categoría de empleado.
B) El número de identificación del empleado con el tiempo de atención más alto y el del más bajo. 

Aclaración: todos los empleados tienen tiempos de atención distintos.
"""

tiempo_s=0
tiempo_j=0
tiempo_t=0
cant=0

categoria=input("categoría del empleado (S = Senior, J = Junior y T = Trainee)")
while categoria!='F':
    legajo=input("Ingresa legajo")
    tiempo_atencion=int(input("ingrese tiempo de atencion en minutos"))
    while tiempo_atencion<0:
       tiempo_atencion=int(input("ingrese tiempo de atencion en minutos"))  
    cant+=1
    if cant==1:
        legajo_tiempo_mas_atencion=legajo
        legajo_tiempo_menos_atencion=legajo
        tiempo_mas_atencion=tiempo_atencion
        tiempo_menos_atencion=tiempo_atencion
    else:
        if  tiempo_atencion>tiempo_mas_atencion:
             tiempo_mas_atencion=tiempo_atencion
             legajo_tiempo_mas_atencion=legajo

        if  tiempo_atencion<tiempo_menos_atencion:
             tiempo_menos_atencion=tiempo_atencion
             legajo_tiempo_menos_atencion=legajo

    if categoria == 'S':
        tiempo_s+=tiempo_atencion
    elif categoria == 'J':
        tiempo_j+=tiempo_atencion
    elif categoria == 'T':
        tiempo_t+=tiempo_atencion
    categoria=input("categoría del empleado (S = Senior, J = Junior y T = Trainee)")


tiempo_total=(tiempo_s+tiempo_t+tiempo_j)
promedio_t=tiempo_t/tiempo_total
promedio_j=tiempo_j/tiempo_total
promedio_s=tiempo_s/tiempo_total


print("Promedio T ",promedio_t)
print("Promedio J ",promedio_j)
print("Promedio S ",promedio_s)
print("El número de identificación del empleado con el tiempo de atención más alto: ",legajo_tiempo_mas_atencion)
print("El número de identificación del empleado con el tiempo de atención menos alto: ",legajo_tiempo_menos_atencion)








