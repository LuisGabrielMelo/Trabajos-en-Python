numero=int(input("Cuantos numeros desea Introducir: "))

if numero>0:
	pares=0
	impares=0
	for i in range(numero):
		print(i)
	
		pares=int(input("Ingrese un numero par: "))

		impares=int(input("Ingrese un numero impar: "))
		print("La cantidad de numeros pares fue: ",pares, "\nLa cantidad de impares fue: " ,impares )	
	
else:
			print("El control de numeros finalizado")
	