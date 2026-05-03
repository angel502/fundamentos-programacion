password = input("Ingrese su contraseña: ").strip()

if len(password) >=8 and not password.isalpha() and not password.isnumeric() and password.find(" ") == -1:
    print("Contraseña fuerte puede acceder:")
elif password < 8:
    print("La contraseña debe ser mas fuerte antes de acceder")
else:
    print("La contraseña debe incluir letras y numeros  y no tener espacios.")