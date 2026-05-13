for numero in range(1,51):
    divisible_3 = numero % 3 == 0
    divisible_7 = numero % 7 == 0

    if divisible_3:
        print(f"numero divisible por 3: {numero}")

    if divisible_7:
        print(f"Numero divisible por 7: {numero}")