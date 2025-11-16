cars = ["audi", "Bwm", "subaru", "toyota"]
for car in cars:
    if car=="bmw":
        print(car.upper())
    else:
        print(car)


# El condicional es el corazon de un if
# Condicional
car = "bmw"
print(car=="bmw") # True

# Condicional False
car = "Audi"
print(car=="audi")

# Posible solucion a la entrada del usuario
car = "Audi"
print(car.lower()=="audi") # True

# Operador relacional ! = para determinar desigualdad
requested_topping = "mushroom"
if requested_topping != "anchovies":
    print("Hold the anchovies")

# Comparaciones numericas
age = 18 # Entero
print(age==18) # True

answer = 17
if answer != 42:
    print("Esa no es la respuesta correcta. Intenta otra vez")


age = 17
print(age < 21 ) # True
print(age <= 21) # True
print(age > 21) # False
print(age >= 21) # False


# Multiples condiciones
age_0 = 22
age_1 = 18
# Operacion and
print(age_0 >= 21 and age_1 >= 21) # False
print(age_0 >= 21 and age_1 >= 18) # True

# Operacion or (ESTE ES MAS FLEXIBLE QUE EL AND)
print(age_0 >= 21 or age_1 >= 21) # True
print(age_0 >= 21 or age_1 >= 21) # False

"""
    Para preguntarnos si un valor especifico
    esta en una lista, podemos utilizar el siguiente comparador:

    value in list
"""

motorcycles = ["mortalica", "honda", "vento", "yamaha"]
moto_charly_wants = "italica"
print(moto_charly_wants in motorcycles) # False
print("honda" in motorcycles) # True

"""
    Para preguntarnos si un valor especifico
    esta en una lista, podemos utilizar el siguiente comparador:

    value not in list
"""

banned_students = ["jorge", "carlos", "moyra", "luz", "hots"]
user = "mauro"
print(user not in banned_students) # True
print("jorge" not in banned_students) # True


## Variables del tipo booleano
game_active = True
can_edit = False

"""
    if statement

    sintax:

    if condition:
        do something

    if condition:
        do something
    
    else:
        do something
"""

age = input("\n ¿Dime cual es tu edad?")
print(age)

if int(age) >=18:
    print("Tu tienes la edad suficiente para votar")
else:
    print("Tu eres menor de edad")
