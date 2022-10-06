#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)
#Después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20céntimos o 10 céntimos).

moneda2 = 0
moneda1 = 0
cent50 = 0
cent20 = 0
cent10 = 0

moneda2= int(input("DIme cuantas monedas de dos euros tienes: \n"))
moneda1= int(input("DIme cuantas monedas de un euro tienes: \n"))
cent50= int(input("DIme cuantas monedas de 50 céntimos tienes: \n"))
cent20= int(input("DIme cuantas monedas de 20 céntimos tienes: \n"))
cent10= int(input("DIme cuantas monedas de 10 céntimos tienes: \n"))

print("Tienes un total de: ", (moneda2*2+moneda1*1+cent50*0.5+cent20*0.2+cent10*0.1), "euros")
print("Tienes un  total de:", (moneda2*200+moneda1*100+cent50*50+cent20*20+cent10*10), "céntimos")