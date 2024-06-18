import random

number = random.randint(1,100)
guess = 0

while guess != number:
    guess = int(input('Enter your Guess number (1-100):'))

    if (guess < number):
        print('It is Higher')
    elif (guess > number):
        print('It is Lower')
    else:
        print('Yehey You are correct, CONGRATULATIONS!!!')