for numero in range (2, 31):
    es_primo = True
    for divisor in range (2,numero):
        if numero % divisor == 0:
            es_primo = False
            break


    
    if es_primo:
        print(f"{numero}, Es primo")
    else:
        print(f"{numero}, No es primo")