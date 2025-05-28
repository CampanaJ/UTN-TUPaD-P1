def factorial(n):
    if n == 0 or n == 1:
        return 1  # Caso base
    else:
        return n * factorial(n - 1)  # Caso recursive

n = int(input("Ingrese un número: "))

for i in range(1, n + 1):
    print(f"Factorial de {i} es {factorial(i)}")
