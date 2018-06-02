#   ===========================================================================
#   *************************** Enunciado 3 ***********************************
#   Leer un número entero, determinar si el mismo es Par o Impar.
#   ===========================================================================


def es_par(numero):
    #if numero%2==0:
    #    return True
    #else:
    #    return False
    return numero%2==0

# Solicitamos datos
x = int(input("Por favor ingrese un numero: "))

print("Es par ? : ",es_par(x))
