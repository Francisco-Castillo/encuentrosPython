#   ===========================================================================
#   *************************** Enunciado 1 ***********************************
#   Leer un número, determinar y mostrar, el número ingresado, el anterior y el
#   siguiente
#   ===========================================================================

def pedir_numero():
    numero = int(input("Ingrese un numero: "))
    return numero

numero_actual = pedir_numero()
numero_anterior=numero_actual-1
numero_posterior=numero_actual+1
#   Imprimimos los resultados
print("\n=======================SECUENCIA RESULTANTE===========================")
print("\n",numero_anterior,numero_actual,numero_posterior, sep="\n",end="\n\n")

#   ===========================================================================
#   *************************** Enunciado 2 ***********************************
#   Leer la base y la altura de un triángulo, calcular y mostrar la superficie
#   del mismo
#   ===========================================================================
