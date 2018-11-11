import random

player_score = 0
sheldon_score = 0
player_choice, sheldon_choice = '', ''
# We check the number by index of player`s choice in this dictionary(tuple).
RPSLS_DICT = ('rock', 'spock', 'paper', 'lizard', 'scissors')


def who_winner(player, sheldon):
    # Function who_winner get 2 integer number from player and computer choices
    # and compares them, determining who won.
    print('Your choice: ' + RPSLS_DICT[player].capitalize())
    print('Sheldon choice: ' + RPSLS_DICT[sheldon].capitalize())
    if (sheldon - player) % 5 >= 3:
        # Player win.
        return True
    else:
        # Player lost
        return False


# The game has 3 rounds. Player and computer select one of five choices.
for i in range(1, 4):
    # compute random guess for sheldon_choice using random.randint()
    sheldon_choice = random.randint(0, 4)
    # print out the message for the player's choice
    print('Round ' + str(i) + '.')
    print('Please select among Rock, Spock, Paper, Lizard and Scissors.')
    player_choice = input('You choice: ').lower()
    # It verifies that user wrote the word correctly.
    if player_choice in RPSLS_DICT:
        # player_choice get index of choice in RPSLS_DICT dictionary.
        player_choice = RPSLS_DICT.index(player_choice)
        if player_choice != sheldon_choice:
            # Call function who_winner and get boolean result.
            result = who_winner(player_choice, sheldon_choice)
            # If result = True then player win.
            if result:
                player_score += 1
                print('You win a point.\n')
            # If result = False then computer win.
            else:
                sheldon_score += 1
                print('You Lose. Sheldon wins a point.\n')
        # If 2 choices are identically, nobody will has point. Go to next round.
        else:
            print('Your and Sheldon`s choices are identically.\n')
    # If user wrote incorrect input - computer will win the round.
    else:
        sheldon_score += 1
        print('Incorrect input. One point to Sheldon. Sorry.\n')

# Print out the message for your and Sheldon`s scores.
print('You score: ' + str(player_score))
print('Sheldon`s score: ' + str(sheldon_score))
# Score points. Use if/elif/else to determine winner, print winner message.
if player_score > sheldon_score:
    print('Congratulations! You win this battle.')
elif player_score == sheldon_score:
    print('No winners.')
else:
    print('Sorry, but you lost this game.')
