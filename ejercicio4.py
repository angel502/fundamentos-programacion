pasajero = int(input("Ingrese su edad señor pasajero: "))

if pasajero < 12:
    print("es un niño asi que pasa gratis")
elif pasajero <= 17:
    print("Es un adolescente asi que paga la mitad")

elif pasajero >= 18 and pasajero <= 64:
    print("es un adulto asi que paga tarifa completa")

elif pasajero >= 65:
    print("es un Adulto mayor asi que paga media tarifa")

else:
    print("Ingrese su edad en numeros, sin meses.")