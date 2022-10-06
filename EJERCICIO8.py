#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas,.

sueldo = 0
venta1 = 0
venta2 = 0
venta3 = 0

print("Vamos a calcular tu sueldo con el 10% extra")

sueldo= int(input("Dime cuanto cobras:\n "))
venta1 = int(input("Dime cuanto ganastes con tu primera venta:\n "))
venta2= int(input("Dime cuanto ganastes con tu segunda venta:\n "))
venta3= int(input("Dime cuanto ganastes con tu tercera venta:\n "))

print(" Tus ganancias obtenidas con las ventas es de:" ,int((venta1+venta2+venta3)*0.1), "euros")
print(" Tu sueldo con los extras es de un total de",int(((venta1+venta2+venta3)*0.1)+sueldo), "euros")