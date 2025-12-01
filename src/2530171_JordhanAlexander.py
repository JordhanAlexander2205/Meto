# Manejo de strings en Python
"""
METODOLOGIAS DE LA PROGRAMACION:
    MAESTRO: CARLOS ANTONIO TOVAR GARCIA
        CARRERA: MECATRONICA
        ALUMNO: JORDHAN ALEXANDER MARIANO RAMIREZ
        MATRICULA: 2530171
"""
# INTRODUCCION:
""""
    Durante este reporte se aprendera a utilizar los famosos strings de python,
    para empezar un string es una secuencia de caracteres que componen codigo como palabras
    y texto, que es lo mas comun, aunque tambien pueden ser numeros y caracteres con el fin de
    mostrar mensajes en pantalla.
    Por ejemplo puedo usar print("HOLA MUNDO") y se mostrara HOLA MUNDO en pantalla,

    Tambien se usa para mostrar correos, numeros de telefono, y entre otras cosas utiles,
    todo debe ir dentro de las comillas, porque se trata de texto y no otra variable mas
    del codigo, tambien es importante las validaciones del texto porque por un simple
    caracter ditinto tu codigo puede ocasionar un error, por ejemplo hola y Hola.
"""

"""
- Los strings son inmutables: cualquier cambio genera una nueva cadena.
- Es buena práctica normalizar entrada con strip() y lower() antes de compararla.
- Evitar "números mágicos" en índices; documentar qué extrae cada slice.
- Usar métodos de string en lugar de reescribir lógica básica.
- Diseñar validaciones claras: primero que no esté vacío, luego el formato.
- Escribir código legible: nombres de variables claros y mensajes de error entendibles.
"""
# RESUMEN EJECUTIVO
"""
- ¿Qué es un string en Python (tipo de dato, inmutabilidad)?
Se trata de una secuencia de caracteres utilizada para manejar texto, 
que se puede crear entre comillas simples o dobles.
Es un tipo de dato inmutable, lo que significa que no se puede modificar después de su creación.

- ¿Qué operaciones básicas se pueden realizar: concatenar, obtener longitud, extraer sub-cadenas,
 buscar patrones, reemplazar texto?
 Concatenar: Unir dos o más cadenas de texto en una sola.

Obtener longitud: Determinar el número de caracteres que componen una cadena de texto.

Extraer sub-cadenas: Aislar una porción específica (subcadena) de una cadena más grande.

Buscar patrones: Localizar la presencia de caracteres o secuencias de caracteres específicas,
a menudo utilizando herramientas como expresiones regulares.

Reemplazar texto: Sustituir una subcadena o patrón de texto por otro texto diferente. 


- ¿Por qué es importante validar y normalizar texto de entrada (por ejemplo, correos, 
nombres, contraseñas)?
Es demasiado importante porque imagina que tu programa solamente detecta la palabra
contraseña como entrada,
y el usuario coloca CONTRASEÑA, a simple vista parece la misma entrada pero Python la detecta
como una entrada completamente distinta por que el caracter C es distinto, por eso nosotros
utilizamos .lower() o .upper() para que la entrada coincida con la que le especificamos a
nuestro programa que estemos realizando
"""
# PROBLEMAS
# Problem 1: Full name formatter (name + initials)
def format_name(full_name_text):
    # Normalize text
    cleaned = full_name_text.strip()

    # Validate empty input
    if not cleaned:
        print("Error: invalid input")
        return

    # Split into words
    parts = cleaned.split()

    # Validate at least two names
    if len(parts) < 2:
        print("Error: invalid input")
        return

    # Format each word in Title Case
    formatted_name = " ".join([p.title() for p in parts])

    # Generate initials
    initials = ".".join([p[0].upper() for p in parts]) + "."

    # Outputs
    print("Formatted name:", formatted_name)
    print("Initials:", initials)

# CASOS DE USO:
# Verdadero:
"""
format_name("juan perez")

Salida Esperada:

Formatted name: Juan Perez
Initials: J.P.

"""
# Borde:
"""
format_name("   maria   lopez   gomez  ")

Salida Esperada:

Formatted name: Maria Lopez Gomez
Initials: M.L.G.

"""
# Error:
"""
format_name("   ")

Salida Esperada:
Error: invalid input

"""

# Problem 2: Simple email validator (structure + domain)
def validate_email(email_text: str):
    # Empezamos normalizando el texto
    email = email_text.strip()

    # Se asegura que sea un email o correo
    if not email:
        print("Valid email: false")
        return

    # Revisa que no contenga espacios
    if " " in email:
        print("Valid email: false")
        return

    # Verifica que el email tenga exactamente un '@'
    if email.count("@") != 1:
        print("Valid email: false")
        return

    # Se separan en 2 partes para asegurarse que el dominio sea correcto
    at_index = email.find("@")
    domain = email[at_index + 1:]  # El dominio es todo lo despues del '@'

    # Se valida que haya texto antes y después del '.' en el dominio
    if "." not in domain:
        print("Valid email: false")
        return

    # Nueva validación mejorada:
    # El dominio debe tener al menos algo antes del punto y algo después
    domain_parts = domain.split(".")
    if len(domain_parts) < 2 or not domain_parts[0] or not domain_parts[1]:
        print("Valid email: false")
        return

    # Si todo lo anterior fue correcto entonces:
    print("Valid email: true")
    print(f"Domain: {domain}")

# CASOS DE USO
# Verdadero:
"""
"usuario@gmail.com"
Salida Esperada:

Valid email: true
Domain: gmail.com

"""
# Borde:
"""
" MiCorreo123@Outlook.mx "
Salida Esperada:

Valid email: true
Domain: Outlook.mx

"""
# Error:
"""
"persona@dominio."
Salida Esperada:

Valid email: false

"""

# Problem 3: Palindrome checker (ignoring spaces and case)
phrase = input("Enter a phrase: ")

# Se valida que no este en blanco el espacio
if not phrase.strip():
    print("Error: phrase cannot be empty.")
else:
    # Normalizamos el texto y quitamos los espacios
    normalized = phrase.lower().replace(" ", "")

    # Se asegura que la frase ingresada no sea demasiado corta
    if len(normalized) < 3:
        print("Error: phrase is too short to check for palindrome.")
    else:
        # Se revisa el palindromo con slicing de manera inversa con -1 para que cuente de
        # derecha a izquierda
        is_palindrome = normalized == normalized[::-1]

        print(f"Normalized phrase: {normalized}")
        print(f"Is palindrome: {is_palindrome}")
# CASOS DE USO:
#Correcto:
"""
Enter a phrase: Anita lava la tina

Salida Esperada:
Normalized phrase: anitalavalatina
Is palindrome: true

"""
#BORDE:
"""
Enter a phrase: aa

Salida Esperada:
Error: phrase is too short to check for palindrome.

"""
#ERROR:
"""
Enter a phrase:

Salida Esperada:
Error: phrase cannot be empty.

"""
# Problem 4: Sentence word stats (lengths and first/last word)
sentence = input("Enter a sentence: ")

# Se asegura que el espacio no este en blanco
if not sentence.strip():
    print("Error: empty sentence.")
else:
    # Se normaliza el texto
    sentence = sentence.strip()

    # Se Separan las palabras
    words = sentence.split()

    if len(words) == 0:
        print("Error: no valid words.")
    else:
        # Se cuentan las palabras
        print("Word count:", len(words))

        # Para identificar la Primera y Ultima
        print("First word:", words[0])
        print("Last word:", words[-1])

        # Para identificar la palabra más corta y más larga
        shortest = min(words, key=len)
        longest = max(words, key=len)

        # Salidas:
        print("Shortest word:", shortest)
        print("Longest word:", longest)
# CASOS DE USO:
# VERDADERO:
"""
Enter a sentence: Hello this is a testing

Salida Esperada:

Word count: 5
First word: Hello
Last word: testing
Shortest word: a
Longest word: testing


"""
# BORDE:
"""
Enter a sentence: Hello

Salida Esperada:
Word count: 1
First word: Hello
Last word: Hello
Shortest word: Hello
Longest word: Hello

"""
# ERROR:
"""
Enter a sentence:

Salida Esperada:
Error: empty sentence.

"""

# Problem 5: Password strength classifier
password_input = input("Enter a password: ")

# Se asegura que el espacio no este en blanco
if not password_input:
    print("Error: password cannot be empty.")
else:
    pw = password_input

    # Validaciones
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for ch in pw:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif not ch.isalnum():
            has_symbol = True

    # Se clasifican:
    # weak: si tiene menos de 8 caracteres, o es muy simple
    if len(pw) < 8 or (has_lower and not (has_upper or has_digit or has_symbol)):
        strength = "weak"
    # strong: Si cumple con todos los parametros
    elif has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    # medium: si cumple con la mayoria
    else:
        strength = "medium"
    # SALIDA
    print("Password strength:", strength)

# CASOS DE USO
# VERDADERO:
"""
Enter a password: Abc123!@

Salida Esperada:
Password strength: strong

"""
# BORDE:
"""
Enter a password: Abc12345

Salida Esperada:
Password strength: medium

"""
# ERROR:
"""
Enter a password: Ab1!

Salida Esperada:
Password strength: weak

"""

# Problem 6: Product label formatter (fixed-width text)
product_name = input("Product name: ").strip()
price_value = input("Price: ").strip()

# Se asegura que el espacio no este en blanco
if not product_name:
    print("Error: product name cannot be empty.")
else:
    try:
        price = float(price_value)
        if price <= 0:
            raise ValueError
    except:
        print("Error: price must be a positive number.")
    else:
        # Se crea la etiqueta del producto
        base = f"Product: {product_name} | Price: ${price}"

        # Hace los ajustes necesarios para que sean los 30 caracteres exactos
        if len(base) > 30:
            label = base[:30]      # Recortar si es necesario
        else:
            label = base.ljust(30) # Rellenar con espacios si es necesario

        print(f'Label: "{label}"')  # Salida

# CASOS DE USO
# VERDADERO:
""" 
product_name = "Laptop"
price_value = 15999

Salida Esperada:

base: "Product: Laptop,  Price: $15999"
"""
# BORDE:
"""
Product name: "ProductldldldldlldgnsiiilmXYZ98709"
Price: 50

Salida Esperada:

Label: "Product:ProductldldldldlldgnsiiilmXYZ98709 "
"""
# ERROR:
"""
Product name: "Guayaba"
Price: -10

Salida Esperada:
Error: price must be a positive number.


# Second case:
Product name: "Melon"
Price: xyz

Salida Esperada:

Error: price must be a positive number.


"""
# Conclusiones
"""
Para terminar con este tema, me parecio muy interesante pues con el uso de strings pudimos
apreciar con cada uno de los ejercicios, como se implementan en diferentes situaciones
para poder realizar diferentes funciones, cuando usamos .upper() o .lower() para hacer
que los textos ingresados coincidan con nuestro codigo y evitar que el codigo se estropee
y genere errores, strip() funciona para quitar los espacios que no vayamos a utilizar,
split() cuando necesitamos dividir la cadena en varias partes como lo fue en el caso del
nombre completo pues lo dividiamos en nombre y apellidos para poder conseguir las iniciales,
join() funciona para unir los elementos como listas o tuplas em una sola cadena.
"""

# References:
"""
1) Cadenas Python W3 schools: https://www.w3schools.com/python/python_strings.asp
2) Tipos de datos de Python_geeksforgeeks: https://www.geeksforgeeks.org/python/python-data-types/
3) ¿QUÉ es una CADENA de CARACTERES en PYTHON? ⛓️ - [ STRINGS ] - Curso PYTHON desde CERO #8: https://www.youtube.com/watch?v=IydiGm6HpMs
4) Métodos de Cadenas de STRING en PYTHON desde CERO ⛓ Principiantes # 012: https://www.youtube.com/watch?v=CSGedJV6Yv8
5) 💻¿Qué son los Strings en Python? ¡Aprende a Manipular Cadenas! 🚀: https://www.youtube.com/watch?v=W8EqQzpmx7A
6) Entrada de usuario de Python: Manipulación, validación y buenas prácticas: https://www.datacamp.com/es/tutorial/python-user-input
"""