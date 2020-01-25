numeros=int(input("Cuantos Numeros Desea Introducir: "))


if numeros>0:
		print("Exelente..")
		negativos=0
		for i in range(numeros):
			print(i)
			dato =int(input("Ingrese un Numero Negativo: "))

			if dato <0:
				negativos +=1
			print("La cantidad de numeros negativos fue: ",negativos)
		
else:

		print("El numero ingresado no es correcto..")


