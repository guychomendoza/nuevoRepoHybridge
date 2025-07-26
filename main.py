from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def menu():
    while True:
        print("\n=== Calculadora ===")
        print("1. Sumar 2 números")
        print("2. Restar 2 números")
        print("3. Multiplicar 2 números")
        print("4. Dividir 2 números")
        print("5. Suma avanzada (N números)")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", sumar(a, b))

        elif opcion == "2":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", restar(a, b))

        elif opcion == "3":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", multiplicar(a, b))

        elif opcion == "4":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", dividir(a, b))

        elif opcion == "5":
            lista = input("Ingresa los números separados por comas: ")
            numeros = [float(n) for n in lista.split(",")]
            print("Resultado:", suma_avanzada(numeros))

        elif opcion == "6":
            print("Adiós")
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()
