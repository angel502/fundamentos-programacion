edades = [12, 8, 7, 13, 15, 16, 17, 18, 19, 14, 11, 9]

for edad in edades:
    if edad < 12:
        print("niño")

    elif edad >= 12 and edad < 18:
        print("Adolescente")

    elif edad >= 18 and edad < 60:
        print("Adulto")

    else:
        print("Adulto mayor")