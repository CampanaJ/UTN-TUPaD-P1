#Ejercicio 1: Añadir frutas al diccionario precios_frutas

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir las nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Ejercicio 2: Actualizar precios en el diccionario

# Actualizar los precios según lo solicitado
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#Ejercicio 3: Crear una lista con las frutas

# Crear una lista con las frutas
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

#Ejercicio 4: Crear la clase Persona

class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

# Ejemplo de uso
persona1 = Persona("Juan", "Argentina", 30)
persona1.saludar()

#Ejercicio 5: Crear la clase Circulo

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# Ejemplo de uso
circulo1 = Circulo(5)
print(circulo1.calcular_area())
print(circulo1.calcular_perimetro())

#Ejercicio 6: Verificar si una cadena de paréntesis está balanceada

def verificar_balance(pila):
    return not pila

def balancear_parentesis(s):
    pila = []
    for char in s:
        if char in "({[":
            pila.append(char)
        elif char in ")}]":
            if not pila or (char == ')' and pila[-1] != '(') \
                or (char == '}' and pila[-1] != '{') \
                or (char == ']' and pila[-1] != '['):
                return False
            pila.pop()
    return verificar_balance(pila)

# Ejemplo de uso
print(balancear_parentesis("(){}[]"))  # True
print(balancear_parentesis("(]"))      # False

#Ejercicio 7: Usar una cola para simular un sistema de turnos en un banco

from collections import deque

class Banco:
    def __init__(self):
        self.cola = deque()

    def encolar(self, cliente):
        self.cola.append(cliente)

    def desencolar(self):
        return self.cola.popleft() if self.cola else None

    def siguiente_cliente(self):
        return self.cola[0] if self.cola else None

# Ejemplo de uso
banco = Banco()
banco.encolar("Cliente 1")
banco.encolar("Cliente 2")
print(banco.siguiente_cliente())  # Cliente 1
atendido = banco.desencolar()
print(atendido)                   # Cliente 1

#Ejercicio 8: Crear una lista enlazada

class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self. cabeza = None

    def insertar_al_inicio(self, data):
        nuevo_nodo = Nodo(data)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.data)
            actual = actual.siguiente

# Ejemplo de uso
lista = ListaEnlazada()
lista.insertar_al_inicio(10)
lista.insertar_al_inicio(20)
lista.mostrar_lista()

#Ejercicio 9: Invertir una lista enlazada

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" → ")
            actual = actual.siguiente
        print("None")

def invertir_lista_enlazada(lista):
    actual = lista.cabeza
    anterior = None
    while actual:
        siguiente = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente
    lista.cabeza = anterior

# Ejemplo de uso
lista = ListaEnlazada()
lista.insertar_al_inicio(10)
lista.insertar_al_inicio(20)
lista.insertar_al_inicio(30)

print("Lista original:")
lista.mostrar_lista()

invertir_lista_enlazada(lista)

print("Lista invertida:")
lista.mostrar_lista()