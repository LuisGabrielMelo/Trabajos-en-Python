print("Calculadora de impuesto anual ")

ingresos_anuales=int(input("Ingrese sus ingresos porfavor:"))
cantidad_hijos=int(input("Ingrese la cantidad de hijos: "))

if cantidad_hijos>0:
	deduccion_x_hijos=(60*cantidad_hijos)
	ingreso=(ingresos_anuales-deduccion_x_hijos-(600))
	impuesto_x_años=(ingreso/3)
else:
	ingreso=(ingresos_anuales-(600))
	impuesto_x_años=(ingreso/3)
print("Tus impuestos son:", impuesto_x_años)