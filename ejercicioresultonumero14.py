print("Cambio de dolares a Pesos")

pesos=int and float(input("Ingrese cantidad de pesos a convertir: "))
dolar=int and float(input("Ingrese valor del dolar: "))

if pesos>0 and dolar>0:
	usd=(dolar*pesos)
	print(pesos,"Pesos =",usd,"Dolares")
else:
	print("El valor ingresado no es correcto")