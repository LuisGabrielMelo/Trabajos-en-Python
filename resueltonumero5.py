print("Numeros Enteros...")

numero1=int(input("Ingrese el Primer Numero: "))
numero2=int(input("Ingrese el Segundo Numero: "))

if numero1>numero2:
	multiplo=numero1%numero2
	if multiplo==0:
		print("El Mayor es %s y es multiplo de %s" %(str(numero1), str(numero2)))
	else:
		print("El mayor es %s y no es multiplo de %s" % (str(numero1),str(numero2)))
elif numero1<numero2:
	multiplo=numero2%numero1
	if multiplo==0:
		print("El mayor es %s y es multiplo de %s" % (str(numero2) , str (numero1)))
	else:
			print("El Mayor es %s y no es multiplo de %s" % (str(numero2), str(numero1)))
else:
		print("Los numeros son iguales")				
