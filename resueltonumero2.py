print("Division de Numeros Enteros")

numero1=int(input("Escriba el primer numero: "))
numero2=int(input("Escriba el segundo numero: "))
division=(numero1/numero2)
resultado=(numero1%numero2)

if resultado==0:
	print("La Division es exacta. El Resultado es: cociente= %s" % str(division))
else:
	print("La Division no es exacta. El Resultado es: cociente= %s y el resto= %s" % (str(division),str(resultado)))