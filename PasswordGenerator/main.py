'''Password generator 1.0 by Harsh'''

import random

chars = 'abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*'
length = int(input("Enter the length of password:"))
password = ""

for a in range(length):
    password += random.choice(chars)

print("password:", password)