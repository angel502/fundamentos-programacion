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
    elif opcion =="3":
        if texto.isdigit():
            print(f"EL texto '{texto}' Si es un numero (solo digito)")
        else:
            print(f"El texto '{texto}' No es un numero")
    elif opcion == "4":
        if texto.isalpha():
            print(f"El texto {texto} Si contiene solo letras")
        else:
            if texto.isdigit():
                print(f"El texto {texto} Solo contienen numeros")
            elif " " in texto:
                print(f"El texto {texto} Contiene espacios")
            else:
                print(f"El texto {texto} contiene numeros o simbolos")
    
    elif opcion == "5":
        if texto == "":
            print("El texto esta vacio")
        else:
            palabra = input("Que palabra deseas buscar: ")
            posicion = texto.find(palabra)

            if posicion == -1:
                print(f"La palabra {palabra} NO se encontro")

            else:
                print(f"La palabra '{palabra}' esta en la posicion correcta")

    elif opcion == "6":
        if texto =="":
            print("El texto esta vacio")

        else:
            palabras = texto.find()
            cantidad = len(palabras)
            print(f"El texto tiene {cantidad} de palabra(s)")
            print(f"palabras: {palabras}")

    elif opcion == "7":
        longitud = len(texto)
        print(f"El texto '{texto}' tiene {longitud} caracteres")

        if longitud == 0:
            print("El texto esta vacio")

        elif longitud == 1: 
            print("El texto solo tiene 1 caracter")

        else:
            print(f"tiene {longitud} caracteres")

    elif opcion == "8":
        resultado = texto.title()
        print(f"El texto original: {texto}")
        print(f"Formato titulo: {resultado}")

    elif opcion == "9":

        print("\n--- CaLCULADORA BASICA ---")
        print("Operaciones disponibles: + , - , * , / , %")

        num1 = float(input("Ingrese el primer numero: "))
        operador = input("Ingrese el operador (+,-,*,/,%): ")
        num2 = float(input("Ingrese el segundo numero: "))

        print("-" * 55)

        if operador == "+":
            resultado = num1 + num2
            print(f"{num1} + {num2} = {resultado}")

        elif operador == "-":
            resultado = num1 - num2 
            print(f"{num1} - {num2} = {resultado}")

        elif operador == "*":
            resultado = num1 * num2
            print(f"{num1} * {num2} = {resultado}")
        elif operador == "/":
            if num2 != 0:
                resultado = num1 / num2
                print(f"{num1} / {num2} = {resultado}")
            else:
                print("Error, no se puede dividir un numero entre cero")

        elif operador == "%":
            if num2 != 0:
                resultado = num1 % num2
                print(f"{num1} % {num2} = {resultado}")

            else:
                print("Error, no es posible calcular modulo con cero")
        else:
            print(f"operador {operador} no es valido")

    elif opcion == "10":
        print("\n---Comparador de Numeros---")

        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingrese el sdegundo numero: "))

        print("-" * 55)

        if num1 > num2:
            print(f"{num1} es MAYOR que {num2}")

        elif num1 < num2: 
            print(f"{num1} es MENOR que {num2}")

        else:
            print(f"{num1} es IGUAL a {num2}")

        diferencia = num1 - num2
        print(f"La diferencia entre ellos es: {abs(diferencia)}")

    elif opcion == "11":
        print("\n---PAR O IMPAR---")
        numero = int(input("Ingrese un numero entero: "))

        print("-" * 55 )

        if numero % 2 == 0:
            print(f"el numero {numero} es par")
            if numero == 0:
                print("El cero Es un numero  par especial")
            elif numero % 4 == 0:
                print(f"(Ademas, {numero} es multiplo de 4)")
        else:
            print(f"El numero {numero} es impar")
            
            if numero % 5 == 0:
                print(f"(Ademas, {numero}, termina en 5)")
        
        print(f"\nOperacion: {numero} % 2 = {numero % 2}")
        if numero % 2 == 0:
            print("Resudio 0 = ES PAR")
        else: 
            print("Residuo 1 = ES IMPAR")
    else: 
        print(f"ERROR: la opcion '{opcion}' no es Valida")
        print("Porfavor, Elige un numero del 1 al 12")

    input("\nPresiona Enter para continuar....")

print("\n" +  "=" * 55)
print("¡Excelente trabajo! Has practicado:")
print("- Métodos de string")
print("- Operadores aritmeticos (+, -, *, /, %)")
print("- Condicionales (if, elif, else, if anidados)")
print("- Entrada y salida de datos")
print ("=" * 55)   