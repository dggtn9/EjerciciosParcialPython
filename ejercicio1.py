"""Pedir por teclado números enteros. El ingreso finaliza con un número negativo.
Determinar:
1) La cantidad de números que se ingresaron
2) La cantidad de números ingresados que son múltiplos de 5
3) El mayor número
4) El menor número

Bonus: Determinar la seguidilla mas larga de números repetidos y mostrar también cual fue el número.

Ejemplo:
Si el usuario ingresa
1 3 7 7 8 1 -5

La seguidilla mas larga fue 2 para el número 7

Otro ejemplo:
Si el usuario ingresa:
1 2 9 6 6 8 7 6 6 5 5 5 5 2 3 11 11 11 10 -100

La seguidilla mas larga fue 4 para el número 5

Caso borde:
Si el usuario ingresa
11 2 3 4 5 7 9 8 -10

La seguidilla mas larga fue 1 para el número 11

"""

numero=int(input("Ingresar numeros enteros: "))
cant=0
cant_mult5=0
numero_mayor=0
numero_menor=0
cant_veces_repetidas=1
valor_mayor_seguidilla=1

while numero >0:
    cant+=1
    if cant == 1:
        numero_mayor=numero
        numero_menor=numero
        primer_numero=numero
        numero_mayor_seguidilla=numero
    else:
        if numero_mayor < numero:
            numero_mayor=numero
        if numero_menor > numero:
            numero_menor=numero
        if primer_numero == numero:
            cant_veces_repetidas+=1  
        else:
            if cant_veces_repetidas>valor_mayor_seguidilla:
                valor_mayor_seguidilla=cant_veces_repetidas
                numero_mayor_seguidilla=primer_numero
            primer_numero = numero
            cant_veces_repetidas=1
    if numero%5==0:
        cant_mult5+=1
    numero=int(input("Ingresar numeros enteros: "))
if cant_veces_repetidas>valor_mayor_seguidilla:
                valor_mayor_seguidilla=cant_veces_repetidas
                numero_mayor_seguidilla=primer_numero
print("La cantidad de números que se ingresaron: ",cant)
print("La cantidad de números ingresados que son múltiplos de 5: ",cant_mult5)
print("El mayor número: ",numero_mayor)
print("El menor número: ",numero_menor)
print("El  número que se repite: ",numero_mayor_seguidilla)
print("veces que se repite : ",valor_mayor_seguidilla)