
def multiplicar(a, b):
    return a * b

# Ejemplo de uso
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

resultado = multiplicar(num1, num2)
print(f"El resultado de la multiplicación es: {resultado}")

print("Presiona (a) para dividir")
opcion = input("Elige una opción:")

if opcion =="a":
    n1 = int(input("Primer numero:"))
    n2 = int(input("Segundo numero:"))
    
    print("Resultado:", n1/n2)
    