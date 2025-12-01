# Centinel: El usuario decide cuando salir del programa y no el mismo programa
"""
    Vamos a realizar un programa que sume Pesos mexicanos
    hasta que el ususario escriba la palabra "salir"

    El programa tambien debe decirme cuantos numeros ingreso el usuario,
    cual fue el minimo y cual fue el maximo.

"""
sum_of_numbers = 0.0
counter = 0
minimum = None
maximum = None

while True:
    print("Ingresa la palabra salir para terminar")
    user_input = input("Ingresa una cantidad(MXN):")

    # Centinel
    if user_input == "salir":
        break
    
    try:
        quantity = float(user_input)
    except ValueError:
        print("Cantidad no valida, ingresa nuevamente")
        continue
    except KeyboardInterrupt:
        break
    
    counter = counter + 1 # Estructura contadora, tambien se puede usar counter +=1
    sum_of_numbers = sum_of_numbers + quantity # Estructura acumuladora, pero tambien se puede usar sum_numbers += quantity


    if minimum is None or quantity < minimum:
        minimum = quantity
    
    if maximum is None or quantity < maximum:
        maximum = quantity

print("SUM", sum_of_numbers)
print("CONTADOR", counter)
print("MAXIMO", maximum)
print("MINIMO", minimum)

    