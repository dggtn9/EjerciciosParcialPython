"""Ejercicio 2:
------------

Hacer un programa que determine que tipo de transporte se debe utilizar para transportar mercadería.
El usuario debe ingresar por producto:
- cantidad
    - peso (en kilogramos)

La carga de datos finalizar con una cantidad igual a -1

Si la cantidad de artículos es menor o igual a 10 y el peso total es menor o igual a 100 kg, se debe utilizar una furgoneta.
Si la cantidad de artículos es menor o igual a 20 y el peso total es menor o igual a 500 kg, se debe utilizar un camión.
Para cualquier otro caso, se debe utilizar un transporte de carga.

El programa debe mostrar:
Cantidad total de unidades
Peso total
Transporte a utilizar"""


cant=0
peso_total=0

cantidad=int(input("Ingresa cantidad de articulos"))
while cantidad !=-1:
  cant+=cantidad
  peso=float(input("Ingresar peso en kilogramos"))
  peso_total= peso *cantidad
  cantidad=int(input("Ingresa cantidad de articulos"))
if cant<=10 and peso_total <=100:
    transporte="furgoneta"
elif cant<=20 and peso_total <=500:
    transporte="camion"
else:
    transporte="transporte de carga"

print("Cantidad total de unidades:",cant)
print("Peso total: ",peso_total)
print("Transporte a utilizar",transporte)