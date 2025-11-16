# SLICING
players = ["cr7", "messi", "Travis", "chicha", "corona"]
print(players[0:3])
# Slice es trabajar con un grupo especifico de elementos de una lista

print(players[1:4]) # ["messi", "Travis", "chicha"]
print(players[:4])  # ["cr7", "messi", "Travis", "chicha"]
print(players[2:]) # ["Travis", "chicha"]

print(players[-3:])
print(players[-3:-1])
print(players[4:2]) # LISTA VACIA PORQUE NO SE PUEDE EMPEZAR DESDE EL 4 Y VOLVER AL 2 SI NO ES NUMERO NEGATIVO

# PLAYERS
players = ["axel", "ignacio", "Travis", "chicha", "corona", "jorge"]
first_three_player = players[0:3]
print("first_three_players: ", first_three_player)

print("Aqui vienen los tres mejores alumnos del salon: ")
for player in players[0:3]
    print(player.upper())

# Copia de listas
my_food = ["pizza", "gorditas de jaumave", "machacado"]
# MANERA ERRONEA DE COPIAR UNA LISTA,   copy_of_food = my_food

copy_of_food_1 = my_food[:]
copy_of_food_2 = my_food.copy()
copy_of_food_3 = list(my_food)
"""
LAS LISTAS SON ELEMENTOS MUTABLES, QUE PUEDO HACER ELEMENTOS MAS GRANDES O REDUCIRLOS, PYTHON APARTA UN LUGAR DE MEMORIA
APARTA UN ESPACIO PARA ESA VARIABLE, ESO LO HACE PYTHON, CUANDO SE HACEN LISTAS SE APARTA UN ESPACIO,
LAS TUPLAS SE DEFINEN UN TAMAÑO DE UNA LISTA CON 5 ELEMENTOS, VA A TENER 5 ELEMENTOS PARA SIEMPRE OSEA SON INMUTABLES PORQUE
YA TIENEN UN VALOR FIJO Y NO SE PODRAN AGREGAR Y QUITAR.

LISTAS MUTABLES, TUPLAS INMUTABLES.
"""

# Modificando elementos
cars = ["bwm", "porch", "masda", "totoya", "ford"]
cars[0]="bmw"
cars[1]="porshe"
cars[2]="mazda"
cars[3]="toyota"