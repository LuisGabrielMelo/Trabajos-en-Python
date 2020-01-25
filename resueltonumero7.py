print("Año Bisiesto")

añob=int(input("Ingrese un Año Bisiesto: "))
if (añob%4==0 and añob%100!=0) or añob%400==0:
	print("El año %s es Bisiesto" % str(añob))
else:
	print("El año %s no es Bisiesto" % str(añob))