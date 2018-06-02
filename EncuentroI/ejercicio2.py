#   ===========================================================================
#   *************************** Enunciado 2 ***********************************
#   Leer la base y la altura de un triángulo, calcular y mostrar la superficie
#   del mismo
#   ===========================================================================

#   Definimos una funcion para realizar el calculo
def calcula_superficie(base,altura):
    return ((base * altura)/2)


#   Solicitamos al usuario que ingrese los datos
base=int(input("Ingrese la base: "))
altura=int(input("Ingrese la altura: "))
#   Invocamosa la funcion y mostramos resultados
print("\n====================== SUPERFICE DEL TRIÁNGULO =========================")
print("\nLa superficie del triángulo es de : ",calcula_superficie(base,altura),"\n")
