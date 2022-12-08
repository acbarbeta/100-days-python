# Decidi modificar este projeto para não perguntar o número de cada tipo de caracter ao usuário. O gerador fornecerá uma senha randômica contendo entre  8 e 20 caracteres, sendo ao menos um símbolo, uma letra maiúscula e um número.

import random


MIN_CHAR = 8
MAX_CHAR = 20

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+']
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_char = random.randint(MIN_CHAR,MAX_CHAR)

password = []

password.append(random.choice(capital_letters))
password.append(random.choice(symbols))
password.append(random.choice(numbers))

for item in range(nr_char - 3):
    password.append(random.choice(char))

random.shuffle(password)

final_password = ""
for char in password:
    final_password += char

print(final_password)

