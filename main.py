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

def multiplicar(a, b):
    return a * b


def restar(a, b):
    return a - b

def dividir(a, b):
    return a / b



resultado = restar(6, 9)

resultado = multiplicar(3, 5)

resultado = dividir(4, 8)