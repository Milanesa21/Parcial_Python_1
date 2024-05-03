#Se solicita el ingreso de la primera cadena
cadena1 = input("Ingrese la cadena 1: ")
#Se solicita el ingreso de la segunda cadena
cadena2 = input("Ingrese la cadena 2: ")

#Se crea la funcion para la comparacion de las cadenas, y toma los parametros antes ingresados
def comparar_cadenas_lexicograficas(cadena1, cadena2):
    if cadena1.isdigit() | cadena2.isdigit():
        print("Se debe escribir una cadena de caracteres")
    else:
        #Si la cadena 1 es mayor a la 2 devuelve 1
        if cadena1 > cadena2:
            print("1")
            #Si la cadena 2 es mayor a la 1 devuelve -1
        elif cadena2 > cadena1:
            print("-1")
            #Si ambas cadenas son iguales, devuelve 0
        else:
            print("0")

#Se llama a la funcion y se le pasan los parametros para que retorne el resultado de la cadena
comparar_cadenas_lexicograficas(cadena1, cadena2)