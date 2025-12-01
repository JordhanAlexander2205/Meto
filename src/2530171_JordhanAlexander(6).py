# Fibonacci
"""
METODOLOGIAS DE LA PROGRAMACION:
    MAESTRO: CARLOS ANTONIO TOVAR GARCIA
        CARRERA: MECATRONICA
        ALUMNO: JORDHAN ALEXANDER MARIANO RAMIREZ
        MATRICULA: 2530171
"""

# Resumen Ejecutivo:
"""
- ¿Qué es la serie de Fibonacci?
Se trata de una sucesion infinita de números donde cada término es la suma de los dos anteriores, comenzando generalmente con 0 y 1.
La secuencia comienza: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, y asi de manera infinita-

- ¿Qué significa “calcular la serie hasta un número de términos n”?
Significa generar la lista en base de los numeros que el usuario haya solicitado

- ¿Qué cubrirá tu programa?: lectura de n, validación básica y generación de la serie.
Se le solicitara al usuario que ingrese una cierta cantidad de numeros y con base a eso, se realizara la secuencia de Fibonacci
correspondiente,

Por ejemplo si el usuario ingresa n = 7, el programa arrojara la siguiente sucession:

Resultado Esperado
Serie Fibonacci:
0 1 1 2 3 5 8

"""
def fibonacci(n):
    """Generate n terms of the Fibonacci series using a loop."""
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    series = [0, 1]
    while len(series) < n:
        next_value = series[-1] + series[-2]
        series.append(next_value)
    return series


def main_program(n_text: str):
    # Se valida para asegurarse que sea entero.
    try:
        n = int(n_text)
    except ValueError:
        # En caso de Error debera mostrar el siguiente mensaje.
        print("Error: invalid input")
        return

    # Validaciones del rango.
    if n < 1 or n > 50:
        print("Error: invalid input")
        return

    # Para poder generar nuestra serie de Fibonacci.
    series = fibonacci(n)

    # Salida para mostrar los resultados:
    print("Fibonacci series:", *series)


if __name__ == "__main__":
    # Se Leer desde un input en caso de que se llegara a ejecutar el script directamente
    user_input = input("Enter number of terms: ").strip()
    main_program(user_input)

# CASO USO
# CORRECTO:
"""
Enter number of terms: 10

Salida Esperada:

Fibonacci series: 0 1 1 2 3 5 8 13 21 34

"""

# BORDE:
"""
Si se ingresa "Enter number of terms: 1", se mostrara lo siguiente:

Resultado Esperado:

Serie Fibonacci:
0
"""

# ERROR:
"""

Enter number of terms: "hola"

Si se ingresa un valor incorrecto se mostrara lo siguiente:

Resultado esperado:
Error: n must be a positive integer.
"""

# Diagrama
"""
flowchart TD

A[Inicio] --> B[Leer n_text como string]
B --> C{¿Se puede convertir a entero?}
C -- No --> C1[Mostrar "Error: invalid input"] --> Z[Fin]
C -- Sí --> D[Convertir n = int(n_text)]

D --> E{¿n < 1 o n > 50?}
E -- Sí --> E1[Mostrar "Error: invalid input"] --> Z
E -- No --> F[Llamar fibonacci(n)]

F --> G{¿n == 1?}
G -- Sí --> G1[Regresar [0]] --> H[Serie generada]
G -- No --> I{¿n == 2?}
I -- Sí --> I1[Regresar [0,1]] --> H
I -- No --> J[Inicializar series = [0,1]]

J --> K{len(series) < n?}
K -- Sí --> L[Calcular next_value = suma de últimos dos] --> M[Agregar next_value a series] --> K
K -- No --> H[Serie generada]

H --> N[Mostrar "Fibonacci series:" + series]
N --> Z[Fin]

"""

# Conclusion:
"""
El uso de ciclos fue perfecto para este problema planteado, pues los ciclos ayudaban a crear la serie de Fibonacci correctamente,
La implementacion sobre el uso de n=1 y n=2 fue de gran utilidad debido que la sucesion ya estaba definida y se seguia la secuencia para
realizar un bucle con base a los datos obtenidos conforme se iban generando mediante el mismo. la operacion de la cantidad de veces
que el usuario ingrese para su realizacion.
"""

# References:
"""
1) Fibonacci, el matemático que se puso a contar conejos y descubrió la secuencia divina: https://www.bbc.com/mundo/noticias-46926506
2) Bucle For de Python: un tutorial detallado: https://blog.udemy.com/python-while-loop/?utm_campaign=PMax_la.ES_cc.MX&utm_source=google&utm_medium=paid-search&portfolio=Mexico&utm_audience=mx&utm_tactic=pmax&utm_term=&utm_content=x&funnel=&test=&gad_source=1&gad_campaignid=23268773883&gbraid=0AAAAADROdO0GsFzlbPEUlanosfuS12Yz8&gclid=CjwKCAiA86_JBhAIEiwA4i9Ju5Y84dor5vGkHHSHXgsoNQJcp1g-3lSEnp_YtPC38XU_8Cwv0xlduhoCy_4QAvD_BwE
3) Secuencia de Fibonacci en Python: Aprende y explora técnicas de programación: https://www.datacamp.com/es/tutorial/fibonacci-sequence-python
4) W3 Schools: https://www.w3schools.com/python/python_while_loops.asp
5) Loops while y for en Python: ¿Qué son y cómo usarlos?: https://platzi.com/blog/loops-while-y-for-en-python-que-son-y-como-usarlos/
"""
