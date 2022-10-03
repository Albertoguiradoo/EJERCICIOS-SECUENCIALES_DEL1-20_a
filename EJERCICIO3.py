#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
import math
cateto1 = 0
cateto2 = 0

print("vamos a calcular la hipotenusa de un triángulo")
cateto1= (int) (input ("dime la distanciad del primer cateto: \n"))
cateto2= (int) (input ("dime la distancia del segundo cateto: \n"))
print("la hipotenusa del triángulo es:", (math.sqrt(cateto1*cateto1+cateto2*cateto2)))
 