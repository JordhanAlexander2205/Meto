"""
    APLICACION DE LO APRENDIDO EN LAS CLASES DE CHARLY DE PYTHON
"""
# SUMA DE 2 NUMEROS

num1 = input("Dame el primer numero: ")
num2 = input("Dame el segundo numero: ")

num1 = int(num1)
num2 = int(num2)
suma = num1 + num2

print("LA SUMA DE AMBOS NUMEROS ES MAS NI MENOS QUE:", suma)

# LO MISMO PERO AHORA SON 3 NUMEROS Y AGREGANDO UNA RESTA

num1 = input("DAME EL PRIMER NUMERO: ")
num2 = input("DAME EL SEGUNDO NUMERO: ")
num3 = input("Y POR ULTIMO DAME EL TERCER NUMERO: ")


num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

Suma = num1 + num2 + num3
Resta = num1 - num2
Resta2 = num1 - num3
Resta3 = num2 - num3

print("LA SUMA DE LOS 3 NUMEROS QUE ME DISTE ES: ", Suma)
print("LA RESTA ENTRE EL PRIMER NUMERO Y EL SEGUNDO: ", Resta)
print("LA RESTA ENTRE EL PRIMER NUMERO Y EL TERCERO: ", Resta2)
print("LA RESTA ENTRE EL SEGUNDO NUMERO Y EL TERCERO: ", Resta3)

# HAZ QUE PIDA 4 NUMEROS PERO QUE EL PRIMERO MULTIPLIQUE CON EL CUARTO
# EL SEGUNDO RESTE CON EL TERCERO Y LOS 4 NUMEROS SE SUMEN ENTRE TODOS

num1 = input("DAME EL PRIMER NUMERO:")
num2 = input("DAME EL SEGUNDO NUMERO:")
num3 = input("DAME EL TERCER NUMERO:")
num4 = input("DAME UN CUARTO NUMERO:")

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
num4 = int(num4)

suma = num1 + num2 + num3 + num4
resta = num2 - num3
mult = num1 * num4

print("LA SUMA DE TODOS LOS NUMEROS ES DE:", suma)
print("LA RESTA DEL SEGUNDO Y TERCERO ES DE:", resta)
print("LA MULTIPLICACION DEL PRIMER Y CUARTO TERMINO ES DE:", mult)

# DAME UN NUMERO Y TE DIRE SI ES PAR O IMPAR
num = input("DAME UN NUMERO Y TE DIRE SI ES PAR O IMPAR:")

num = int(num)

if num % 2 == 0:
    print("EL NUMERO ES PAR")
else:
    print("ES IMPAR")



# PRACTICANDO ESO DEL IF Y ELSE

# REPASEMOS LO APRENDIDO PERO AHORA QUE ME DIGA SI PAGO SI ES ADULTO, BOLETO PA LA FERIA O NO
age = input("DIME TU EDAD")
print(age)

if int(age) <= 18:
    print("NO PAGAS BOLETO")

else:
    print("ÑIMODO VE ABRIENDO LA CARTERA ME DEBES EL BOLETO")


# HACIENDO LA MISMA WEA PERO USANDO EL MENTADO TRY Y EXCEPT
try:
    Dinero = int(input("DAME MIS 100 PESOS QUE ME DEBES WEY"))
    print(Dinero)
except:
    Dinero =-1
    print("WEY NO ME DES MONEDAS DEVALUADAS")

if Dinero == 100:
    print("GRACIAS CARNAL")

elif Dinero > 100:
    print("CON QUE MUY GENEROSO HOY, MUCHAS GRACIAS :)")

elif Dinero < 100 and Dinero >= 0:
    print("ME FALTA PLATA BRO")





# RECORDEMOS ESA WEA
try:
    Money = int(input("DAME YOUR MONEY PLEASE"))
    print(Money)
except:
    Money = -1
    
if Money == 100:
    print("EXELENT 100 PESOS")

elif Money > 100:
    print("TE PASASTE DE GENEROSO")

elif Money == 0:
    print("0 pesos?")

else:
    print("INVALID CHARACTER")













