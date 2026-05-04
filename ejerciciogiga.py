print("=" * 55)
print("       TALLER DE TEXTO Y MATEMATICAS BASICAS")
print("=" * 55)


while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1. Convertir texto a MAYUSCULAS")
    print("2. Convertir texto a minusculas")
    print("3. Verificar si es un numero")
    print("4. Verificar si es solo letras")
    print("5. Buscar una palabra en el texto")
    print("6. Dividir texto en palabras")
    print("7. Contar caracteres del texto")
    print("8. Convertir a formato titulo")
    print("9. Calculadora (+ , - , * , / , %)")
    print("10. Comparar dos numeros")
    print("11. Saber si un numero es par o impar")
    print("12. Salir del programa")

    opcion = input("\nElige una opcion: (1-12): ")

    if opcion == "12":
        print("\nGracias, vuelva pronto a ocupar nuestra glamurosa pagina")
        break


    if opcion in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        texto = input("Ingrese el texto: ")

        print("-" * 55)


    if opcion == "1":
        Resultado = texto.upper()
        print(f"texto original: {texto}")
        print(f"\nTexto en mayusulas {Resultado}")

    elif opcion == "2":
        Resultado = texto.lower()
        print(f"Texto original: {texto}")
        print(f"\nTexto en minusculas: {Resultado}")