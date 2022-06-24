import random

print('Hello World!')


def game():
    Correct = 0
    Wrong = 0

    Numbers = input(
        'Type two numbers divided by a backspace, in a range of which you would like to guess, or type quit '
        'if you want to exit: ')
    Numbers_range = Numbers.split(' ')

    try:
        int(Numbers_range[0])
    except ValueError:
        print('Oops, probably you have written something apart from numbers')
        print(f'{Correct}:{Wrong}')
        if Correct > Wrong:
            print('You won!')
        elif Correct == Wrong:
            print('It`s a draw')
        else:
            print('You lost!')
        game()

    try:
        while True:

            Player_choice = input('Guess the number: ')

            if Player_choice != 'quit':

                Random_number = random.randint(int(Numbers_range[0]), int(Numbers_range[1]))

                Player_choice_int = int(Player_choice)

                if Player_choice_int in range(int(Numbers_range[0]), int(Numbers_range[1]) + 1):
                    print(Player_choice_int)
                    print(Random_number)

                    if Player_choice_int == Random_number:
                        Correct += 1
                        print('You guessed!')
                    else:
                        Wrong += 1
                        print("You didn't guess")
                else:
                    print(f'Your number must be between {int(Numbers_range[0])} and {int(Numbers_range[1])}')

            else:
                print(f'{Correct}:{Wrong}')
                if Correct > Wrong:
                    print('You won!')
                elif Correct == Wrong:
                    print('It`s a draw')
                else:
                    print('You lost!')
                exit()
    except ValueError:
        print('Oops, probably you have written something apart from numbers')
        game()


game()
