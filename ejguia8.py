numero = int(input("Ingrese de que numero quiere saber la tabla de multiplicacion hasta el 10: "))

if numero > 0:
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")