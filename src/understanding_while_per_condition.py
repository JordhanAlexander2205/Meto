# Contraseñas
"""
    Programa que pida un PIN y despues de 3 intentos fallidos se bloquea
    y uno correcto se muestra el mensaje, Acceso permitido,

    si el usuario se equivoca, el programa debe decirle cuantos intentos le quedan y en caso
    de que no le queden intentos el mensaje debe decir Acceso Denegado, exediste tus intentos
"""

CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3
intents = 0

while intents < MAX_ATTEMPTS:
    user_pin = input("Escribe tu PIN")
    if user_pin == CORRECT_PIN:
        print("ACCESO PERMITIDO")
        break
    else:
        intents+=1
        remaining_attemps = MAX_ATTEMPTS-intents
        if remaining_attemps>0:
            print(f"PIN INCORRECTO {remaining_attemps} Intentos Restantes.")
        else:
            print("Acceso denegado.")
print("Final")

