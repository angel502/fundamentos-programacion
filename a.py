precio = float(input("Ingrese el preio de su producto: "))
socio = input("¿Usted es socio? (s/n): ")

if socio == "s" and precio > 50000:

    print("Felicidades obtuvo un descuento del 20%")

    descuento = 0.20

elif socio == "n" and precio > 50000:
    print("Obtuvo un 10%, de descuento por no ser socio")
    descuento = 0.10
elif socio == "s" and precio < 50000:
    print("solo obtuvo un 5%, de descuento estimado socio")
    descuento = 0.05
else:

    print("No tiene descuento")
    descuento = 0

final = precio * (1 - descuento)
print (f"Precio final de su producto: ${final: .1f}")