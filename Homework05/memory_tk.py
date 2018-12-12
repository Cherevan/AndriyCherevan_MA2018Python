from tkinter import *
import random

numbers = []
exposed = []
previous = [16, 16]
shot = 0


def new_game():
    global numbers, exposed, shot, previous
    shot = 0
    previous = [16, 16]
    numbers = [num for num in range(8)] * 2
    [random.shuffle(numbers) for _ in range(3)]  # Shuffle our deck three times
    exposed = [False] * 17  # 16 playing cards and 1 invisible
    for i in range(len(exposed)):
        c.create_rectangle(50 * i, 0, 50 * i + 49, 100, fill='green', outline='white')


def mouse_click(event):
    # add game state logic here
    global shot, exposed, previous
    choice = event.x // 50
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

    c.delete('all')
    for i, card in enumerate(exposed[:-1]):
        if card:  # Draw number
            c.create_text(50 * i + 25, 50, text=numbers[i], font='Ubuntu 50', fill='white')
        else:  # Draw deck
            c.create_rectangle(50 * i, 0, 50 * i + 49, 100, fill='green', outline='white')
    label['text'] = 'Turns = {}'.format(shot)
    # label.configure(text='Turns = {}'.format(shot))


root = Tk()
root.title('Memory')

frame = Frame(root, width=800, height=40)
frame.pack()

button_reset = Button(frame, text='Reset', command=new_game)
button_reset.pack(side=LEFT)

label = Label(frame, text='Turns = {}'.format(shot), font=32)
label.pack(side=RIGHT)

c = Canvas(root, width=800, height=100, bg='#003300')
c.pack(side=BOTTOM)
c.bind('<Button-1>', mouse_click)

new_game()

root.mainloop()
