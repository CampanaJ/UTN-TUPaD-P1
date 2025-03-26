num1 = int(input("Ingresa el primer número (distinto de 0): "))
num2 = int(input("Ingresa el segundo número (distinto de 0): "))

suma = num1 + num2
resta = num1 - num2
multiplica = num1 * num2
try:
    division = num1 / num2
except ZeroDivisionError:
    division = "No se puede dividir por cero."

print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplica}, División: {division}")
