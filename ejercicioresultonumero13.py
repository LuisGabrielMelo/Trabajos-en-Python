print("Calcular Salario")

ventas= int and float(input("Ingrese la suma obtenida por ventas del mes: "))
if ventas >0:
	salario= 2000
	salario= (salario + (ventas * 3) / 100)
	salarioneto= (salario -  (salario *32) / 100)
print ("Salario neto: $", salarioneto)