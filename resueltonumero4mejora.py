
añoactual=int(input("Escriba el Año Actual: "))
añocualquiera=int(input("Escriba cualquier Año: "))

while añoactual==añocualquiera:
	print("Error. Por favor introduzca un año diferente")
	añocualquiera=int(input("Escriba Cualquier año: "))
if añoactual>añocualquiera:
	r=añoactual-añocualquiera
	if r==1:
		print("Desde el año %s ha pasado 1 año" % str(añocualquiera))
	else:
		print(u"Desde el año %s ha pasado %s" % str(añocualquiera)) , str(r)
elif añoactual<añocualquiera:
	r=añocualquiera-añocualquiera
	if r==1:
		print("Para llegar al año %s falta 1 año" % str(añocualquiera))
	else:
		print("Para llegar al %s falta %s" % (str(añocualquiera) , str(r)))
 		
		