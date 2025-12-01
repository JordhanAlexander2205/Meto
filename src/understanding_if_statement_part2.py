"""
    Vamos a realizar un programa que pregunte al usuario por su edad y muestre al usuario
    por su edad y muestre un mensaje diferente segun el rango de edad en el que se encuentre:
"""
try:
    age = int(input("Por favor, introduce tu edad: "))
except:
    age = -1
    print("Tuviste un error, ingresaste un caracter negativo")

if age > 100:
    print("Tienes mas de un siglo de vida")
elif age >= 18 and age <= 100:
    print("Eres Mayor de Edad")
elif age < 18 and age >= 0:
    print("Eres un menor de edad")
else:
    print("Edad no valida")

print("Hola Charly")

"""
    Hacer un programa que pregunte la edad de una persona y responda lo siguiente:
        -Si la edad es menor o igual a 4, la entrada es gratuita
        -Si la edad es menor o igual a 18, pero mayor a 4, entonces la entrada cuesta
        $200
        -Si la entrada es mayor que 18, entonces la entrada cuesta $400.
"""
try:
    age = int(input("Por favor, ingresa tu edad: "))
except:
    age = -1
    print("Tuviste un error, ingresaste un caracter negativo")

if age <= 4:
    print("La entrada es gratuita")

elif age <= 18 and 4:
    print("La entrada cuesta $200")
elif age > 18:
    print("La entrada cuesta $400")


# Multiple if
guisos = ["deshebrada", "asado", "salsa verde", "pozole"]
if "asado" in guisos:
    print("si hay asado")
if "tamales" in guisos:
    print("Hay tamales")
if "salsa verde" in guisos:
    print("Si hay salsa verde")
else:
    print("No hay salsa verde")