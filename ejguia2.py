nota1 = float(input("Ingrese la primera nota para sacar su promedio: "))
nota2 = float(input("ingrese la segunda nota: "))
nota3 = float(input("ingrese la tercera nota: "))
nota4 = float(input("ingrese la cuarta nota: "))
nota5 = float(input("ingrese la quinta nota: "))


notas = [nota1, nota2, nota3, nota4, nota5 ]
suma = 0

for nota in notas:
    suma += nota
    
promedio = suma / len(notas)


if promedio >= 4.0:
    print(f"Aprueba con promedio: {promedio}")

elif promedio >= 3.0 and promedio < 4.0:
    print(f"Habilita con: {promedio}")
else:
    print(f"Reprueba con promedio: {promedio}")