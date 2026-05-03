usuario = input("Ingrese el nombre de usuario: ")

if len(usuario) > 5 and len(usuario) < 15 and usuario[0].isalpha() and usuario.isalnum():
    print(f"Bienvenido {usuario}")

elif usuario <= 5 and usuario >=15:
    print("EL nombre de usuario debe estar entre 6 y 14 caracteres")

else:
    print("El nombre de usuario debe ser alfanumerico y debe empezar con una letra")