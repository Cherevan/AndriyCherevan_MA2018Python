import simplegui

our_time = 0
win = 0
step = 0
flag = False


def timer_handler():
    global our_time
    our_time += 1


def draw(canvas):
    canvas.draw_text(reformat(our_time), [100, 160], 32, 'White')
    line = str(win) + '/' + str(step)
    canvas.draw_text(line, [220, 30], 24, 'White')


def start_timer():
    global flag
    flag = True
    timer.start()


def stop_timer():
    global flag, win, step
    timer.stop()
    if flag:
        step += 1
        if our_time % 10 == 0:
            win += 1
    flag = False


def reset_game():
    global our_time, flag, win, step
    flag = False
    timer.stop()
    our_time = 0
    win = 0
    step = 0


def reformat(f):
    global flag
    f += 400 * (f // 600)
    f = str(f)
    f = '0' * (4 - len(f)) + f
    if int(f) >= 10000:
        flag = False
        stop_timer()
        return '10:0.0'
    else:
        return f[-4::-1] + ':' + f[-3:-1] + '.' + f[-1]


frame = simplegui.create_frame('Stop: Game', 300, 300)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler)
frame.add_button('Start', start_timer, 100)
frame.add_button('Stop', stop_timer, 100)
frame.add_button('Reset', reset_game, 100)

frame.start()
