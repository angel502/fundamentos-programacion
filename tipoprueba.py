vehiculos_pesados = 0
vehiculos_ligeros = 0
while True:
    try:
        vehiculos = int(input("Ingrese cuantos vehiculos desea registrar en esta sesión (numero entero positivo (mayor a 0)): "))

        if vehiculos > 0:
            break
        else:
            print("¡Cantidad invalida! Ingresa un numero entero positivo para continuar")
    except ValueError:
        print(("¡Cantidad invalida! Ingresa un numero entero positivo para continuar"))


for i in range(vehiculos):
    print(f"\n---REGISTRO DEL VEHICULO {i+1}---")

    while True:
        placa = input("Ingrese la placa vehicular: ")
        if len(placa) >= 6 and " " not in placa:
            break
        else:
            print("¡Error de formato! La placa debe tener al menos 6 caracteres y no contener espacios")

    while True:
        capacidad = int(input("Ingrese la capacidad de carga (en toneladas): "))

        try:
            if capacidad > 0:
                break
            else:
                print("Error logistico ingresa un numero entero positivo para la capacidad de carga")
        except ValueError:
            print("Error logistico ingresa un numero entero positivo para la capacidad de carga")

    if capacidad > 55:

        vehiculos_pesados += 1

    else:
        vehiculos_ligeros +=1


print(f"La flota cuenta con {vehiculos_pesados} vehiculos pesados y {vehiculos_ligeros} vehiculos ligeros")


