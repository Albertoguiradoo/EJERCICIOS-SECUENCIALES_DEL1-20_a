def ejercicio1():
    nombre = ""

    print("Hola")
    nombre= input ("dime tu nombre:\n ")
    print("Hola", nombre)

def ejercicio2():
    altura = 0
    lado = 0


    print("Vamos a calcular el perimetro del rectángulo.")
    lado= (int)(input("Dime la distancia del lado :\n "))
    altura= (int)(input("Dime la distancia de la altura :\n "))
    print("-El perimetro del rectángulo es:", (2*lado +2*altura))
    print("-Vamos a calcular el area del rectángulo:")
    print("El area del rectángulo es:", (lado*altura), "metros")
