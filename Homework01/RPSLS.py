import random

player_score = 0
sheldon_score = 0
player_choice, sheldon_choice = '', ''
RPSLS_DICT = ['rock', 'spock', 'paper', 'lizard', 'scissors']


def who_winner(player, sheldon):
    global player_score, sheldon_score
    print('Sheldon choice: ' + RPSLS_DICT[sheldon].capitalize())
    if (sheldon - player) % 5 >= 3:
        player_score += 1
        print('You win one point.\n')
    else:
        sheldon_score += 1
        print('You Lose. Sheldon wins a point.\n')


for i in range(3):
    sheldon_choice = random.randint(0, 4)
    print('Round ' + str(i + 1) + '.')
    print('Please select between Rock, Spock, Paper, Lizard, Scissors.')
    player_choice = input('You choice: ')
    if player_choice.lower() in RPSLS_DICT:
        player_choice = RPSLS_DICT.index(player_choice.lower())
        if 0 <= player_choice <= 4:
            if player_choice != sheldon_choice:
                who_winner(player_choice, sheldon_choice)
            else:
                print('Your and Sheldon`s choice is identical.\n')
    else:
        sheldon_score += 1
        print('Incorrect input. One point to Sheldon.\n')

print('You score: ' + str(player_score))
print('Sheldon`s score: ' + str(sheldon_score))
if player_score > sheldon_score:
    print('Congratulations! You won this battle.')
elif player_score == sheldon_score:
    print('No winners.')
else:
    print('Sorry, but you lost this game.')
