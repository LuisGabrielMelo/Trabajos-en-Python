print("Ecuaciones...")

a=int(input("Escriba el primer Valor de A: "))
b=int(input("Escriba el segundo Valor de B: "))

if a==0 and b!=0:
	print("La Ecuacion no tiene Solucion")
elif a==0 and b==0:
	print("Todos los numeros son iguales")

else:
	incognita=-b/a
	print("El Valor de x= %s " % str(incognita))