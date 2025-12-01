# PROBANDO CODIGOS PYTHON
Bloques = ["Tierra", "Piedra", "Roble", "Diamante"]
print(Bloques[0:3])

# QUE MUESTRE SOLO LOS DE ENMEDIO DE 5 OBJETOS DE DERECHA A IZQUIERDA

Bloques = ["Tierra", "Piedra", "Roble", "Diamante", "Adoquin","Arena"]
print(Bloques[-4:-2])

# MODIFICANDO NOMBRES EN LISTAS
name = ["ALES", "JORJE","MAR1A"]
print("NOMBRES ORIGINALES", name)
name[0]="ALEX"
name[1]="JORGE"
name[2]="MARIA"
print("Nombres ya corregidos", name)

print("RANGO DE NUMEROS")
for numbers in range(1,5):
    print(numbers)

print("NUMEROS PARES?")
for odd_numbers in range(2, 12, 2):
    print(odd_numbers)
odd_numbers = list(range(2, 12, 2))
print(odd_numbers)

squares = [num **2 for num in range(11)]
print(squares)

rectangles = [num **2 for num in range(20)]
print(rectangles)


ford_dimensions = (100, 200)
print(f"LARGO: {ford_dimensions[0]}mm")
print(f"ANCHO: {ford_dimensions[1]}mm")

rectangle_dimensions = (200, 50) # Tupla
print(f"largo: {rectangle_dimensions[0]} mm")
print(f"ancho: {rectangle_dimensions[1]} mm")

# TUPLA ORIGINAL
test = (50, 100)
print(f"TESTING: {test[0]} TESTEANDO")
print(f"TESTEANDO: {test[1]} TESTINING")
# NUEVA TUPLA
test = (110, 60)
print(f"NEW GENERATION: {test[0]} MEDINING")
print(f"LA NUEVA MEDIDA: {test[1]} MEDIBLE")

# NUMERO PAR O IMPAR
num = int(input("DAME UN NUMERO"))

if num % 2 == 0:
    print("NUMERO PAR")
else:
    print("NUMERO IMPAR")
































# NUMERO PAR Y IMPAR INTENTANDO IMPLEMENTAR EL TRY Y EXEPT:

try:
    num = int(input("DAME UN NUMERO: "))

    if num % 2 == 0:
        print("NUMERO PAR")
    else:
        print("NUMERO IMPAR")
# OJO SOLO FUNCIONA CON TEXTO COMO A,B,C,D, ETC. SI SON NUMEROS NEGATIVOS FUNCIONAN NORMALMENTE
except ValueError:
    print("INVALID")
