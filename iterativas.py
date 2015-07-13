#Ejemplo con bucle while
#año = 2001
#while año <= 2012:
#    print ("Informes del año ", str(año))
#   año += 1
#Aqui se usa un break para frenar la ejecucion cuando el condicional deje de cumplirse
while True: #Este while verifica que la variable sea verdadera
    nombre = input("Indique su nombre: ")
    if nombre: #Si es verdadera el bucle para y va a break
        break
