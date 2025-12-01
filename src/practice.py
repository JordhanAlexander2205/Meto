# practicar centinel
sum_of_numbers = 0
counter = 0
maximum = None
minimum = None

while True:
    print("Para terminar el programa escribe salir")
    user_input = input("Dime una cantidad de dinero: ")

    if user_input == "salir":
        break
    
    try:
        quantity = float(user_input)
    except ValueError:
        print("NO ES VALIDO, INGRESE DE NUEVO POR FAVOR")
        continue
    except KeyboardInterrupt:
        break

    counter += 1
    sum_of_numbers = sum_of_numbers + quantity


    if minimum is None or quantity < minimum:
        minimum = quantity
    if maximum is None or quantity < maximum:
        maximum = quantity


print("SUMA", sum_of_numbers)
print("CANTIDAD", quantity)
print("MAXIMO", maximum)
print("MINIMO", minimum)