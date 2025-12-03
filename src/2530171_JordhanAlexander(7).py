# CRUD
"""
METODOLOGIAS DE LA PROGRAMACION:
    MAESTRO: CARLOS ANTONIO TOVAR GARCIA
        CARRERA: MECATRONICA
        ALUMNO: JORDHAN ALEXANDER MARIANO RAMIREZ
        MATRICULA: 2530171
"""

# RESUMEN EJECUTIVO:
"""
- ¿Qué es un CRUD y qué significan Create, Read, Update, Delete?
Un CRUD es un conjunto básico de operaciones que se usan para gestionar datos en cualquier sistema
(bases de datos, archivos, diccionarios en Python, etc.).
SE DIVIDE EN SIGLAS:
C- Create
R- Read
U- Update
D- Delete

- ¿Qué estructura de datos elegiste (dict o list de dicts) y por qué?
En el programa presentado se usa la estructura dict.

Se prefirio en mi caso utilizar dict porque puedo buscar un objeto mediante su ID que a su vez se evitan objetos duplicados debido
a que un ID siempre debe ser unico, con la unica excepcion de poder usar un caracter distinto para que el programa lo detecte como
uno completamente distinto y el codigo esta estructurado de manera mas ordenada

- ¿Cómo te ayuda usar funciones para organizar la lógica del CRUD?

Separan la lógica, debido a que cada operacion tiene una funcion distinta para todos los casos.
-create_item
-read_item
-update_item
-delete_item
-list_items

Puedo reutilizar lineas de codigo con solo llamarlas de nuevo sin la necesidad de volver a escribir todo de nuevo de manera
repetitiva,
por ejemplo:
create_item(items, id, name, price, quantity),

Ayuda a detectar errores y probar el codigo sin necesidad de revisar de manera abrumadora las lineas de codigo.

- ¿Qué cubre tu programa?: menú principal, operación de creación, lectura, actualización, eliminación y listado de elementos.
El programa contiene un menu principal que podremos elegir la opcion que necesitemos como por ejemplo, para crear un nuevo objeto,
leer objetos, actualizar los valores, borrar objetos, mostrar la lista de los objetos existentes y incluso para finalizar mi
programa con solo teclear el numero 0,

La operacion Create solicita al usuario que ingrese el ID, nombre, precio y la cantidad del objeto que quiere registrar,

La opcion de Read permite leer y verificar si un objeto existe mediante su ID,

Update nos permite modificar tanto el nombre, el precio y la cantidad de un objeto ya registrado anteriormente,

Delete nos permite borrar objetos mediante su ID, asi como verifica si se elimino correctamente

List mostrara un listado de todos los objetos registrados, al no tener registrado un objeto previamente mostrara el mensaje de
"No items", para indicarnos que el diccionario esta vacio.
"""

def create_item(items, item_id, name, price, quantity):
    if item_id in items:      # no permitir duplicados
        return False
    items[item_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    return True


def read_item(items, item_id):
    return items.get(item_id)


def update_item(items, item_id, name, price, quantity):
    if item_id not in items:
        return False
    items[item_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    return True


def delete_item(items, item_id):
    if item_id not in items:
        return False
    del items[item_id]
    return True


def list_items(items):
    if not items:
        print("No items")
    else:
        for item_id, data in items.items():
            print(f"{item_id} -> {data}")


def main():
    items = {}

    while True:
        print("\n1) Create item")
        print("2) Read item")
        print("3) Update item")
        print("4) Delete item")
        print("5) List all items")
        print("0) Exit")

        option = input("Choose option: ").strip()

        if option not in {"0", "1", "2", "3", "4", "5"}:
            print("Error: invalid input")
            continue

        if option == "0":
            print("Bye!")
            break

        # CREATE
        if option == "1":
            item_id = input("ID: ").strip()
            name = input("Name: ").strip()

            try:
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))
            except ValueError:
                print("Error: invalid input")
                continue

            if price < 0 or quantity < 0 or not item_id:
                print("Error: invalid input")
                continue

            if create_item(items, item_id, name, price, quantity):
                print("Item created")
            else:
                print("Error: ID already exists")

        # READ
        elif option == "2":
            item_id = input("ID: ").strip()
            if not item_id:
                print("Error: invalid input")
                continue

            item = read_item(items, item_id)
            if item is None:
                print("Item not found")
            else:
                print(item)

        # UPDATE
        elif option == "3":
            item_id = input("ID: ").strip()
            if item_id not in items:
                print("Item not found")
                continue

            name = input("New name: ").strip()
            try:
                price = float(input("New price: "))
                quantity = int(input("New quantity: "))
            except ValueError:
                print("Error: invalid input")
                continue

            if price < 0 or quantity < 0:
                print("Error: invalid input")
                continue

            update_item(items, item_id, name, price, quantity)
            print("Item updated")

        # DELETE
        elif option == "4":
            item_id = input("ID: ").strip()
            if delete_item(items, item_id):
                print("Item deleted")
            else:
                print("Item not found")

        # LIST
        elif option == "5":
            print("Items list:")
            list_items(items)

if __name__ == "__main__":
    main()

# CASO USO:

# NORMAL:
"""
-Create item:
Inputs: ID="A001", Name="Laptop", Price=1500.0, Quantity=5

Resultado esperado: "Item created" y el item se agrega al diccionario.

-Read item:
Input: ID="A001" (existente)

Resultado esperado: {'name': 'Laptop', 'price': 1500.0, 'quantity': 5}

-Update item:
Inputs: ID="A001", New Name="Laptop Pro", Price=1600.0, Quantity=6

Resultado esperado: "Item updated" y item modificado en el diccionario.

-Delete item:
Input: ID="A001"

Resultado esperado: "Item deleted" y item eliminado del diccionario.
"""

# BORDE:
"""
-Create item:
Inputs: ID="A002", Name="Mouse", Price=0.0, Quantity=0

Resultado esperado: "Item created" (valores mínimos permitidos).

-Read item:
Input: ID="A002" (último item agregado con valores mínimos)

Resultado esperado: {'name': 'Mouse', 'price': 0.0, 'quantity': 0}

-Update item:
Inputs: ID="A002", New Name="Mouse Basic", Price=0.0, Quantity=0

Resultado esperado: "Item updated" (valores mínimos permitidos).

-Delete item:
Input: ID="A002" (último item)

Resultado esperado: "Item deleted" y diccionario queda vacío.
"""

# ERROR:
"""
-Create item:
Inputs: ID="A001" (duplicado), Name="Keyboard", Price=500.0, Quantity=2

Resultado esperado: "Error: ID already exists".

-Read item:
Input: ID="A999" (no existe)

Resultado esperado: "Item not found".

-Update item:
Inputs: ID="A999" (no existe), cualquier nombre, precio y cantidad

Resultado esperado: "Item not found".

-Delete item:
Input: ID="A999" (no existe)

Resultado esperado: "Item not found".
"""

# References
"""
1) Documentacion Python: https://docs.python.org/3/tutorial/datastructures.html
2) Python Geeks: https://www.geeksforgeeks.org/python/python-dictionary/
3) DataCamp: https://www.datacamp.com/tutorial/functions-python-tutorial
4) ¿Cómo hacer un CRUD (Guardar, Mostrar, Modificar y Eliminar) con Python y MySQL? FÁCIL Y SENCILLO: https://www.youtube.com/watch?v=Ro2m95m8QkI
5) COMO HACER UN CRUD CON PYTHON Y MYSQL UTILIZANDO FLASK | COMPLETO: https://www.youtube.com/watch?v=QS2uiRedr1U
"""
