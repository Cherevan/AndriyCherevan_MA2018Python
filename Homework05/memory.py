# implementation of card game - Memory
import simplegui
import random

numbers = []
exposed = []
previous = [16, 16]
shot = 0


# helper function to initialize globals
def new_game():
    global numbers, exposed, shot, previous
    shot = 0
    previous = [16, 16]
    numbers = [num for num in range(8)] * 2
    [random.shuffle(numbers) for _ in range(3)]  # Shuffle our deck three times
    exposed = [False] * 17  # 16 playing cards and 1 invisible


# define event handlers
def mouse_click(pos):
    # add game state logic here
    global shot, exposed, previous
    choice = pos[0] // 50
    if not exposed[choice]:  # If card not open
        exposed[choice] = True  # Open card
        # Player open the first card
        if exposed.count(True) % 2 == 1:
            for i in range(2):  # Close previous two cards
                exposed[previous[i]] = False
            previous[0] = choice  # Remember first card
        # Player open the second card
        else:
            previous[1] = choice  # Remember second card
            if numbers[previous[0]] == numbers[previous[1]]:  # If two numbers are identical
                previous = [16, 16]  # Set index to invisible block
            shot += 1


# cards are logically 50x100 pixels in size
def draw(canvas):
    for i, card in enumerate(exposed[:-1]):
        if card:  # Draw number
            canvas.draw_text(str(numbers[i]), (50 * i + 10, 65), 50, 'White')
        else:  # Draw deck
            canvas.draw_polygon([(50 * i, 0), (50 * i + 49, 0),
                                 (50 * i + 49, 100), (50 * i, 100)], 2, 'White', 'Green')
    label.set_text('Turns = ' + str(shot))


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouse_click)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
