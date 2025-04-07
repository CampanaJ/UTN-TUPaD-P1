edad = input("Ingrese su Edad: ")
edad = int(edad)

if edad <0:
    print("No")
elif edad > 65:
    print("mas 65")
elif edad > 18:
    print("mas 18")
else:
    print("menor 18")