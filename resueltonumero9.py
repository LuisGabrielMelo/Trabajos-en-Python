print("Elija la figura Geometrica")
print("Elija 1 si quiere triangulo ")
print("Elija 2 si quiere circulo ")

respuesta = float(input("la figura elegida es:" ))

if(respuesta == 1):
  
   base=float(input("Ingrese el valor de la base:" ))
   altura=float(input("Ingrese el valor de la altura: "))
  
   areaT= (base*altura)/2
   print("el area del triangulo es:  " , areaT)
  
elif(respuesta == 2):
  
    radio=float(input("ingrese el valor del radio: "))
    areaC=(3,1416*(radio**2))
    print("El area del circulo es: " , areaC)
