#Ejercicio 1:

#Programa que solicita la edad del usuario.

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

#Ejercicio 2:

#Programa que solicita la nota del usuario.

nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3:

#Programa que permite ingresar solo números pares.

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio 4:

#Programa que clasifica la edad del usuario.

edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#Ejercicio 5:

#Programa que valida la longitud de una contraseña.

contrasena = input("Ingrese su contraseña (8 a 14 caracteres): ")
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6:

#Programa que calcula moda, mediana y media y determina el sesgo.

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana > moda:
    resultado = "Sesgo positivo"
elif media < mediana < moda:
    resultado = "Sesgo negativo"
else:
    resultado = "Sin sesgo"

print(f"Moda: {moda}, Mediana: {mediana}, Media: {media}, Resultado: {resultado}")

#Ejercicio 7:

#Programa que agrega un signo de exclamación si el string termina en vocal.

frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in 'aeiou':
    print(frase + "!")
else:
    print(frase)

#Ejercicio 8:

#Programa que modifica el nombre según la opción seleccionada.

nombre = input("Ingrese su nombre: ")
opcion = int(input("Seleccione una opción: 1) Mayúsculas 2) Minúsculas 3) Primera letra mayúscula: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida")

#Ejercicio 9:

#Programa que clasifica la magnitud de un terremoto.

magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#Ejercicio 10:

#Programa que determina la estación del año según la fecha y el hemisferio.

hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

if hemisferio == 'N':
        if (mes == 12 and dia >= 21) or (mes <= 3 and mes != 3) or (mes == 3 and dia <= 20):
           print("Invierno")
        elif (mes == 3 and dia >= 21) or (mes <= 6 and mes != 6) or (mes == 6 and dia <= 20):
            print("Primavera")
        elif (mes == 6 and dia >= 21) or (mes <= 9 and mes != 9) or (mes == 9 and dia <= 20):
            print("Verano")
        else:
            print("Otoño")
else:
        if (mes == 12 and dia >= 21) or (mes <= 3 and mes != 3) or (mes == 3 and dia <= 20):
            print("Verano")
        elif (mes == 3 and dia >= 21) or (mes <= 6 and mes != 6) or (mes == 6 and dia <= 20):
            print("Otoño")
        elif (mes == 6 and dia >= 21) or (mes <= 9 and mes != 9) or (mes == 9 and dia <= 20):
            print("Invierno")
        else:
            print("Primavera")