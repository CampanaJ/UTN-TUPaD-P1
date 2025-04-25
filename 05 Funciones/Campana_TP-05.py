#1. Función imprimir_hola_mundo:

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#2. Función saludar_usuario(nombre):

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingresa tu nombre: ")
print(saludar_usuario(nombre))

#3. Función informacion_personal(nombre, apellido, edad, residencia):

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#4. Función calcular_area_circulo(radio) y calcular_perimetro_circulo(radio):

import math

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingresa el radio del círculo: "))
print(f"Área del círculo: {calcular_area_circulo(radio)}")
print(f"Perímetro del círculo: {calcular_perimetro_circulo(radio)}")

#5. Función segundos_a_horas(segundos):

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingresa la cantidad de segundos: "))
print(f"Cantidad de horas: {segundos_a_horas(segundos)}")

#6. Función tabla_multiplicar(numero):

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingresa un número para la tabla de multiplicar: "))
tabla_multiplicar(numero)

#7. Función operaciones_basicas(a, b):

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return suma, resta, multiplicacion, division

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}, Resta: {resultados[1]}, Multiplicación: {resultados[2]}, División: {resultados[3]}")

#8 Función calcular_imc(peso, altura):

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

#9. Función celsius_a_fahrenheit(celsius):

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingresa la temperatura en Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"Temperatura en Fahrenheit: {fahrenheit}")

#10. Función calcular_promedio(a, b, c):

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio es: {promedio}")