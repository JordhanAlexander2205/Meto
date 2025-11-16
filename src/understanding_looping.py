magicians = ["ron", "harry", "snape", "hermonie"]
print(magicians[0], magicians[1], magicians[2], magicians[3])

for magician in magicians:
    print(magician)
    print(magician.upper())
    print(f"{magician.title()} ese fue un gran hechizo.")
    print("\n ")
print("Gracias a todos. Fue un gran espectaculo")

"""
 Identacion
    Python utiliza la identacion para determinar cuendo una linea de codigo esta conectada
    a la linea de codigo anterior.

    Basicamente, se utilizan 4 espacios en blanco para obligarnos a escribir codigo ordenado y
    estructurado.
"""

# No olvidemos identar (donde se necesita)
# Ejemplo
magicians = ["alice", "david", "jorge"]
for magician in magicians:
#print(magician) #Error
    print(magician) #Solucion

# Identation Error
# Logical error
magicians = ["alice", "david", "jorge", "candelario"]
for magician in magicians:
    print(magician)
print(f"Great {magician}!, I cant wait to see you next trick")

# LOGICA RESUELTA EN EL ULTIMO "PRINT"
magicians = ["alice", "david", "jorge", "candelario"]
for magician in magicians:
    print(magician)
    print(f"Great {magician}!, I cant wait to see you next trick")

# Identacion innecesaria
message = "Hola Charly"
 print(message) # ES INUTIL BRINCAR AQUI SI NO ES UN FOR O LOOP

#ASI NO
magicians = ["alice", "david", "jorge", "candelario"]
for magician in magicians:
    print(magician)
    print(f"Great {magician}!, I cant wait to see you next trick")
    print("Thank you everyone, that was a great magic show!") # SOLUCION MAL COLOCADA PORQUE REPITE COMO DISCO RAYADO XD

magicians = ["alice", "david", "jorge", "candelario"]
for magician in magicians:
    print(magician)
    print(f"Great {magician}!, I cant wait to see you next trick")
print("Thank you everyone, that was a great magic show!") # asi si


# Error de syntaxis
magicians = ["alice", "david", "jorge", "candelario"]
for magician in magicians: # (SYNTAXERROR): Olvidar colocar los dos puntos (:)
    print(magician)
