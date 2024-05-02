"""3) Un estudio contable procesa la facturación de 10 empresas diferentes. 
Por cada una se procesan los comprobantes ingresando 
importe
 total de la factura - importe real mayor a cero - y tipo de comprobante siendo ‘A’ para factura tipo A y tipo de comprobante ‘B’
para factura tipo B. 

El ingreso de comprobantes por empresa finaliza con el ingreso de tipo de comprobante igual a ‘F’
Se desea conocer el importe de facturación total por empresa y la cantidad de comprobantes de tipo A y de tipo B.
Al final informe la cantidad de comprobantes totales procesados para el total de las empresas."""


cant_a=0
cant_b=0
total=0

tipo_de_comprobante=input("Ingrese A,B o F para terminar: ")
while tipo_de_comprobante !='A' and tipo_de_comprobante!='B' and tipo_de_comprobante !='F' :    
    
    tipo_de_comprobante=input("Ingrese A,B o F para terminar: ")

while tipo_de_comprobante !='F':

        if tipo_de_comprobante == 'A':
             cant_a+=1
        else:
             cant_b+=1
        
        importe=float(input("Ingrese importe total: "))

        while importe <=0:

            importe=float(input("Ingrese importe total: "))
        
        total+=importe
        
        tipo_de_comprobante=input("Ingrese A,B F para terminar: ")

        while tipo_de_comprobante !='A' and tipo_de_comprobante!='B'and tipo_de_comprobante !='F' :    

            tipo_de_comprobante=input("Ingrese A,B ")

print("Importe de facturación total por empresa: ",total)
print("cantidad de comprobantes de tipo A y de tipo B: ",cant_a)
print("cantidad de comprobantes de tipo A y de tipo B: ",cant_b)
print("Cantidad de comprobantes totales procesados para el total de las empresas: ",cant_a+cant_b)