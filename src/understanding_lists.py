# Una lista es una coleccion ordenada y mutable de elementos
# Se definen utilizando corchetes y separando los elementos con comas.
# Ejemplo de creacion de una lista
fruits = ["manzana", "banana", "cereza"]
print(fruits) # Salida: ["manzana", "banana", "cereza"]

# Acceso a elementos
print(fruits[0].upper()) # Salida: manzana
print(fruits[1]) # Salida: banana
print(fruits[2].title()) # Salida: cereza

# print(fruits[3]) # Salida: ERROR

# Acceder al ultimo elemento
print(fruits[-1].capitalize()) # Salida: cereza
print(fruits[-2]) # Salida: banana
print(fruits[-3]) # Salida: manzana

my_favorite_fruit = fruits[0]
message = f"Mi fruta favorita es {my_favorite_fruit.title()}."
print(message) # Salida: Mi fruta favorita es Manzana.

"""
 Agregar elementos a una lista
 - append(): Agrega un elento al final de la lista.
"""
print("\n Agregar elementos a una lista: Metodo append() \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.append("ducati")
print(motorcycles)

"""
 Agregar elementos a una lista
  -insert(): Inserta un elemento en una posicion especifica de la lista.
   El metodo insert(index, element) toma dos argumentos:
   el indice donde se desea insertar el elemento y el elemento en si
"""

print("\n Agregar elementos a una lista: Metodo insert \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.insert(-2, "ducati")
print(motorcycles)
print(motorcycles[0])

"""
 Eliminar metodos de una lista
  -del: Elimina un elemento en una posicion especifica de la lista.
  la declaracion del index elimina el elemento de la posicion especificada.
"""
print("\n Eliminar elementos de una lista: declaracion de \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
del motorcycles[0]
print(motorcycles)

"""
Eliminar elemetos de una lista utilizando pop
"""
print("\n Eliminar elementos de una lista: Metodo pop() \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(f"la motocicleta eliminada es: {popped_motorcycle}.")

"""
 Eliminar elementos de una lista con pop(index)
"""

print("\n Eliminar elementos de una lista: Metodo pop(index) \n")
motorcycles = ["honda", "yamaha", "suziki"]
print(motorcycles)
first_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(f"La primera motocicleta eliminada: {first_motorcycle}.")

"""
 Eliminar elementos de una lista con remove()
 El metodo remove(value)
"""
print("\n Eliminar elementos de una lista: Metodo remove() \n")
motorcycles = ["honda", "yamaha", "suzuki", "ducati", "yamaha"]
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)

# Ejemplo practico del metodo remove()
names = ["ana", "juan", "pedro", "maria", "juan"]
print(names)
deleted_names = input("Ingrese el nombre que desea eliminar de la lista: ")
names.remove(deleted_names.strip().lower())
print(names)

"""
 Ordenar listas
 "Metodo de las listas: .sort()"
 Ordenamiento permantente, es decir, ordena las lista para siempre.
"""
cars = ["bmw", "audi", "ford", "kia"]
print(cars)
cars.sort()
print(cars)

"""
 Metodo Reverse
"""
motorcycles = ["mortalica","hona", "ducatti"]
print(motorcycles)
motorcycles.reverse()
print(motorcycles)

"""
 Cantidad de elementos en una lista
 Metodo built-in len()
"""
cars = ["ford","kia","chevrolet"]
print("\n Metodo build-in len")
print(len(cars))

"""
 Metodo built-in
 sorted()
  Ordena una lista temporalmente
"""

favorite_students = ["jorge", "jose", "carlos", "emiliano"]
print(favorite_students)

print("Lista ordenada temporalmente: ", sorted(favorite_students))
print("Lista original: ", favorite_students)
