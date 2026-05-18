secreto = 18
intentos = [10, 18, 50, 40, 30]
i = 0

while i < len(intentos):
    if intentos[i] == secreto:
        print("Adivinaste el numero")
        break
    elif intentos[i] < secreto:
        print(f"{intentos[i]} es menor al secreto")
    elif intentos[i] > secreto:
        print(f"{intentos[i]}, es mayor al secreto")
    i += 1