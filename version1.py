import random 
elements = "+-/*!&$#?=@<>abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
pass_length = int(input("Introduzca la longitud del pase: "))

if x <= 5:
    while true:
        x = int(input("La longitud es un poco corta. Escribe la longitud de tu contraseña de nuevo:"))
        if x > 5:
            break

password = ""
for i in range(pass_length):
    password += random.choice(elements)
    
print(password)