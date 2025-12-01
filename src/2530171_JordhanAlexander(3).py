# Manejo de Listas, Tuplas y Diccionarios en Python
"""
METODOLOGIAS DE LA PROGRAMACION:
    MAESTRO: CARLOS ANTONIO TOVAR GARCIA
        CARRERA: MECATRONICA
        ALUMNO: JORDHAN ALEXANDER MARIANO RAMIREZ
        MATRICULA: 2530171
"""

# INTRODUCCION:
"""
Se buscara conocer todo lo relacionado con las listas y las tuplas que viene manejando python,
ambas se parecen demasiado pero en funcion y concepto son distintos, por ejemplo
una lista se podra modificar a nuestra conveniencia, mientras la tupla se mantendra igual
y la unica manera de cambiar sus valores sera volviendo a definirla osea sobreescribir
sus valores con los que fue creada originalmente.
"""
# RESUMEN EJECUTIVO
"""
- ¿Qué es una lista, una tupla y un diccionario en Python y en qué se diferencian?
son estructuras de datos fundamentales utilizadas para almacenar colecciones de elementos, 
pero se diferencian significativamente en sus propiedades de mutabilidad, en su orden
y como acceden a los datos.

- ¿Qué significa que una lista sea mutable y una tupla inmutable?
Una lista es mutable debido a que podemos cambiar sus valores cuando el programa este
funcionando digamos que los valores originalmente eran [pera,manzana] y podemos agregar
una nueva y quedaria asi [pera,manzana,naranja],

mientras que una tupla sera inmutable porque no podemos modificar sus valores a menos que
dentro del codigo la volvamos a definir, su ventaja es que su valor siempre se mantendra
para guardar valores ya fijos como un dia de la semana o tu cumpleaños. Este se conforma
por () ejemplo: ("lunes","martes","miercoles")

El diccionario, se define por {} y cada elemento se conforma por pares por ejemplo,
{"manzana":"roja", "piña":"amarilla", "pera":"verde"}

- ¿Cómo se usan los diccionarios para asociar claves con valores?
se utilizan para asociar información a través de pares clave-valor, de manera similar 
a como se usa un índice para buscar información en un libro o una libreta de direcciones 
para encontrar el número de teléfono de una persona por su nombre.

"""
# PROBLEMAS
#  Problem 1: Shopping list basics (list operations)
def products(initial_items_text, new_item, search_item):
    # Se validaciones las iniciales ingresadas
    if not initial_items_text.strip():
        # Decisión documentada:
        # El usuario tiene oportunidad de dejar dentro de la lista espacios en blanco si necesita.
        items_list = []
    else:
        # Se limpian los espacios sobrantes
        raw_items = initial_items_text.split(",")
        items_list = [item.strip() for item in raw_items if item.strip()]

    # Se Valida new_item y search_item
    if not new_item.strip() or not search_item.strip():
        print("Error: invalid input")
        return

    # Agrega el nuevo producto
    items_list.append(new_item.strip())

    # Se muestra el total de elementos
    len_list = len(items_list)

    # Se verifica si el producto buscado está en la lista
    is_in_list = (search_item.strip() in items_list)

    # Salidas
    print("Items list:", items_list)
    print("Total items:", len_list)
    print("Found item:", str(is_in_list).lower())

# Caso uso:
# Correcto:
"""
products("milk, bread, eggs", "coffee", "bread")

Salida Esperada:
Items list: ['milk', 'bread', 'eggs', 'coffee']
Total items: 4
Found item: true

"""
# Borde:
"""
products("", "water", "water")

Salida Esperada:
Items list: ['water']
Total items: 1
Found item: true

"""
# Error:
"""
products("apple, pear", "   ", "pear")

Salida Esperada:
Error: invalid input

"""


# Problem 2: Points and distances with tuples
def points(x1_input, y1_input, x2_input, y2_input):
    # Se intenta convertir todas las entradas a float
    try:
        x1 = float(x1_input)
        y1 = float(y1_input)
        x2 = float(x2_input)
        y2 = float(y2_input)
    except ValueError:
        print("Error: invalid input")
        return

    # Se Crean tuplas para nuestras coordenadas X y Y
    point_a = (x1, y1)
    point_b = (x2, y2)

    # Se Calcula la distancia euclidiana
    distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

    # Se Calcula el punto medio
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    # Salidas
    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)

# Caso uso:
# Correcto:
"""
points("0", "0", "3", "4")

Salida Esperada:
Point A: (0.0, 0.0)
Point B: (3.0, 4.0)
Distance: 5.0
Midpoint: (1.5, 2.0)

"""
# Borde:
"""
points("2", "3", "2", "3")

Salida Esperada:
Point A: (2.0, 3.0)
Point B: (2.0, 3.0)
Distance: 0.0
Midpoint: (2.0, 3.0)

"""
# Error:
"""
points("abc", "2", "3", "4")

Salida Esperada:
Error: invalid input

"""

# Problem 3: Product catalog with dictionary
def products(product_name_input, quantity_input):
    # El diccionario inicial con los 3 productos
    product_prices = {
        "apple": 10.0,
        "banana": 6.5,
        "orange": 8.0
    }

    # Se valida el nombre del producto
    product_name = product_name_input.strip().lower()
    if not product_name:
        print("Error: product not found")
        return

    # Se valida la cantidad
    try:
        quantity = int(quantity_input)
    except ValueError:
        print("Error: product not found")
        return

    if quantity <= 0:
        print("Error: product not found")
        return

    # Se verifica la existencia del producto
    if product_name not in product_prices:
        print("Error: product not found")
        return

    # Se obtiene el precio y se calcula el total
    unit_price = product_prices[product_name]
    total_price = unit_price * quantity

    # Salidas
    print("Unit price:", unit_price)
    print("Quantity:", quantity)
    print("Total:", total_price)

# Caso uso:
# Correcto:
"""
products("apple", "3")

Salida Esperada:
Unit price: 10.0
Quantity: 3
Total: 30.0

"""
# Borde:
"""
products("banana", "1")

Salida Esperada:
Unit price: 6.5
Quantity: 1
Total: 6.5

"""
# Error:
"""
products("watermelon", "2")

Salida Esperada:
Error: product not found

"""

# Problem 4: Student grades with dict and list
def adcalif(student_name_input):
    # El Diccionario inicial con 3 estudiantes y listas de calificaciones
    grades = {
        "alice": [90.0, 85.5, 88.0],
        "bob": [70.0, 72.0, 68.5],
        "carla": [95.0, 92.0, 98.0]
    }

    # Se validan los nombres
    student_name = student_name_input.strip().lower()
    if not student_name:
        print("Error: student not found")
        return

    # Se verifica la existencia del estudiante
    if student_name not in grades:
        print("Error: student not found")
        return

    # Se obtiene la lista de calificaciones
    grades_list = grades[student_name]

    # Se valida que la lista no este vacia
    if len(grades_list) == 0:
        print("Error: student not found")  # si no se encuentra muestra un error
        return

    # Se calcula el promedio
    average = sum(grades_list) / len(grades_list)

    # Se determina si aprobo
    is_passed = (average >= 70.0)

    # Salidas
    print("Grades:", grades_list)
    print("Average:", average)
    print("Passed:", str(is_passed).lower())

# Caso uso:
# Correcto:
"""
adcalif("Carla")

Salida Esperada:
Grades: [95.0, 92.0, 98.0]
Average: 95.0
Passed: true

"""
# Borde:
"""
adcalif("   aLIce  ")

Salida Esperada:
Grades: [90.0, 85.5, 88.0]
Average: 87.83333333333333
Passed: true

"""
# Error:
"""
adcalif("juan")

Salida Esperada:
Error: student not found

"""

# Problem 5: Word frequency counter (list + dict)
def countwords(sentence_input):
    # Se valida que el espacio no este en blanco
    if not sentence_input.strip():
        print("Error: invalid input")
        return

    # Para manejar la puntuación simple, se reemplazan .,;!?
    # para los espacios. Esto ayuda a evitar palabras con signos pegados.
    sentence = (
        sentence_input.lower()
        .replace(".", " ")
        .replace(",", " ")
        .replace(";", " ")
        .replace("!", " ")
        .replace("?", " ")
    )

    # Se convierte la lista de palabras
    words_list = [word for word in sentence.split() if word.strip()]

    if len(words_list) == 0:
        print("Error: invalid input")
        return

    # Para construir un diccionario de frecuencias
    freq_dict = {}
    for word in words_list:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    # Se determina la palabra más común
    most_common_word = None
    max_freq = 0

    for word, freq in freq_dict.items():
        if freq > max_freq:
            most_common_word = word
            max_freq = freq

    # Salidas
    print("Words list:", words_list)
    print("Frequencies:", freq_dict)
    print("Most common word:", most_common_word)


# Caso uso:
# Correcto:
"""
countwords("Hola hola adiós hola")

Salida Esperada:
Words list: ['hola', 'hola', 'adiós', 'hola']
Frequencies: {'hola': 3, 'adiós': 1}
Most common word: hola

"""
# Borde:
"""
countwords("...Hola,, hola!!   HOLA?;   adios...")

Salida Esperada:
Words list: ['hola', 'hola', 'hola', 'adios']
Frequencies: {'hola': 3, 'adios': 1}
Most common word: hola

"""
# Error:
"""
countwords("   .... ,,, ;; !! ???   ")

Salida Esperada:
Error: invalid input

"""
# Problem 6: Simple contact book (dictionary CRUD)
def contact_book(action_text_input, name_input=None, phone_input=None):
    # El Diccionario inicial de contactos
    contacts = {
        "alice": "1234567890",
        "bob": "5551112222",
        "carla": "9876543210"
    }

    # Se normaliza la accion
    action = action_text_input.strip().upper()

    # Se valida la accion
    if action not in ["ADD", "SEARCH", "DELETE"]:
        print("Error: invalid action")
        return

    # Se valida el nombre
    if name_input is None or not name_input.strip():
        print("Error: contact not found")
        return
    name = name_input.strip().lower()

    # Para el manejo de acciones
    if action == "ADD":
        # Para validar el telefono
        if phone_input is None or not phone_input.strip():
            print("Error: contact not found")
            return
        phone = phone_input.strip()

        # Para Guardar o actualizar el contacto
        contacts[name] = phone
        print("Contact saved:", name, phone)

    elif action == "SEARCH":
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Error: contact not found")

    elif action == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")
# Caso uso:
# Correcto:
"""
contact_book("ADD", "Daniel", "4449990000")

Salida Esperada:
Contact saved: daniel 4449990000

"""
# Borde:
"""
contact_book("search", "   Alice   ")

Salida Esperada:
Phone: 1234567890

"""
# Error:
"""
contact_book("DELETE", "juan")

Salida Esperada:
Error: contact not found

"""

# CONCLUSION
"""
 El uso y implementacion de listas y tuplas es escencial para poder organizar nuestros
 objetos y poder identificarlos de una manera mas sencilla y ordenada,
 dentro del codigo podemos utilizar una o otra de acuerdo a lo que se necesite por ejemplo
 si necesitamos un listado con numeros como por ejemplo
    1- Primera opcion
    2- Segunda opcion
    3- Tercera opcion
a diferencia de una lista como esta [manzana,pera,piña,uva,naranja]
en la primera opcion nos funcionaria para poder teclear un numero y de acuerdo al numero este
realizara la operacion correspondiente, mientras la otra podemos usar solo para mostrar listas
o utilizar el sistema de coordenadas como el ejemplo anterior que se pudo apreciar
"""

# References:
"""
1) Tuple vs List en Python: ¿Cuál es la diferencia?: https://www.freecodecamp.org/espanol/news/tuple-vs-list-en-python-cual-es-la-diferencia/
2) ¿Qué son las listas, tuplas y diccionarios en Python?: https://www.pontia.tech/python-listas-tuplas-diccionario/
3) Listas y tuplas Recursos Python: https://recursospython.com/guias-y-manuales/listas-y-tuplas/
4) COMO USAR las LISTAS, TUPLAS Y RANGE en PYTHON #7: https://www.youtube.com/watch?v=lH9qJ7OxCig
5) Comprensión de Diccionario en Python: Explicado con ejemplos: https://www.freecodecamp.org/espanol/news/compresion-de-diccionario-en-python-explicado-con-ejemplos/
"""
