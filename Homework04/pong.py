# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel  # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction:
        ball_vel = [random.randrange(120, 241) / 60, -random.randrange(60, 180) / 60]
    else:
        ball_vel = [-random.randrange(120, 241) / 60, -random.randrange(60, 180) / 60]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1, score2 = 0, 0
    paddle1_pos, paddle2_pos = 200, 200
    paddle1_vel, paddle2_vel = 0, 0
    if random.randint(0, 1):
        spawn_ball(RIGHT)
    else:
        spawn_ball(LEFT)


def check_paddle():
    global paddle1_pos, paddle2_pos
    # Check the left paddle
    if paddle1_pos - HALF_PAD_HEIGHT <= 0 and paddle1_vel < 0:
        paddle1_pos = HALF_PAD_HEIGHT
    elif paddle1_pos + HALF_PAD_HEIGHT >= HEIGHT and paddle1_vel > 0:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    else:
        paddle1_pos += paddle1_vel

    # Check the right paddle
    if paddle2_pos - HALF_PAD_HEIGHT <= 0 and paddle2_vel < 0:
        paddle2_pos = HALF_PAD_HEIGHT
    elif paddle2_pos + HALF_PAD_HEIGHT >= HEIGHT and paddle2_vel > 0:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
    else:
        paddle2_pos += paddle2_vel


def update_ball():
    global ball_pos, score1, score2
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:  # Left
        up_point = paddle1_pos - (HALF_PAD_HEIGHT + BALL_RADIUS)
        down_point = paddle1_pos + (HALF_PAD_HEIGHT + BALL_RADIUS)
        if up_point <= ball_pos[1] <= down_point:
            ball_vel[0] = -ball_vel[0] * 1.1
        else:  # If goal
            score2 += 1
            spawn_ball(RIGHT)

    if ball_pos[0] >= WIDTH - 2 * PAD_WIDTH - BALL_RADIUS / 2:  # Right
        up_point = paddle2_pos - (HALF_PAD_HEIGHT + BALL_RADIUS)
        down_point = paddle2_pos + (HALF_PAD_HEIGHT + BALL_RADIUS)
        if up_point <= ball_pos[1] <= down_point:
            ball_vel[0] = -ball_vel[0] * 1.1
        else:  # If goal
            score1 += 1
            spawn_ball(LEFT)

    if ball_pos[1] >= HEIGHT - BALL_RADIUS or ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]


def draw(canvas):
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    update_ball()

    # draw ball
    canvas.draw_circle(ball_pos, 20, 2, 'Lime', 'White')

    # update paddle's vertical position, keep paddle on the screen
    check_paddle()
    pad1_coor = [[0, paddle1_pos - HALF_PAD_HEIGHT], [8, paddle1_pos - HALF_PAD_HEIGHT],
                 [8, paddle1_pos + HALF_PAD_HEIGHT], [0, paddle1_pos + HALF_PAD_HEIGHT]]
    pad2_coor = [[WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos - HALF_PAD_HEIGHT],
                 [WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT]]

    # draw paddles
    canvas.draw_polygon(pad1_coor, 1, 'White', 'Lime')
    canvas.draw_polygon(pad2_coor, 1, 'White', 'Lime')

    # draw scores
    canvas.draw_text(str(score1), [200, 100], 24, 'White')
    canvas.draw_text(str(score2), [400, 100], 24, 'White')


def key_down(key):
    global paddle1_vel, paddle2_vel
    if key == 87:  # Key W
        paddle1_vel -= 3
    elif key == 83:  # Key S
        paddle1_vel += 3
    elif key == 38:  # Key Up
        if paddle2_pos - HALF_PAD_HEIGHT > 0:
            paddle2_vel -= 3
    elif key == 40:  # Key Down
        paddle2_vel += 3


def key_up(key):
    global paddle1_vel, paddle2_vel
    if chr(key) in ('W', 'S'):
        paddle1_vel = 0
    if key in (38, 40):
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
frame.add_button('Reset', new_game, 100)

# start frame
new_game()
frame.start()
