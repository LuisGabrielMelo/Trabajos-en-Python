print("Impresión de dos Numeros..")
 
numero1=int(input("Escriba el primer Numero: "))
numero2=int(input("Escriba el segundo Numero: "))

if numero1>numero2:
	print("El mayor es %s y el menor es %s" % (str(numero1), str(numero2)))
elif numero1<numero2:
	print("El mayor es %s y el menor es %s" % (str(numero2), str(numero1)))
else:
	print("Los numeros son iguales")