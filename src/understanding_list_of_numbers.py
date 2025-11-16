"""
 las listas tambien pueden almacenar numeros y de hecho
 son ideales para almacenarlos.
 Python ofrece cantidad de funciones integradas para trabajar con listas de numeros

 Por ejemplo, podemos usar la funcion range():

"""

# La funcion range() gener una lista de numeros en un rango especifico.
# Por ejemplo, numero del 0 al 9
numeros = list(range(10)) # List para tipo lista
print(numeros) # Salida de los numeros
print(type(numeros)) # Salida tipo type

# Podemos realizat lo mismo con un for Loop:
for num in range(10):
    print(num)
   # print(type(num)) # Salida <class "int">

print("Numeros del 1 al 4:")
for num in range(1,5):
    print(num)

numbers_1_to_4 = list(range(1, 5))
print(numbers_1_to_4)

print("Numeros Impares:")
for num in range(1, 10, 2): # Numeros impares del 1 al 9
    print(num)
odd_numbers = list(range(1, 10, 2))
print(odd_numbers) # Lo mismo pero en lista

print("Numeros Pares:")
for num in range(2, 10, 2): # Numeros pares de 2 al 8
    print(num)
even_numbers = list(range(2, 10, 2))
print(even_numbers) # Lo mismo pero en lista

## Podemos crear cualquier tipo de listas de numeros
## Utilizando range() y list()
print("\n Primeros 10 numeros al cuadrado: ")
squares = []
for values in range(1, 11):
    square = values ** 2 # Elevar al cuadrado
    squares.append(square)
print(squares) # Salida: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Metodo built-in para listas de numeros
print("\n Metodos built-in para listas de numeros:")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"Lista de digitos: {digits}")
print("Valor minimo:", min(digits)) # Salida: 0
print("Valor maximo:", max(digits)) # Salida: 9
print("Suma de todos los digitos:", sum(digits)) # Salida 45:

digits = [0, 1, 2 ,3 , 4, 5, 6, 7, 8, 9]
squares = []
for num in digits:
    square = num ** 2
    squares.append(square)
print(square)

# List comprenhensions
squares = [num **2 for num in range(11)]
print(squares)