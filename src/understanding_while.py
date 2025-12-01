"""
     Docstring for understanding_while_loop_104

     Utilizamos el while loop para ejecutar un bloque de codigo mientras una condicion
     sea verdadera.

     Estructura basica del while loop en Python

        while condicion:
            # Bloque de codigo a ejecutar

"""

# Ejemplo basico de un while loop
# Verificar si un numero esta en un rango especifico
# Rango (10 y entre 20)

while True: # While loop infinito
    try:
        number = int(input("Ingrese un numero entre el 10 y el 20: "))

        if number < 20 and number > 10:
            print("Numero dentro del rango, Felicidades.")
            break

        else:
            print("Numero fuera del rango, Intentalo de nuevo.")
    except ValueError:
        print("Entrada Invalida, Por favor ingrese un numero entero.")
    
    except KeyboardInterrupt:
        print("\n Programa terminado por el usuario.")
        break

print("Saliste del While yupi")

# Otra manera:

while True: # While loop infinito
    
        number_string  =input("Ingrese un numero entre el 10 y el 20: ")

         if number_string.isdigit():
            number = int(number_string)
            if number < 20 and number > 10:
                print("Numero dentro del rango, Felicidades.")
                break

            else:
                print("Numero fuera del rango, Intentalo de nuevo.")
        else:
            print("Entrada Invalida, Por favor ingrese un numero entero.")
    
    except KeyboardInterrupt:
        print("\n Programa terminado por el usuario.")
        break

print("Saliste del While yupi")



