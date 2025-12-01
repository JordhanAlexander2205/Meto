# Manejo de números y booleanos en Python
"""
METODOLOGIAS DE LA PROGRAMACION:
    MAESTRO: CARLOS ANTONIO TOVAR GARCIA
        CARRERA: MECATRONICA
        ALUMNO: JORDHAN ALEXANDER MARIANO RAMIREZ
        MATRICULA: 2530171
"""

# INTRODUCCION:
"""
EN ESTE REPORTE SE BUSCA CONOCER ACERCA DEL USO DE LOS NUMEROS Y BOOLEANOS EN PYTHON, TAMBIEN
SE BUSCARA EXPLICAR LOS SIGUIENTES EJERCICIOS DE UNA MANERA QUE RESULTE SENCILLA Y PRACTICA
DE ENTENDER PARA EL LECTOR.
"""

# RESUMEN EJECUTIVO
"""
- ¿Qué son los tipos int y float en Python y en qué se diferencian?
Para empezar utilizamos int para numeros enteros como el 1,2,3,4,5.
Mientras que float funciona para numeros reales es decir 0.5,0.25, 10.25, entre otros

- ¿Qué es un booleano (True/False) y cómo se obtiene a partir de comparaciones?
Son operaciones de logica,se trata de una pregunta con 1 opcion ya sea
VERDADERO o FALSO, aunque tambien podemos ampliar su extension con IF y ELSE acorde a lo que
necesitemos, se obtiene a partir de los Operadores de comparacion como por ejemplo, >,<, ==.

- ¿Por qué es importante validar rangos y evitar división entre cero?
Validar los rangos es importante, porque el programa entiende cuales son los limites que
nosotros le damos, de lo contrario este continuaria contando infinitamente.

Se evita la division entre el 0, debido a que dividir cualquier cantidad entre 0 es algo
totalmente indefinido provocando que nuestro programa colapse y no sepa como reaccionar
ante esa situacion, por lo tanto se cierra antes de que se corrompa nuestro codigo
"""

# PROBLEMAS:
# Problem 1: Temperature converter and range flag
    
def convertir_temperatura(temp_c_input):
    # Se valida para que se pueda convertir a float
    try:
        temp_c = float(temp_c_input)
    except ValueError:
        # Si los datos son incorrectos mostrara ese mensaje
        print("Invalid input: cannot be converted to float.")
        return

    # Se realiza la operacion para conseguir los Kelvin
    temp_k = temp_c + 273.15

    # Se mostrara este mensaje si la temperatura es físicamente imposible
    if temp_k < 0.0:
        print("Invalid temperature: the value in Kelvin cannot be less than 0.")
        return

    # Se realiza la operacion para Fahrenheit
    temp_f = temp_c * 9 / 5 + 32

    # Se determina si la temperatura es alta
    is_high_temperature = (temp_c >= 30.0)

    # Salidas
    print("Fahrenheit:", temp_f)
    print("Kelvin:", temp_k)
    print("High temperature:", str(is_high_temperature).lower())

# Caso uso:
# Correcto:
"""
convertir_temperatura("25")

Salida Esperada:
Fahrenheit: 77.0
Kelvin: 298.15
High temperature: false

"""
# Borde:
"""
convertir_temperatura("-273.15")

Salida Esperada:
Fahrenheit: -459.66999999999996
Kelvin: 0.0
High temperature: false


"""
# Error:
"""
convertir_temperatura("hello")

Salida Esperada:
Invalid input: cannot be converted to float.

"""

# Problem 2: Work hours and overtime payment
def calcular_pago(hours_worked_input, hourly_rate_input):
    # Se Intentan convertir las entradas a float
    try:
        hours_worked = float(hours_worked_input)
        hourly_rate = float(hourly_rate_input)
    except ValueError:
        # Si es incorrecto, se mostrara el siguiente mensaje
        print("Error: invalid input")
        return

    # Si los datos son correctos continuara con las operaciones correspondientes
    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
        return

    # Operaciones correspondientes de las horas regulares y extra
    regular_hours = min(hours_worked, 40)
    overtime_hours = max(hours_worked - 40, 0)

    # Se calculan los pagos mediante las horas
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = regular_pay + overtime_pay

    # Usamos un Booleano para las horas extra
    has_overtime = (hours_worked > 40)

    # Salidas
    print("Regular pay:", regular_pay)
    print("Overtime pay:", overtime_pay)
    print("Total pay:", total_pay)
    print("Has overtime:", str(has_overtime).lower())

# Caso uso:
# Correcto:
"""
calcular_pago("45", "10")

Salida Esperada:
Regular pay: 400.0
Overtime pay: 75.0
Total pay: 475.0
Has overtime: true

"""
# Borde:
"""
calcular_pago("40", "15")

Salida Esperada:
Regular pay: 600.0
Overtime pay: 0.0
Total pay: 600.0
Has overtime: false

"""
# Error:
"""
calcular_pago("hola", "8")

Salida Esperada:
Error: invalid input

"""
# Problem 3: Discount eligibility with booleans
def calcular_descuento(purchase_total_input, is_student_text, is_senior_text):
    # Se intenta convertir el total de compra a un float
    try:
        purchase_total = float(purchase_total_input)
    except ValueError:
        # Al ser un error mostrara el siguiente mensaje
        print("Error: invalid input")
        return

    # Se Valida el total de compra
    if purchase_total < 0.0:
        print("Error: invalid input")
        return

    # Se normalizan los textos a mayusculas
    is_student_norm = is_student_text.strip().upper()
    is_senior_norm = is_senior_text.strip().upper()

    # Se validan y convierten a Booleanos
    if is_student_norm == "YES":
        is_student = True
    elif is_student_norm == "NO":
        is_student = False
    else:
        # Si no es posible, se mostrara el siguiente mensaje
        print("Error: invalid input")
        return
        # repetimos el mismo proceso pero ahora con senior
    if is_senior_norm == "YES":
        is_senior = True
    elif is_senior_norm == "NO":
        is_senior = False
    else:
        print("Error: invalid input")
        return

    # Se determina si es elegible para el descuento
    discount_eligible = (is_student or is_senior or (purchase_total >= 1000.0))

    # Se calcula el total final
    if discount_eligible:
        final_total = purchase_total * 0.9
    else:
        final_total = purchase_total

    # Salidas
    print("Discount eligible:", str(discount_eligible).lower())
    print("Final total:", final_total)

# Caso uso:
# Correcto:
"""
calcular_descuento("500", "YES", "NO")

Salida Esperada:
Discount eligible: true
Final total: 450.0

"""
# Borde:
"""
calcular_descuento("1000", "NO", "NO")

Salida Esperada:
Discount eligible: true
Final total: 900.0

"""
# Error:
"""
calcular_descuento("300", "maybe", "NO")

Salida Esperada:
Error: invalid input

"""
# Problem 4: Basic statistics of three integers
def calcular_valores(n1_input, n2_input, n3_input):
    # Se valida para convertir a int
    try:
        n1 = int(n1_input)
        n2 = int(n2_input)
        n3 = int(n3_input)
    except ValueError:
        # Al ser un error se mostrara el siguiente mensaje
        print("Error: invalid input")
        return

    # Se realizan los calculos correspondientes
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    # Salidas
    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", str(all_even).lower())
# Caso uso:
# Correcto:
"""
calcular_valores("4", "7", "10")

Salida Esperada:
Sum: 21
Average: 7.0
Max: 10
Min: 4
All even: false

"""
# Borde:
"""
calcular_valores("2", "2", "2")

Salida Esperada:
Sum: 6
Average: 2.0
Max: 2
Min: 2
All even: true

"""
# Error:
"""
calcular_valores("10", "x", "5")

Salida Esperada:
Error: invalid input

"""

# Problem 5: Loan eligibility (income and debt ratio)
def evaluar_prestamo(monthly_income_input, monthly_debt_input, credit_score_input):
    # Se intentan las conversiones
    try:
        monthly_income = float(monthly_income_input)
        monthly_debt = float(monthly_debt_input)
        credit_score = int(credit_score_input)
    except ValueError:
        print("Error: invalid input")
        return

    # Se validan los valores obtenidos anteriormente
    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
        return

    # Se calcula el debt ratio
    debt_ratio = monthly_debt / monthly_income

    # Se determina la elegibilidad
    eligible = (
        monthly_income >= 8000.0 and
        debt_ratio <= 0.4 and
        credit_score >= 650
    )

    # Salidas
    print("Debt ratio:", debt_ratio)
    print("Eligible:", str(eligible).lower())
# Caso uso:
# Correcto:
"""
evaluar_prestamo("10000", "2000", "700")

Salida Esperada:
Debt ratio: 0.2
Eligible: true

"""
# Borde:
"""
evaluar_prestamo("8000", "3200", "650")

Salida Esperada:
Debt ratio: 0.4
Eligible: true

"""
# Error:
"""
evaluar_prestamo("ocho mil", "1000", "700")

Salida Esperada:
Error: invalid input

"""

# Problem 6: Body Mass Index (BMI) and category flag
def calcular_bmi(weight_input, height_input):
    # Se hace un intento para las conversiones
    try:
        weight_kg = float(weight_input)
        height_m = float(height_input)
    except ValueError:
        print("Error: invalid input")
        return

    # Se validan datos
    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
        return

    # Se realiza el calculo del BMI
    bmi = weight_kg / (height_m * height_m)
    bmi_redondeado = round(bmi, 2)

    # Usamos booleanos con condiciones
    is_underweight = (bmi < 18.5)
    is_normal = (18.5 <= bmi < 25.0)
    is_overweight = (bmi >= 25.0)

    # Salidas
    print("BMI:", bmi_redondeado)
    print("Underweight:", str(is_underweight).lower())
    print("Normal:", str(is_normal).lower())
    print("Overweight:", str(is_overweight).lower())
# Caso uso:
# Correcto:
"""
calcular_bmi("70", "1.75")

Salida Esperada:
BMI: 22.86
Underweight: false
Normal: true
Overweight: false

"""
# Borde:
"""
calcular_bmi("80", "1.79")

Salida Esperada:
BMI: 25.0
Underweight: false
Normal: false
Overweight: true

"""
# Error:
"""
calcular_bmi("sesenta", "1.70")

Salida Esperada:
Error: invalid input

"""

# CONCLUSION
"""
    Para finalizar este tema me resulto interesante porque se aprendio la implementacion
    de operaciones dentro de codigo para que los programas utilicen las cantidades y 
    arrojen el resultado final, podriamos realizar una calculadora y pedirle que solo haga
    una operacion en base al numero que se elija o incluso podremos realizar calculos de 
    formulas especificas como por ejemplo para sacar los grados Kelvin y Farenheint como se
    pudo apreciar en los ejercicios anteriores. 
"""

# References:
"""
1) DATOS NUMÉRICOS | Curso de Python desde cero 🐍: https://www.youtube.com/watch?v=Nn7k0G-IRSk
2) 3.14.0 Documentación » Manual de referencia de la API de Python/C » Capa de objetos concretos » Objetos booleanos: https://docs.python.org/3/c-api/bool.html
3) Python desde Cero » Operadores Lógicos y Relacionales: https://controlautomaticoeducacion.com/python-desde-cero/operadores-logicos-y-relacionales/#:~:text=Operadores%20Relacionales%20y%20Operadores%20L%C3%B3gicos%20en%20Python,-Tap%20to%20unmute&text=Este%20tipo%20de%20operadores%20nos,una%20parte%20determinada%20del%20c%C3%B3digo.
4) Tipos de datos de Python: https://www.geeksforgeeks.org/python/python-data-types/
5) Tipos de datos numéricos en Python | ¿Qué son Números en Python? | Curso completo Python: https://www.youtube.com/watch?v=a5Du8RvdCrg
"""