import math
print("hola chicos")

x = int(input("Elige un numero:"))
y = input("Elige lo que quieres hacer con el numero: (restar, sumar, multiplicar, dividir, raiz cuadrada)")

if y == "raiz cuadrada":
    if x >= 0:
        root = math.sqrt(x)
        print("La raiz cuadrada de", x, "es", root)
    else:
        print("Syntax Error")

