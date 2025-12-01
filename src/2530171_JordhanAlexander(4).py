# Manejo de bucles en Python
"""
METODOLOGIAS DE LA PROGRAMACION:
    MAESTRO: CARLOS ANTONIO TOVAR GARCIA
        CARRERA: MECATRONICA
        ALUMNO: JORDHAN ALEXANDER MARIANO RAMIREZ
        MATRICULA: 2530171
"""
# Resumen Ejecutivo
"""
- ¿Qué es un bucle for y para qué se usa típicamente?
es una estructura de control fundamental en programación que permite ejecutar 
repetidamente un bloque de código un número determinado de veces.

- ¿Qué es un bucle while y cuándo es más natural usarlo?
es una estructura de control en programación que ejecuta repetidamente un bloque de código 
mientras una condición específica siga siendo verdadera

- ¿Qué son un contador y un acumulador?
Un contador es una variable numérica cuyo valor se incrementa o decrementa en una cantidad fija 
y constante con cada iteración de un bucle. 

- ¿Por qué es importante definir bien la condición de salida y evitar ciclos infinitos?
Para garantizar que el programa termine y no cree un ciclo infinito, debido a que
nunca terminara y consumira memoria del dispositivo innecesariamente
"""

# PROBLEMAS:
#  Problem 1: Sum of range with for
def sum_to_n(n_text: str):
    # Validar conversión a entero
    try:
        n = int(n_text)
    except ValueError:
        print("Error: invalid input")
        return

    # Validar que n >= 1
    if n < 1:
        print("Error: invalid input")
        return

    total_sum = 0
    even_sum = 0

    # Recorrer de 1 a n
    for i in range(1, n + 1):
        total_sum += i
        if i % 2 == 0:      # si es par
            even_sum += i

    print("Sum 1..n:", total_sum)
    print("Even sum 1..n:", even_sum)

# CASO USO:
# CORRECTO
"""
10

Salida esperada:
Sum 1..n: 55
Even sum 1..n: 30

"""

# BORDE
"""
1

Salida esperada:
Sum 1..n: 1
Even sum 1..n: 0

"""

# ERROR
"""
hello

Salida esperada:
Error: invalid input

"""

# Problem 2: Multiplication table with for
def multiplication_table(base_text: str, m_text: str):
    # Validar conversión a entero
    try:
        base = int(base_text)
        m = int(m_text)
    except ValueError:
        print("Error: invalid input")
        return

    # Validar que m >= 1
    if m < 1:
        print("Error: invalid input")
        return

    # Generar tabla
    for i in range(1, m + 1):
        product = base * i
        print(f"{base} x {i} = {product}")

# CASO USO:
# CORRECTO
"""
base: 5
m: 4

Salida Esperada:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20

"""

# BORDE
"""
base: 7
m: 1

Salida Esperada:
7 x 1 = 7
"""

# ERROR
"""
base: 9
m: hola

Salida Esperada:
Error: invalid input

"""

# Problem 3: Average of numbers with while and sentinel
def sentinel_average():
    sentinel_value = -1
    total = 0.0
    count = 0

    while True:
        number_text = input("Enter a number (-1 to stop): ")

        # Validar conversión a float
        try:
            number = float(number_text)
        except ValueError:
            print("Error: invalid input")
            continue  # vuelve a pedir número

        # Verificar sentinela
        if number == sentinel_value:
            break

        # Acumular datos válidos
        total += number
        count += 1

    # Revisar si hubo datos válidos
    if count == 0:
        print("Error: no data")
    else:
        average = total / count
        print("Count:", count)
        print("Average:", average)

# CASO USO:
# CORRECTO
"""
10
20
30
-1

Salida Esperada:
Count: 3
Average: 20.0

"""

# BORDE
"""
-1
Salida Esperada:
Error: no data

"""

# ERROR
"""
hola
5
15
-1

Salida Esperada:
Error: invalid input
Count: 2
Average: 10.0

"""

# Problem 4: Password attempts with while

CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3
intents = 0

while intents < MAX_ATTEMPTS:
    user_pin = input("Write the Password")
    if user_pin == CORRECT_PIN:
        print("Acess")
        break
    else:
        intents+=1
        remaining_attemps = MAX_ATTEMPTS-intents
        if remaining_attemps>0:
            print(f"wrong Password {remaining_attemps} remaining attempts.")
        else:
            print("Access Denied.")
print("Finally")


    # Si se consumen todos los intentos
    print("Access Denied")

# CASO USO:
# CORRECTO
"""
Intento 1: 1234

Salida Esperada:
Finally
"""

# BORDE
"""
Intento 1: hola
Intento 2: admin123
Intento 3: 1234

Salida Esperada:
Finally
"""

# ERROR
"""
Intento 1: abc
Intento 2: test
Intento 3: 0000

Salida Esperada:
Access Denied
"""

# Problem 5: Simple menu with while
def menu_system():
    counter = 0  # inicializar contador

    while True:
        # Mostrar menú
        print("1) Show greeting")
        print("2) Show current counter value")
        print("3) Increment counter")
        print("0) Exit")

        option_text = input("Choose an option: ")

        # Validar opción
        try:
            option = int(option_text)
        except ValueError:
            print("Error: invalid option")
            continue  # vuelve al menú

        # Procesar opción
        if option == 1:
            print("Hello!")

        elif option == 2:
            print("Counter:", counter)

        elif option == 3:
            counter += 1
            print("Counter incremented")

        elif option == 0:
            print("Bye!")
            break  # salir del menú

        else:
            print("Error: invalid option")
    
# CASO USO:
# CORRECTO
"""
1
3
3
2
0

Salida Esperada:
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
Choose an option: 1
Hello!

...
Choose an option: 3
Counter incremented

...
Choose an option: 3
Counter incremented

...
Choose an option: 2
Counter: 2

...
Choose an option: 0
Bye!

"""

# BORDE
"""
2
0

Salida Esperada:
Counter: 0
Bye!

"""

# ERROR
"""
hola
0

Salida Esperada:
Error: invalid option
Bye!

"""

# Problem 6: Pattern printing with nested loops
def star_pattern(n_text: str):
    # Validar conversión a entero
    try:
        n = int(n_text)
    except ValueError:
        print("Error: invalid input")
        return

    # Validar rango
    if n < 1:
        print("Error: invalid input")
        return

    # Patrón normal (triángulo rectángulo)
    for i in range(1, n + 1):
        print("*" * i)

    # -------------------------------------------
    # OPCIONAL: patrón invertido
    # -------------------------------------------
    # Puedes comentar esta sección si no lo deseas.
    for i in range(n - 1, 0, -1):
        print("*" * i)
# CASO USO:
# CORRECTO
"""
5

Salida Esperada:
*
**
***
****
*****
****
***
**
*

"""

# BORDE
"""
1
Salida Esperada:
*

"""

# ERROR
"""
hello 
Salida Esperada:
Error: invalid input


"""

# CONCLUSION
"""
Para terminar con este tema, los bucles nos ayudan a crear cadenas sin la necesidad de estar
definiendo lo mismo una y otra vez, nos ahorran trabajo y tiempo a la hora de crear el codigo,
tambien hay que colocar un limite del bucle debido a que este al no tener un limite impuesto,
seguira repitiendo el codigo una cantidad ilimitada de veces, saturando nuestra memoria del
dispositivo.
"""

# References:
"""
1) Tutorial sobre bucles en Python: https://www.datacamp.com/es/tutorial/loops-python-tutorial
2) Bucles, Recursos Python: https://tutorial.recursospython.com/bucles/
3) Bucles, learnpython.org: https://www.learnpython.org/es/Loops
4) Ciclos en Python: cómo funcionan los bucles For y While y cómo hacerlos: https://ebac.mx/blog/ciclos-en-python
5) ¿Cómo hacer un BUCLE ♾️ en PYTHON? (Con EJEMPLOS incluidos) | Curso PYTHON desde CERO #5: https://www.youtube.com/watch?v=moUHTWl7QCQ
"""
