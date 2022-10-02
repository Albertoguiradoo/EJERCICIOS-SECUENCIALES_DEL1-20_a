#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente
#desea saber cuanto deberá pagar finalmente por su compra.

from ast import If


productos = 0
producto1 = 0
producto2 = 0
producto3 = 0

productos= (int)(input("(¿Cuántos productos lleva usted en la cesta:\n  ?"))
if (productos=1):
    producto1=(int)(input("¿Cuánto vale el producto 1:\n?"))
print("su comprasería de", (producto1*0.85),"euros con el descuento incluido")
if (productos=2):
    producto1=(int)(input("¿Cuánto vale el producto 1:\n?"))
    producto2=(int)(input("¿Cuánto vale el producto 2:\n?"))
print("su comprasería de", ((producto1+producto2)*0.85),"euros con el descuento incluido")
If (productos=3):
     producto1=(int)(input("¿Cuánto vale el producto 1:\n?"))
    producto2=(int)(input("¿Cuánto vale el producto 2:\n?"))
    producto3=(int)(input("¿Cuánto vale el producto 3:\n?"))
print("su comprasería de", ((producto1+producto2+producto3)*0.85),"euros con el descuento incluido")

