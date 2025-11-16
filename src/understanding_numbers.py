# Numbers

"""
Integers - Enteros
Son numeros sin punto decimal,
-infty , ..., -2, -1, 0, 1, 2, ..., infty

Ejemplo:
# Tipado dinamico
age = 33

Los podemos sumar(+), restar(-), multiplicar(*) y dividir(/).

Potencias (**2, **3, **4)

Modulo (Dividendo%Divisor)
"""

number_1 = 33
number_2 = 13

suma = number_1 + number_2
difference = number_1 - number_2
multiplication = number_1 * number_2
division = number_1/number_2
modulo = number_1%number_2
power = number_1**number_2

print("suma", suma)
print("difference", difference)
print("multiplication", multiplication)
print("division", division)
print("modulo", modulo)
print("power", power)

print("La suma es de tipo", type(suma))
print("La diferencia es de tipo", type(difference))
print("La multiplicacion es de tipo", type(multiplication))
print("La division es de tipo", type(division))
print("El modulo es de tipo", type(modulo))
print("El Power es de tipo", type(power))

# Floats

print(0.1+0.1)
print(0.2-0.2)
print(2*0.1)
print(2*0.2)

print(0.2+0.1)
print(3.0+0.1)

### Edad de alguien
age = 33
message = "Charly tiene " + str(age) + " años."
print(message)

"""
 Type error: Python no puede reconocer el tipo de informacion que se esta utilizando.
 Para convertir a string utilizo: str()
"""

message_f = f"Charly tiene {age} años"
print(message_f)
