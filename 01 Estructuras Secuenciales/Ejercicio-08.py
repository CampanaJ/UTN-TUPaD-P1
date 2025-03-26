try:
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))
    
    if altura <= 0:
        print("La altura debe ser mayor que cero.")
    else:
        imc = peso / (altura ** 2)
        print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
except ValueError:
    print("Por favor, ingresa valores numéricos válidos.")