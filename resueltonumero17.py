mayor= int(2)
b= "V"

numero= int(input("Porfavor Ingrese un Numero : "))

while((b=="V") and (mayor < numero)):
	if ((numero%mayor)==0):

		band= "F"

	else:
		mayor=mayor+1

if (b=="V"):
	print("El numero  es primo")

else:
	print("El numero No es primo")