# An Exciting Number Guessing Game

import random

name = input('Enter your full name:\t')

while True:
    upper_limit = int(input('\nEnter the upper limit:\t'))
    lower_limit = int(input('Enter the lower limit:\t'))

    generated_number = random.randint(lower_limit, upper_limit)

    attempt = 1

    while attempt <= 5:
        print('\nRemaining Chances:\t', 5 - attempt)
        print('Lower Limit:\t', lower_limit)
        print('Upper Limit:\t', upper_limit)

        guessed_number = int(input("\nEnter your guess in the range of upper and lower limit:\t"))

        if guessed_number == generated_number:
            print('Correct !')
            break

        elif guessed_number > generated_number:
            print('Guessed number is big.')
            attempt += 1

        else:
            print('Guessed number is small.')
            attempt += 1

    if attempt < 6:
        print(name, 'guessed the number in ', attempt, 'attempts.')
    else:
        print('OOPS !!! Maximum attempt reached.\nDon\'t Worry, You can try again.')

    choice = input('Do you want to play again (yes / no) ?')
    if choice == 'no' or choice == 'NO':
        break
