#Un alumno desea saber cual será su calificación final en la materia de Algoritmos.  
#  55% del promedio de sus tres calificaciones parciales. 
#  30% de la calificación del examen final.
#  15% de la calificación de un trabajo final.

nota1 = 0
nota2 = 0
nota3 = 0
print("Vamos a calcular tu nota de final de curso")
nota1= (int)(input("Dime tu nota del primer trimestre:\n "))
nota2= (int)(input("Dime tu nota del segundo trimestre:\n "))
nota3= (int)(input("Dime tu nota del tercer trimestre:\n "))
print("tu nota final es de una calificación de: ", (nota1*0.55+nota2*0.3+nota3*0.15))