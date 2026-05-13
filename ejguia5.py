frase = input("Ingrese una frase (sin numeros,guiones,ni nada externo a las letras y espacios): ")

consonantes = vocales = espacios = 0

for caracter in frase.lower():
    if caracter in "aeiou":
        vocales += 1
    elif caracter == " ":
        espacios += 1

    elif caracter >= "a" and caracter <= "z":
        consonantes += 1

print(f"vocales: {vocales}")
print(f"consonantes: {consonantes}")
print(f"espacios: {espacios}")