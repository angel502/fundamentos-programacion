secreto = 18 

intento = int(input("Ingrese un intento para adivinar el numero secreto"))


while intento != secreto :
    if intento > secreto:
        print("Es menor")

    elif intento < secreto:
        print("Es mayor")

    intento = int(input("Ingrese un intento para adivinar el numero secreto"))

if intento == secreto:
    print("Felicidades acertaste el numero secreto")