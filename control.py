#Primer programa
#verde = False
#semaforo = 1
#if semaforo == verde:
#    print ("Cruza la calle")
#else:
#    print ("Esperar")
gasto = input ("¿Cuanto gastaste?: ")
gast1 = float(gasto)
totalCompra= gast1

if gast1 < 100 :
    print ("Pago con dinero en efectivo")
elif gast1 > 100 and gast1 < 300 :
    print("Pago con tarjeta de debito ")
else:
    print("Pago con tarjeta de credito")

if gast1 > 100:
    tasaDescuento= 10
    importeDescuento = gast1 * tasaDescuento /100
    importePagar = totalCompra - importeDescuento
    print("Tu total a pagar es :" )
    print(importePagar)
