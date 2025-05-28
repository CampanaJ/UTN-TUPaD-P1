def fibonacci(n):
    if n == 0:
        return 0  # Caso base
    elif n == 1:
        return 1  # Caso base
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Caso recursivo
    
n = int(input("Ingrese la posición hasta donde quiere mostrar la serie de Fibonacci: "))

for i in range(n + 1):
    print(f"Fibonacci en posición {i} es {fibonacci(i)}")