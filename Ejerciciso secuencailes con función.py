import math


def ejercicio1(nombre:str):
    print("-Ejercicio1\n")
    print("Hola", nombre)

ejercicio1("Alberto.\n")

def ejercicio2(altura:int,lado:int):
    print("-Ejercicio2\n")
    print("Vamos a calcular el perimetro del rectángulo.")
    print("-El perimetro del rectángulo es:", (2*lado +2*altura))
    print("-Vamos a calcular el area del rectángulo:")
    print("El area del rectángulo es:", (lado*altura), "metros")

ejercicio2(2,3)

def ejercicio3(cateto1:int,cateto2:int):
    print("-Ejercicio3\n")
    print("vamos a calcular la hipotenusa de un triángulo")
    print("la hipotenusa del triángulo es:", (math.sqrt(cateto1*cateto1+cateto2*cateto2)))

ejercicio3(5,6)

def ejercicio4(num1:int,num2:int):
    print("-Ejercicio4\n")
    print("Vamos a sumar dos números")
    print("la suma es:", (num1+num2))
    print("Ahora, vamos a restar: ", (num1-num2))
    print("Ahora, vamos a multiplicar los dos números: ", (num1*num2))
    print("Ahora, vamos a dividir los dos números: ", (num1/num2))

ejercicio4(2,3)

def ejercicio5(Fahrenheit:int):
    print("-Ejercicio5\n")
    print("vamos a pasar de Fahrenheit a grados")
    print("En grados sería: ", (Fahrenheit-32)*5/9)  
ejercicio5(298)

def ejercicio6(numero1:int,numero2:int,numero3:int):
    print("-Ejercicio6\n")
    print("Vamos a hacer la media de tres números pedidos por teclado")
    print("la media de los tres es:", int((numero1+numero2+numero3)/3))
ejercicio6(2,3,4)

def ejercicio7(minutos:int):
    print("-Ejercicio7\n")
    print("vamos a calcular minutos")
    print(f"Los {minutos} minutos son: {int (minutos/60)} horas y {int (minutos%60)} minutos")
ejercicio7(125)

def ejercicio8(sueldo:int,venta1:int,venta2:int,venta3:int):
    print("-Ejercicio8\n")
    print("Vamos a calcular tu sueldo con el 10% extra")
    print(" Tus ganancias obtenidas con las ventas es de:" ,int((venta1+venta2+venta3)*0.1), "euros")
    print(" Tu sueldo con los extras es de un total de",int(((venta1+venta2+venta3)*0.1)+sueldo), "euros")
ejercicio8(1200,100,200,300)

def ejercicio9(compra:int):
    print("-Ejercicio9\n")
    print("Su compra con el descuento del 15% es de",(compra*0.85), "euros")
ejercicio9(12330)

def ejercicio10(nota1:int,nota2:int,nota3:int,examen:int,trabajo:int):
    print("-Ejercicio10\n")
    print("Vamos a calcular tu nota de final de curso")
    print("tu nota final es de una calificación de: ",(((nota1+nota2+nota3)/3)*0.55)+examen*0.3+trabajo*0.15)
ejercicio10(10,8,7,10,10)

def ejercicio20(moneda2:int,moneda1:int,cent50:int,cent20:int,cent10:int):
    print("-Ejercicio20\n")
    print("Tienes un total de: ", (moneda2*2+moneda1*1+cent50*0.5+cent20*0.2+cent10*0.1), "euros")
    print("Tienes un  total de:", (moneda2*200+moneda1*100+cent50*50+cent20*20+cent10*10), "céntimos")

ejercicio20(2,4,8,5,10)