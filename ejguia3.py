numeros = [2, -29, 0, 12222, 342, -34343, 585, -33, 0, 0]
positivos = negativos = ceros = 0

for n in numeros:
    if n > 0: 
        positivos += 1

    elif n < 0:
        negativos += 1

    else:
        ceros += 1

print(f"positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Ceros: {ceros}")

    

    

