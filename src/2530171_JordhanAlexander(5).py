# Manejo de funciones en Python
"""
METODOLOGIAS DE LA PROGRAMACION:
    MAESTRO: CARLOS ANTONIO TOVAR GARCIA
        CARRERA: MECATRONICA
        ALUMNO: JORDHAN ALEXANDER MARIANO RAMIREZ
        MATRICULA: 2530171
"""
# Resumen Ejecutivo:
"""
- ¿Qué es una función en Python y para qué sirve?
Se refiere a un conjunto de instrucciones agrupadas bajo un nombre.

- ¿Qué diferencia hay entre parámetros (definition) y argumentos (call)?
Los PARAMETROS Son los nombres que aparecen cuando se define la función,
representan las variables que la función usara.
Ejemplo:
def sumar(a, b):   # a y b son PARÁMETROS
    return a + b


Los ARGUMENTOS Son los valores reales que se pasa a la función cuando es llamada.
Ejemplo:
resultado = sumar(3, 5)  # El 3 y 5 son ARGUMENTOS

- ¿Por qué es útil separar la lógica en funciones reutilizables?
Nos da multiples ventajas, entre ellas destacan:
    -No tener la necesidad de declarar variables duplicadas, si se necesita utilizar solo es llamada.
    -Mantiene el codigo del programa mas limpio y organizado, ademas es mas facil de leer.
    -Se le puede dar un mejor mantenimiento y agregar nuevos elementos.
    -Evita errores y tambien resulta mas sencillo resolverlos si es que los hay.
- ¿Qué es un valor de retorno y por qué es mejor devolver resultados en lugar de solo imprimirlos?
Un valor de retorno es el resultado que una función entrega cuando esta termina de ejecutarse.
En Python se utiliza la palabra clave "return".

Ejemplo:
def sumar(a, b):
    return a + b

# a y b son parte de retorno del mismo codigo.
"""

# PROBLEMAS
# Problem 1: Rectangle area and perimeter (basic functions)
def calculate_area(width, height):
    return width * height


def calculate_perimeter(width, height):
    return 2 * (width + height)


def main_program(width_text: str, height_text: str):
    # Intentar convertir a float
    try:
        width = float(width_text)
        height = float(height_text)
    except ValueError:
        print("Error: invalid input")
        return

    # Validar rango
    if width <= 0 or height <= 0:
        print("Error: invalid input")
        return

    # Llamar funciones
    area = calculate_area(width, height)
    perimeter = calculate_perimeter(width, height)

    print("Area:", area)
    print("Perimeter:", perimeter)
# CASO USO:
# CORRECTO
"""
width = 5
height = 3

Salida Esperada:
Area: 15.0
Perimeter: 16.0

"""

# BORDE
"""
width = 0.1
height = 0.1

Salida Esperada:
Area: 0.010000000000000002
Perimeter: 0.2

"""

# ERROR
"""
width = hola
height = 10

Salida Esperada:
Error: invalid input

"""

# Problem 2: Grade classifier (function with return string)
def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main_program(score_text: str):
    # Validar conversión
    try:
        score = float(score_text)
    except ValueError:
        print("Error: invalid input")
        return

    # Validar rango
    if score < 0 or score > 100:
        print("Error: invalid input")
        return

    # Clasificar
    category = classify_grade(score)

    print("Score:", score)
    print("Category:", category)
# CASO USO:
# CORRECTO
"""
95
Salida Esperada:
Score: 95.0
Category: A

"""

# BORDE
"""
80
Salida Esperada:
Score: 80.0
Category: B

"""

# ERROR
"""
150
Salida Esperada:
Error: invalid input

"""

# Problem 3: List statistics function (min, max, average)
def summarize_numbers(numbers_list):
    summary = {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }
    return summary


def main_program(numbers_text: str):
    # Validar texto no vacío
    if not numbers_text.strip():
        print("Error: invalid input")
        return

    parts = numbers_text.split(",")

    # Intentar convertir cada elemento a número
    numbers_list = []
    for item in parts:
        item = item.strip()
        if not item:  # evita elementos vacíos como "10,,20"
            print("Error: invalid input")
            return
        try:
            num = float(item)
        except ValueError:
            print("Error: invalid input")
            return
        numbers_list.append(num)

    # Validar lista no vacía
    if len(numbers_list) == 0:
        print("Error: invalid input")
        return

    # Obtener resultados
    result = summarize_numbers(numbers_list)

    print("Min:", result["min"])
    print("Max:", result["max"])
    print("Average:", result["average"])
# CASO USO:
# CORRECTO
"""
10, 20, 30, 40

Salida Esperada:
Min: 10.0
Max: 40.0
Average: 25.0

"""

# BORDE
"""
15
Salida Esperada:
Min: 15.0
Max: 15.0
Average: 15.0

"""

# ERROR
"""
10, , 20

Salida Esperada:
Error: invalid input

"""

# Problem 4: Apply discount list (pure function)
def apply_discount(prices_list, discount_rate):
    # Crear una nueva lista con el descuento aplicado
    discounted = []
    for price in prices_list:
        discounted_price = price * (1 - discount_rate)
        discounted.append(discounted_price)
    return discounted


def main_program(prices_text: str, discount_text: str):
    # Validar texto no vacío
    if not prices_text.strip():
        print("Error: invalid input")
        return

    # Intentar convertir descuento
    try:
        discount_rate = float(discount_text)
    except ValueError:
        print("Error: invalid input")
        return

    # Validar rango del descuento
    if discount_rate < 0 or discount_rate > 1:
        print("Error: invalid input")
        return

    # Procesar lista de precios
    parts = prices_text.split(",")
    prices_list = []

    for item in parts:
        item = item.strip()
        if not item:
            print("Error: invalid input")
            return
        try:
            price = float(item)
        except ValueError:
            print("Error: invalid input")
            return

        if price <= 0:
            print("Error: invalid input")
            return

        prices_list.append(price)

    # Validar lista no vacía
    if len(prices_list) == 0:
        print("Error: invalid input")
        return

    # Llamar a la función pura (sin modificar original)
    discounted_list = apply_discount(prices_list, discount_rate)

    print("Original prices:", prices_list)
    print("Discounted prices:", discounted_list)

# CASO USO:
# CORRECTO
"""
prices_text = "100, 50, 25"
discount_text = "0.2"
main_program(prices_text, discount_text)

Salida Esperada:
Original prices: [100.0, 50.0, 25.0]
Discounted prices: [80.0, 40.0, 20.0]

"""

# BORDE
"""
prices_text = "   10   "
discount_text = "0"
main_program(prices_text, discount_text)

Salida Esperada:
Original prices: [10.0]
Discounted prices: [10.0]

"""

# ERROR
"""
prices_text = "100, 200"
discount_text = "1.5"
main_program(prices_text, discount_text)

Salida Esperada:
Error: invalid input

"""
# Problem 5: Greeting function with default parameters
def greet(name, title=""):
    # Normalizar entradas
    name = name.strip()
    title = title.strip()

    # Validar nombre
    if not name:
        return "Error: invalid input"

    # Construir nombre completo
    if title:                   # si el título no está vacío
        full_name = f"{title} {name}"
    else:
        full_name = name

    return f"Hello, {full_name}!"


def main_program():
    # Ejemplos de llamada
    
    # Argumentos posicionales
    greeting1 = greet("Alice")
    
    # Argumentos nombrados (title opcional)
    greeting2 = greet(name="Bob", title="Eng.")
    
    print("Greeting:", greeting1)
    print("Greeting:", greeting2)

# CASO USO:
# CORRECTO
"""
greet("Alice")

Salida Esperada:
"Hello, Alice!"

"""

# BORDE
"""
greet("   Carlos   ")

Salida Esperada:
"Hello, Carlos!"

"""

# ERROR
"""
greet("")

Salida Esperada:
"Error: invalid input"

"""
# Problem 6: Factorial function (iterative or recursive)
def factorial(n):
    """
    Implementación ITERATIVA del factorial.
    Se usa un ciclo for porque:
    - evita el límite de recursión de Python,
    - es más eficiente en memoria,
    - es más simple de depurar.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main_program(n_text: str):
    # Validar conversión a entero
    try:
        n = int(n_text)
    except ValueError:
        print("Error: invalid input")
        return

    # Validar rango
    if n < 0 or n > 20:   # límite opcional por números demasiado grandes
        print("Error: invalid input")
        return

    # Calcular factorial
    fact_value = factorial(n)

    print("n:", n)
    print("Factorial:", fact_value)
# CASO USO:
# CORRECTO
"""
main_program("5")

Salida Esperada:
n: 5
Factorial: 120

"""

# BORDE
"""
main_program("0")

Salida Esperada:
n: 0
Factorial: 1

"""

# ERROR
"""
main_program("abc")

Salida Esperada:
Error: invalid input

"""

# CONCLUSION:
"""
    El uso de funciones en python resulta util y eficaz cuando se trata de crear lineas de codigo mas limpias, organizadas y claras
    tanto para la persona que crea el programa como para los que se encargan de revisar el codigo.

    Ademas tener codigo mas organizado y limpio nos da una ventaja para poder detectar errores y corregirlos de una manera mas
    rapida a comparacion de tener un codigo desorganizado.
"""

# References:
"""
1) Funciones en Python: https://aulavirtual.espol.edu.ec/courses/4558/pages/funciones-en-python
2) Funciones incorporadas: https://docs.python.org/es/3.13/library/functions.html
3) Funciones de Python: https://www.w3schools.com/python/python_functions.asp
4) Las FUNCIONES en PYTHON | ¿Para qué sirven y cómo se usan?: https://www.youtube.com/watch?v=hLRoDs4wNCU
5) APRENDE FUNCIONES en PYTHON: def, pass, sintaxis, None, return vs print, argumentos, scope y más: https://www.youtube.com/watch?v=9k91jETchkI
"""
