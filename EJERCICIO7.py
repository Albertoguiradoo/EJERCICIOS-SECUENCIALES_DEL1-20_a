#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla
#a cuantas horas y minutos corresponde.Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

minutos = 0

print("vamos a calcular minutos")
minutos= (int) (input("¿Cuántos minutos deseas pasar a horas?:\n "))
print(f"Los {minutos} minutos son: {int (minutos/60)} horas y {int (minutos%60)} minutos")