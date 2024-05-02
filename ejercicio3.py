"""1) Desarrolle un algoritmo que permita calcular e informar la edad máxima y mínima de un lote de edad que se 
ingresa de 500 personas. 

Informar por cada persona si es mayor de edad (edad mayor o igual a 18) o si es menor de edad (edad menor a 18). (2 PUNTOS)"""

cant=0
edad=int(input("ingrese su edad: "))
for i in range(9):
    cant+=1
    if cant==1:
           edad_maxima=edad
           edad_minima=edad
    else:
           if edad_maxima<edad:
                  edad_maxima=edad
           if edad_minima>edad:
                  edad_minima=edad 
    if edad>=18:
            print("La persona es mayor de edad: ")
    else:
            print("La persona es menor de edad: ")

    edad=int(input("ingrese su edad: "))
 
print("Edad maxima: ",edad_maxima)
print("Edad minima: ",edad_minima)


      
       








