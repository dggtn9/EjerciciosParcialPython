"""
2) Desarrolle un algoritmo para la empresa LA ESTRELLA S.A., que le permita calcular e imprimir el sueldo a abonar por cada empleado.
 El valor actual de la hora es de $3000.
Por cada empleado se ingresa el legajo (número entero en el rango 5000-30000) y la cantidad de horas trabajadas (mayor a 0) y 
antigüedad (mayor o igual a 0). Se debe validar el ingreso de los datos."""

"""El ingreso de los datos finaliza con el número de legajo 99."""

"""Si la antigüedad es mayor a 5 años el empleado cobra un adicional del 12%. 
Calcular e informar por cada empleado el sueldo a abonar 
 y el sueldo promedio que abona la empresa. (4 PUNTOS)"""

valor_hora=3000
total_sueldos_con_adicional=0
total_sueldos_sin_adicional=0
empleados=0
sumatoria_sueldos=0

legajo=int(input("Ingrese numero de legajo"))
while legajo<5000 or legajo >30000:
      legajo=int(input("Ingrese numero de legajo"))

while legajo !=99:
    empleados+=1
    horas_trabajadas = int(input("Ingresa horas trabajadas")) 
    while horas_trabajadas <0:
        horas_trabajadas = int(input("Ingresa horas trabajadas")) 

    antiguedad=int(input("Antiguedad"))
    while antiguedad<0:
        antiguedad=int(input("Antiguedad"))
    sueldo=horas_trabajadas*valor_hora    
    if antiguedad>5:
        sueldo+=(sueldo*0.12)
    print("Sueldo a abonar es: ",sueldo)
    legajo=int(input("Ingrese numero de legajo"))
    sumatoria_sueldos+=sueldo
    while legajo<5000 or legajo <30000:
      legajo=int(input("Ingrese numero de legajo"))

sueldo_promedio=sumatoria_sueldos/empleados