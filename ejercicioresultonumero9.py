print("Calcular del area de un Rectangulo")

largo=int(input("Ingrese la longitud de un Rectangulo:  "))
ancho=int(input("Ingrese el ancho de un Rectangulo: "))

if largo>0 and ancho>0:
	area=(largo*ancho)
	perimetro=(largo+largo+ancho+ancho)
print("El area es:",area)
print("El perimetro es:",perimetro)