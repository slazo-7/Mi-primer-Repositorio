import random
a = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
b = int(input("¿Cual es la longitud de la contraseña?"))
password = ""
for i in range(b):
    z = random.choice(a)
  password += z    
print("La contraseña generada fue:",password)