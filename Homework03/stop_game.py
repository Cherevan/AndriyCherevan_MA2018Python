import simplegui

our_time = 0
win = 0
step = 0
flag = False


def timer_handler():
    # Handler for add 1 point to count every 1/10 seconds.
    global our_time
    our_time += 1


def draw(canvas):
    canvas.draw_text(reformat(our_time), [100, 160], 32, 'White')
    line = str(win) + '/' + str(step)
    canvas.draw_text(line, [220, 30], 24, 'Orange')


def start_timer():
    # Event`s handler for button 'Start'. Starts the timer.
    global flag
    flag = True
    timer.start()


def stop_timer():
    # Event`s handler for button 'Stop'. Stop the timer. If the player wins, we add 1 point to him.
    global flag, win, step
    timer.stop()
    if flag:  # If the timer is stopped, value flag = False.
        step += 1
        if our_time % 10 == 0:
            win += 1
    flag = False


def reset_game():
    # Function to reset a game. All values become zeros.
    global our_time, flag, win, step
    flag = False
    timer.stop()
    our_time = 0
    win = 0
    step = 0


def reformat(f):
    # Helper function converts time from an integer into formatted string A:BC.D
    global flag
    f = str(f + 400 * (f // 600))
    f = '0' * (4 - len(f)) + f
    if int(f) >= 10000:  # After 10 minutes this game stopped.
        flag = False
        stop_timer()
        return '10:0.0'
    else:  # Return a formatted string type A:BC.D
        return f[:-3] + ':' + f[-3:-1] + '.' + f[-1]


# Create new graphics form and timer.
frame = simplegui.create_frame('Stop: Game', 300, 300)
timer = simplegui.create_timer(100, timer_handler)
# Create 3 new buttons.
frame.add_button('Start', start_timer, 100)
frame.add_button('Stop', stop_timer, 100)
frame.add_button('Reset', reset_game, 100)

frame.set_draw_handler(draw)
frame.set_canvas_background('Blue')
frame.start()
