"""
Un string es de manera sencilla una serie de caracteres.
En python todo lo que se encuentre dentro de comillas simples
'' o dobles comillas "" es considerado un string.

    "Este es un string"
    'Esto tambien es un string'

    'Le dije a un amigo, "Python es mi lenguaje favorito"'
    "El lenguaje 'Python' lleva el nombre por Monty Python,
    no por la serpiente"
"""


name = "clase de programacion"
print(name)
print(name.title())
print(name)


"""
Un metodo es una accion que Python puede realizar en un fragmento de datos o sobre una variable.

El punto . despues de una variable seguida del metodo title(), dice que se tiene que ejecutar
el metodo title() de la variable name.

Todos los metodos van seguidos de parentesis, porque en ocasiones necesitan informacion adicional
para funcionar, en esta ocasion el metodo .title() no requiere informacion adicional para ejecutarse.
"""

print(name.upper())
print(name.lower())

# Concatenacion de STRINGS
print("CONCATENACION DE STRINGS")
first_name = "charly"
last_name = "mercury"
full_name = first_name +" "+ last_name
print(full_name)

print("Hola, " + full_name.title() + "!")


message = "Una fortaleza de Python es su comunidad"
print(message)

message = "Una fortaleza de 'Python' es su comunidad"
print(message)

# Concatenacion con f-strings
famous_person = "Charly Mecury"
quote = "Python is love"

message = famous_person +" una vez dijo que "+ quote
print(message)

# Concatenacion con fstring
message_f_string = f"{famous_person} una vez dijo {quote}"
print(message_f_string)

# Actividad
"""
Elije un personaje famoso e igualalo a una variable string
Elije una frase famosa que el dijo y igualalo a una variable tipo string
Genera un mensaje con las 2 variables utilizando fstring
Imprime mensaje
"""
famous = "Jose Jose"
phrase = "Ya lo pasado es pasado"

message = famous +" Una vez dijo que "+ phrase
print(message)

message_f_string = f"{famous} Una vez dijo {phrase}"
print(message_f_string)



# Withespaces
"""
 Se refiere a cualquier caracter que no se imprime, es decir, un tabulador y finales de linea.
 Los whitespaces se utilizan comunmente para organizar las salidas (prints)
 de tal manera que sea mas amigable de leer o ver para los usuarios.
"""

# Ejemplos
print("Python")
print("\t Python")
print("\t\t Python")

# Ejemplo de salto de linea
print("Languages: \n Python \n C \n Javascript")
print("Carlos")
print("Tovar")

message = """
 Esta clase es de programacion

 Mis alumnos son buena onda
             Metodologias de la Programacion

"""

print(message)
message = "\n\t Esta clase es de programacion \n\t Mis alumnos son buena onda \n\t\t\t Metodologias de la programacion"

# Eliminacion de espacios en blanco
programming_languages = " Python "
print(programming_languages)
print(programming_languages.lstrip())
print(programming_languages.rstrip())
print(programming_languages.strip())