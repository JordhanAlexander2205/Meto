"""
 Las tuplas son listas inmutables
 se utilizan los () para definir una tupla.

 Ejemplo:
"""
# Rectangulo (ancho, alto)
rectangle_dimensions = (200, 50) # Tupla
print(f"largo: {rectangle_dimensions[0]} mm")
print(f"ancho: {rectangle_dimensions[1]} mm")

# Vamos a modificar una tupla
# rectangle_dimensions[0] = 250 # Error tipo TypeError
# rectangle_dimensions[1] = 100 # Error tipo TypeError

for dimension in rectangle_dimensions:
    print(dimension)

"""
    No podemos modificar una tupla, ni tampoco agregar/eliminar elementos.
    Lo que si podemos hacer es cambiar la asignacion a una variable que almacena
    una tupla.
"""
rectangle_dimensions = (300, 150, 50) # Tupla

