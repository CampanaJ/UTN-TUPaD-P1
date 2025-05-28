def decimal_a_binario(n):
    if n == 0:
        return ""  # Caso base: cuando el número es 0, devuelve cadena vacía
    else:
# Calculamos el resto (0 o 1), y llamamos recursivamente con el cociente
        resto = n % 2
        cociente = n // 2
# Concatenamos los resultados en orden correcto
    return decimal_a_binario(cociente) + str(resto)

# Función auxiliar para manejar el caso cuando n es 0 inicialmente
def convertir_decimal_a_binario(n):
    if n == 0:
        return "0"
    else:
        return decimal_a_binario(n)

# Ejemplo:
numero = int(input("Ingrese un número en decimal: "))
binario = convertir_decimal_a_binario(numero)

print(f"El número {numero} en binario es: {binario}")