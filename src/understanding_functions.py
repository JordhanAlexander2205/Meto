# FUNCTIONS
"""
    Las funciones son bloques de codigo diseñados para realizar una tarea especifica.

    Cuando queremos realizar la tarea que se ha definido en una funcion, tenemos que llenar
    el nombre de la funcion responsable de esto.

    Definicion de una funcion (Syntax)

    def name_of_functions(parameters):
        actions 
"""

def greet_mauro():
    print("Hola Mauro, que gusto verte!!!")

def greet(username):
    print(f"Hola {username}, que gusto verte!!!")

def greet(username, msj):
    print(f"Hola {username}, {msj} que gusto verte!!!")


# Argumentos
#greet_mauro()
#greet("Jordhan", "Se te pegaron las cobijas")

"""
    Vamos a realizar un programa que genere el nombre completo de una persona.

    Vamos a pasar el primer nombre, el segundo y el apellido.

    La funcion debe generar el nombre completo y regresarlo.
"""
def create_full_name(first_name, middle_name, last_name):
    """
        Docstrings - Jorge This function creates the fullname
        of a person give its three names
    """

    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name

user_first_name = input("Escribe tu primer nombre: ").strip().lower()
user_middle_name = input("Escribe tu segundo nombre: ").strip().lower()
user_last_name = input("Escribe Tu apellido: ").strip().lower()

# Argumentos Posicionales -> Positional Arguments
print(create_full_name(user_first_name, user_middle_name, user_last_name))
# Argumentos Posicionales -> Positional Arguments
full_name = create_full_name(user_first_name, user_middle_name, user_last_name)
print(full_name)


# Argumentos Clave -> Keyword Arguments
full_name_key = create_full_name(
    last_name = user_last_name,
    first_name = user_first_name,
    middle_name = user_middle_name
)
print(full_name_key)


for i in range(10):
    greet_mauro()



# Parametros opcionales
profe_falso = create_full_name(user_first_name, user_last_name)
print(profe_falso)



# Temas para estudiar a futuro
# Funciones: args, kwargs -> en funciones
# Manejo de datos: Abrir archivos csv, .json, .yml, .txt, .xls, .doc, .pdf
# Argumentos por linea de comandos: -sys
# cli - command line interface
# Generadores, iteradores, yield
# testing -> 