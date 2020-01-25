Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> minEmpleados= 10
>>> minFacturacion= 2
>>> minBalance= 2
>>> 
>>> empleados= 20
>>> facturacion= 18
>>> balance=5
>>> 
>>> esMicroempresa= (empleados<minEmpleados and facturacion <= minFacturacion) or balance <= minBalance
>>> 
>>> print ('es microempresa', esMicroempresa)
es microempresa False
>>> print (type (esMicroempresa))
<class 'bool'>
>>> esPequeñia = not esMicroempresa and (balance <= 10 or empleados <50 and facturacion <=10)
>>> print ('es pequeña', esPequeñia)
es pequeña True
>>> print(type(esPequeñia))
<class 'bool'>
>>> 