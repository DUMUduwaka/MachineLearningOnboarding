
from random import randint
num = randint(1, 10)


while True:
    try:
        guess = int(input('Guess the number! '))
        if guess > 0 and guess < 11:
            if num == guess:
                print('Congratulations, You guessed the number.')
                break
            else:
                print('Oops You are wrong')
        else:
            print('Please enter a number between 1 and 10')
    except ValueError:
        print("Please enter a number")
        continue
