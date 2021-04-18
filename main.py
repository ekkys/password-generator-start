#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# print(type(nr_letters))
# print(type(nr_symbols))
# print(type(nr_numbers))

import random

#Membuat perulangan random sebanyak request di input
karakter1=""
for letter in range(nr_letters):
  l = random.choice(letters)
  karakter1 += l
# print(karakter1)

karakter2= ""
for symbol in range(nr_symbols):
 o = random.choice(symbols)
 karakter2 += o
# print(karakter2)

karakter3=""
for number in range(nr_numbers):
 n =random.choice(numbers)
 karakter3 += n
# print(karakter3)

print(f"This is password generator Easy-level: \n{karakter1}{karakter2}{karakter3}")

#Hard Level



#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P