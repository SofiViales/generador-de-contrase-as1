import random 

def generador():

    elements = "+-/*!&$#?=@<>abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    x = int(input("Introduzca la longitud del pase: "))

    if x <= 5:
        while True:
            x = int(input("La longitud es un poco corta. Escribe la longitud de tu contraseña de nuevo:"))
            if x > 5:
                break

    password = ""
    for i in range(x):
        password += random.choice(elements)
        
    print(password)

generador()