import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
hard_mode = False
mode_name = 'Soft mode'
outcome = ""
outcome_pos = [150, 480]
score = [0, 0]

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_SIZE)


# define hand class
class Hand:
    def __init__(self):
        self.hand_cards = []  # create Hand object

    def __str__(self):
        result = 'Hand contains '
        for card in self.hand_cards:
            result += str(card) + ' '
        return result  # return a string representation of a hand

    def add_card(self, card):
        self.hand_cards.append(card)  # add a card object to a hand

    def clean_hand(self):
        self.hand_cards = []

    def get_value(self):
        result = 0
        ace_in_hand = False

        for card in self.hand_cards:
            result += VALUES[card.rank]
            if card.rank == 'A':
                ace_in_hand = True

        if ace_in_hand and (result < 12 or hard_mode):
            result += 10

        return result

    def draw(self, canvas, pos):
        for i, card in enumerate(self.hand_cards):  # draw a hand on the canvas, use the draw method for cards
            card.draw(canvas, [pos[0] + 80 * i, pos[1]])


# define deck class
class Deck:
    def __init__(self):
        self.deck = []  # create a Deck object

    def __str__(self):
        result = 'Deck contains '  # return a string representing the deck
        for card in self.deck:
            result += str(card) + ' '
        return result

    def shuffle(self):
        random.shuffle(self.deck)  # shuffle the deck

    def restart(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))
        self.shuffle()

    def deal_card(self):
        return self.deck.pop()  # deal a card object from the deck


# define event handlers for buttons
def deal():
    global outcome, outcome_pos, in_play, score

    deck.restart()
    player_hand.clean_hand()
    dealer_hand.clean_hand()

    if in_play:
        outcome_pos[0] = 180
        outcome = 'You lost the round.'
        score[1] += 1
    else:
        outcome_pos[0] = 120
        outcome = 'Hit or stand? Your choice.'

    # your code goes here
    for _ in range(2):
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())

    # print('Players hand: ' + str(player_hand))
    # print('Deal hand: ' + str(dealer_hand))

    in_play = True


def hit():
    global player_hand, outcome, outcome_pos, score, in_play

    if in_play:
        # if the hand is in play, hit the player
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())

        # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            outcome_pos[0] = 190
            outcome = 'You have busted'
            score[1] += 1
            in_play = False

        # print('Players hand: ' + str(player_hand))
        # print('Dealers hand: ' + str(dealer_hand))


def stand():
    global score, outcome, outcome_pos, in_play

    if in_play:
        # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())

        # assign a message to outcome, update in_play and score
        if dealer_hand.get_value() > 21:
            score[0] += 1
            outcome_pos[0] = 100
            outcome = 'Dealer has busted. You win.'
        else:
            if player_hand.get_value() <= dealer_hand.get_value():
                score[1] += 1
                outcome_pos[0] = 160
                outcome = 'You lose. New deal?'
            else:
                score[0] += 1
                outcome_pos[0] = 160
                outcome = 'You win. New deal?'

    in_play = False


def shift_game():
    global hard_mode, mode_name

    if hard_mode:
        hard_mode = False
        mode_button.set_text('Hard mode')
        mode_name = 'Soft mode'
    else:
        hard_mode = True
        mode_button.set_text('Soft mode')
        mode_name = 'Hard mode'


# draw handler
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_polygon([(0, 0), (600, 0), (600, 50), (0, 50)], 1, 'Khaki', 'Khaki')
    canvas.draw_text('Blackjack', (205, 38), 38, 'DarkSlateGray')
    canvas.draw_polygon([(200, 52), (400, 52), (400, 82), (200, 82)], 2, 'SteelBlue', ' Khaki')
    canvas.draw_text(mode_name, (250, 75), 20, 'DarkSlateGray')

    canvas.draw_text('Dealers hand:', (40, 130), 24, 'LemonChiffon')
    dealer_hand.draw(canvas, [40, 140])
    canvas.draw_text('Players hand:', (40, 310), 24, 'LemonChiffon')
    player_hand.draw(canvas, [40, 320])

    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (76, 188), CARD_BACK_SIZE)

    canvas.draw_text(outcome, outcome_pos, 28, 'LemonChiffon')

    canvas.draw_polygon([(0, 510), (297, 510), (297, 600), (0, 600)], 1, 'Khaki', 'Khaki')
    canvas.draw_polygon([(303, 510), (600, 510), (600, 600), (303, 600)], 1, 'Khaki', 'Khaki')
    canvas.draw_text('Players score: {}'.format(score[0]), (30, 565), 28, 'DarkSlateGray')
    canvas.draw_text('Dealers score: {}'.format(score[1]), (333, 565), 28, 'DarkSlateGray')


deck = Deck()
player_hand = Hand()
dealer_hand = Hand()

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("DarkCyan")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)

frame.add_label(' ', 200)
frame.add_label(' ', 200)
frame.add_label('Change games mode to:', 200)
mode_button = frame.add_button('Hard mode', shift_game, 200)
frame.add_label('In the hard mode, Ace always has 11 points.')
frame.add_label('In soft mode: the player chooses between the Ace value 1 or 11.')
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
