print("Divisores de un Numero")

numero=int(input("Escriba un Numero Mayor Que Cero: "))


s=""
contadord=0

for n in range(1,numero+1):
	if (numero%n==0):
		s=s + "," + str(n)
		contadord=contadord+1
print("Los Divisores de %s son %s" % (str(numero),str(s)))