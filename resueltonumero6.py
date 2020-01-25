print("Numeros Iguales")

numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))
numero3=int(input("Ingrese el tercer numero: "))

if numero1==numero2==numero3:
	print("Los Tres numeros son iguales")
elif numero1==numero2 or numero1==numero3 or numero2==numero3:
		print("Hay dos numeros que son iguales")
else:
	 print("Los tres numeros son distintos")
