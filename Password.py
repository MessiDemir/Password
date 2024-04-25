import random
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Parola uzunluğunu girin: "))
password = ""
for _ in range(uzunluk):
    password += random.choice(characters)
print("Oluşturulan Parola:", password)
