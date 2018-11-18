import simplegui
from random import randint
from math import ceil, log

secret_code = 0
guess_num = 0
max_attempt = 7
max_range = 99


def new_game():
    global secret_code, max_attempt, attempt
    max_attempt = ceil(log(max_range + 1, 2))
    attempt = max_attempt
    secret_code = randint(0, max_range)
    print('=' * 10)
    print('Start new game. You have', max_attempt, 'attempts.\n')


def check_num(guess):
    global attempt
    if ('0' <= guess <= '9_999_999'):
        attempt -= 1
        print('Your guess number was ' + guess + '.')
        guess = int(guess)
        if secret_code > guess:
            print('Higher. ', end='')
        elif secret_code < guess:
            print('Lower. ', end='')
        lbl_input.set_text('Your last input is ' + str(guess))
        if attempt == 0 and guess != secret_code:
            print('You lose this game.\n')
            new_game()
        elif guess != secret_code:
            print('You have', str(attempt), 'tries.\n')
        else:
            print('Correct! You win.\n')
            lbl_input.set_text('You win!')
            new_game()
    else:
        print('Incorrect input.')
    num_input.set_text('')


def range99():
    global max_range
    max_range = 99
    lbl_start.set_text('Secret number in range 0-99.')
    new_game()


def range999():
    global max_range, max_attempt
    max_range = 999
    lbl_start.set_text('Secret number in range 0-999.')
    new_game()


frame = simplegui.create_frame('Guess the number', 200, 250)

lbl_start = frame.add_label('Secret number in range 0-99.', 210)
num_input = frame.add_input('Enter the number:', check_num, 185)
lbl_input = frame.add_label('')
frame.add_label('')
frame.add_label('Start new game:')
frame.add_button('with a range 0-99', range99, 185)
frame.add_button('with a range 0-999', range999, 185)

new_game()
frame.start()
