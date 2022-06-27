import random


def game():
    correct = 0
    wrong = 0

    numbers = input(
        'Type two numbers divided by a backspace, in a range of which you would like to guess, or type quit '
        'if you want to exit: ')
    numbers_range = numbers.split(' ')

    try:
        int(numbers_range[0])
    except ValueError:
        print('Oops, probably you have written something apart from numbers')
        game()

    try:
        while True:

            player_choice = input('Guess the number: ')

            if player_choice != 'quit':

                random_number = random.randint(int(numbers_range[0]), int(numbers_range[1]))

                player_choice_int = int(player_choice)

                if player_choice_int in range(int(numbers_range[0]), int(numbers_range[1]) + 1):
                    print(player_choice_int)
                    print(random_number)

                    if player_choice_int == random_number:
                        correct += 1
                        print('You guessed!')
                    else:
                        wrong += 1
                        print("You didn't guess")
                else:
                    print(f'Your number must be between {int(numbers_range[0])} and {int(numbers_range[1])}')

            else:
                print(f'{correct}:{wrong}')
                if correct > wrong:
                    print('You won!')
                elif correct == wrong:
                    print('It`s a draw')
                else:
                    print('You lost!')
                exit()
    except ValueError:
        print('Oops, probably you have written something apart from numbers')
        print(f'{correct}:{wrong}')
        if correct > wrong:
            print('You won!')
        elif correct == wrong:
            print('It`s a draw')
        else:
            print('You lost!')
        game()


game()
