import random
import string

length = int(input('Enter Length: '))

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

password = ''

for i in range(length):
    next_character = random.choice(chars)
    password += next_character

print('Your Password is:', password)