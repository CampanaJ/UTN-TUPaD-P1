numeros = []
for i in range(3):
    num = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)
    promedio = sum(numeros) / len(numeros)
print(f"El promedio de los tres números es: {promedio:.2f}")
