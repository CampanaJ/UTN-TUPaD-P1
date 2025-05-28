def potencia(n, m):
    if m == 0:
        return 1  # Caso base: cualquier número a la potencia 0 es 1
    else:
        return n * potencia(n, m - 1)  # Caso recursivo
    
base = 2
exponente = 4
resultado = potencia(base, exponente)

print(f"{base} elevado a la potencia {exponente} es {resultado}")