nota = input("ingrese su nota: ")
nota = float(nota)

if 90 < nota < 100:
    print("Excelente!")
elif 80 < nota < 89:
    print("Muy bueno")
elif 70 < nota < 79:
    print("Bueno")
elif 60 < nota < 69:
    print("Suficiente")
elif 0 < nota < 59:
    print("Insuficiente")