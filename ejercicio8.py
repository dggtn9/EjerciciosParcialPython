"""3) Se desea calcular e imprimir la tabla de multiplicar de un número entero mayor a 0 ingresado por el usuario
 (validar este dato), pero solo para los productos que son divisibles por 5,
 mientras el cálculo obtenido sea menor a 600"""

i=1
numero=int(input("Ingresa numero"))
while numero<0:
    numero=int(input("Ingresa numero"))
resultado=0
while resultado<600 :
    resultado=numero*i
    i+=1
    if resultado%5==0:
        print(resultado)



