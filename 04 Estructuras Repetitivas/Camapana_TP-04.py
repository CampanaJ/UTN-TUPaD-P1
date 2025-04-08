#1) Imprimir números del 0 al 100.

for i in range(101):
    print(i)

#2) Contar la cantidad de dígitos de un número entero.

numero = int(input("Ingresa un número entero: "))
cantidad_digitos = len(str(abs(numero)))
print("Cantidad de dígitos:", cantidad_digitos)

#3) Sumar números entre dos valores dados.

inicio = int(input("Ingresa el primer número: "))
fin = int(input("Ingresa el segundo número: "))
suma = 0
for i in range(inicio + 1, fin):
    suma += i
print("La suma de los números entre", inicio, "y", fin, "es:", suma)

#4) Sumar números hasta que el usuario ingrese 0.

suma_total = 0
while True:
    numero = int(input("Ingresa un número entero (0 para terminar): "))
    if numero == 0:
        break
    suma_total += numero
print("Total acumulado:", suma_total)

#5) Juego de adivinar un número entre 0 y 9.

import random

numero_secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if intento == numero_secreto:
        print("¡Correcto! Intentos necesarios:", intentos)
        break
    else:
        print("Intenta de nuevo.")

#6) Imprimir números pares del 0 al 100 en orden decreciente.

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

#7) Sumar números desde 0 hasta un número positivo dado por el usuario.

numero = int(input("Ingresa un número entero positivo: "))
suma = sum(range(numero + 1))
print("La suma es:", suma)

#8) Contar pares, impares, negativos y positivos de 100 números ingresados.

pares = impares = negativos = positivos = 0

for _ in range(100):
    numero = int(input("Ingresa un número entero: "))
if numero % 2 == 0:
    pares += 1
else:
    impares += 1
if numero < 0:
    negativos += 1
elif numero > 0:
    positivos += 1

print("Pares:", pares, "Impares:", impares, "Negativos:", negativos, "Positivos:", positivos)

#9) Calcular la media de 100 números enteros ingresados.

suma = 0

for _ in range(100):
    numero = int(input("Ingresa un número entero: "))
    suma += numero

media = suma / 100
print("La media es:", media)

#10) Invertir el orden de los dígitos de un número.

numero = input("Ingresa un número: ")
numero_invertido = numero[::-1]
print("Número invertido:", numero_invertido)