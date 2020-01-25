print("Año Actual...")
añoactual=int(input("Ingrese el actual: "))
añocualquiera=int(input("Ingrese cualquier año: "))


if añoactual>añocualquiera:
	r=añocualquiera-añoactual
	print("Desde el año %s han pasado %s" %(str(añocualquiera), str(r)))

elif añoactual<añocualquiera:
	r=añocualquiera-añoactual
	print("Para llegar al %s faltan %s" % (str(añocualquiera), str(añoactual)))
else:
	print("Los años son Iguales")	

