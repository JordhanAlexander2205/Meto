# Simple dictionary
alien_0 = {"color": "green","points":5}

# The simpliest dictionary
alien_1 = {"color": "yellow"}

# Empty dictionary
alien_2 = {}


# Modifying values in a dictionary
alien_2 = {"color": "yellow"}
alien_2["color"] = "blue"

# Adding new key-value pairs
alien_2["x_position"] = 0
alien_2["y_position"] = 25

print(alien_2)

## Dictionary to store similar objects
favorite_languages = {
    "jen": "python", 
    "sarah":"c", 
    "edward": "rubi",
    "phil":"python"
}

# print(f"Sarah favorite language is {favorite_languages["sarah"]}")

# Looping through
for key, value in favorite_languages.items():
    print(f"{key.title()}s favorite languaje is {value.title()}.")




for key in favorite_languages.keys()
    print(key)


for value in favorite_languages.values()
    print(value)

# NESTING DICTIONARIES
"""
Nesting dictionaries significa guardar un diccionario dentro de otro, igual que "cajas dentro de cajas".
Esto te permite organizar datos complejos de manera estructurada.

students = {
    "001": {"name": "Ana", "age": 20, "grade": 9.5},
    "002": {"name": "Luis", "age": 22, "grade": 8.7},
    "003": {"name": "María", "age": 21, "grade": 9.0}
}

"""
## LISTAS DE DICCIONARIOS
"""
Una lista de diccionarios es una estructura donde cada elemento de la lista es un diccionario.
Esto se usa muchísimo para representar colecciones de objetos, similar a filas en una base de datos.

people = [
    {"name": "Ana", "age": 20},
    {"name": "Luis", "age": 22},
    {"name": "María", "age": 21}
]

"""

## LISTAS EN DICCIONARIOS
"""
Un diccionario puede contener listas como valores.
Esto es útil cuando un elemento tiene múltiples datos del mismo tipo.

student = {
    "name": "Ana",
    "grades": [9, 10, 8, 9]
}

print(student["name"])       # Ana
print(student["grades"][1])  # 10

"""
## DICCIONARIOS EN DICCIONARIOS
"""
Un diccionario puede contener otros diccionarios como valores.
Esto sirve para organizar datos complejos con estructura jerárquica.

students = {
    "001": {"name": "Ana", "age": 20},
    "002": {"name": "Luis", "age": 22},
    "003": {"name": "María", "age": 21}
}

print(students["001"]["name"])  # Ana
print(students["003"]["age"])   # 21
"""

# Diccionario
covenant = {
    "color": "red",
    "weapon": "sword"
    "armament":"armor"
    "healt": 3,

}


covenant_elite = {
    "color": "blue",
    "weapon": "plasma-sword"
    "armament":"armor"
    "healt": 5,

}

# Lista de diccionario
covenants = [
    covenant
    covenant_elite    
]

for covenant in covenants:
    print ("/n", covenant)
    for key, value in covenant.items():
        print(key, value)
    print()



# Lista en diccionarios
students = {
    "jorge" = ["reprobado", "jaumave", "toreto"],
    "lizarriturri": ["aprobado", "cbtis271", "migajero"]
}

# Diccionarios en Diccionarios
sensors = {
    "temperature": {
        "id": "temp_1",
        "location": "aula 205",
        "value":25,
        "unit": "celsius",
        "calibration": {
            "date": "2024-01-15",
            "tecnichian": "Juan Perez",
        }
    }
}


print("Temperatura")
print(sensors["temperature"]["value"])