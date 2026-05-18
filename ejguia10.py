precios = [50 , 35, 100, 2000, 40, 20 ,1000]

for precio in precios:
    if precio > 100:
        total = precio * 0.80
        print(f"{precio} + 20% de descuento = {total}")
    elif precio >= 50 and precios < 100:
        total = precio * 0.90
        print(f"{precio} + 10% de descuento = {total}")
    else:
        print(f"{precio}, sin descuento")