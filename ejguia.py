num1 = int(input("Ingrese el numero por el cual empeza el contador de par o impar: "))

num2 = int(input("Ingrese el numero por el cual terminar: "))


for numero in range(num1, num2):

    if numero % 2 == 0 and numero % 5 == 0:
        print("El numero es par y multiplo de 5")

    elif numero % 2== 0:
        print("El numero es par")

    else:
        print("El numero es impar")