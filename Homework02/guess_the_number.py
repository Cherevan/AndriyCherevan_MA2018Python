import simplegui
from random import randint
from math import ceil, log

secret_code = 0
attempt = 0
max_range = 99


def new_game():
    global secret_code, attempt
    # Count the number of attempts.
    attempt = ceil(log(max_range + 1, 2))
    # Define a secret number from a given range.
    secret_code = randint(0, max_range)
    print('=' * 10)
    print('Start new game. You have', attempt, 'attempts.\n')
    lbl_input.set_text('Start new game.')


def check_num(guess):
    global attempt
    # Check for the lack of letters in the input.
    if '0' <= guess <= '9_999_999':
        # Count an attempt.
        attempt -= 1
        print('Your guess number was ' + guess + '.')
        guess = int(guess)
        lbl_input.set_text('Your last input is ' + str(guess))
        # Checking for the last try.
        if attempt == 0 and guess != secret_code:
            print('You lose this game.\n')
            new_game()
        # Player didn`t guess.
        elif guess != secret_code:
            if secret_code > guess:
                print('Higher.')
            else:
                print('Lower.')
            print('You have', str(attempt), 'tries.\n')
        # Player win.
        else:
            print('Correct! You win.\n')
            lbl_input.set_text('You win!')
            new_game()
    # If the player wrote text, the program will send the message.
    else:
        print('Incorrect input.')
    num_input.set_text('')


def range99():
    # This function set a maximum number in range and start a new game.
    global max_range
    max_range = 99
    lbl_start.set_text('Secret number in range 0-99.')
    new_game()


def range999():
    # This function set a maximum number in range and start a new game.
    global max_range
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
