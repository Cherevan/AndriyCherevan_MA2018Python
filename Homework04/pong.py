# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
RIGHT_PAD_POINT = WIDTH - PAD_WIDTH


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel  # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]  # Set ball position at the center
    ball_vel = [random.randrange(120, 240) / 60, -random.randrange(60, 180) / 60]  # Set the random speed of a ball
    if not direction:  # If direction = False, then ball go to Left
        ball_vel[0] = -ball_vel[0]


# define event handlers
def new_game():
    global paddle_pos, paddle_vel, score  # Declare global variables
    paddle_pos = [160, 160]
    paddle_vel = [0, 0]
    score = [0, 0]
    spawn_ball(random.randint(0, 1))  # 0 - into Left and 1 - into Right


def check_paddle():
    global paddle_pos, paddle_vel
    # Check left and right paddles
    for i in range(2):  # We move two paddles in this cycle
        if paddle_pos[i] <= 0 and paddle_vel[i] < 0:  # If paddle position is up
            paddle_pos[i] = 0
        elif paddle_pos[i] + PAD_HEIGHT >= HEIGHT and paddle_vel[i] > 0:  # If paddle position is down
            paddle_pos[i] = HEIGHT - PAD_HEIGHT
        else:
            paddle_pos[i] += paddle_vel[i]  # Move paddle


def update_ball():
    global ball_pos, ball_vel, score
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS or ball_pos[0] >= WIDTH - (PAD_WIDTH + BALL_RADIUS):
        ball_vel[0] = -ball_vel[0] * 1.1  # Change the direction and increase velocity
        ball_vel[1] = ball_vel[1] * 1.1
        side = False  # If ball in the left side
        if ball_pos[0] > WIDTH / 2:  # If ball in the right side
            side = True
        up_point = paddle_pos[side] - BALL_RADIUS
        down_point = paddle_pos[side] + (PAD_HEIGHT + BALL_RADIUS)
        if ball_pos[1] < up_point or ball_pos[1] > down_point:  # If a goal
            score[1 - side] += 1
            spawn_ball(1 - side)

    if ball_pos[1] >= HEIGHT - BALL_RADIUS or ball_pos[1] <= BALL_RADIUS:  # Check the upper and lower field limits
        ball_vel[1] = -ball_vel[1]

    for i in range(2):  # Update ball position in the vertical and horizontal axis
        ball_pos[i] += ball_vel[i]


def draw(canvas):
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([RIGHT_PAD_POINT, 0], [RIGHT_PAD_POINT, HEIGHT], 1, "White")

    # update ball
    update_ball()

    # draw ball
    canvas.draw_circle(ball_pos, 20, 2, 'Lime', 'White')

    # update paddle's vertical position, keep paddle on the screen
    check_paddle()  # Call function
    pad1_coord, pad2_coord = [0, 0, 0, 0], [0, 0, 0, 0]
    pad1_coord[0], pad2_coord[0] = [0, paddle_pos[0]], [RIGHT_PAD_POINT, paddle_pos[1]]
    pad1_coord[1], pad2_coord[1] = [PAD_WIDTH, paddle_pos[0]], [WIDTH, paddle_pos[1]]
    pad1_coord[2], pad2_coord[2] = [PAD_WIDTH, paddle_pos[0] + PAD_HEIGHT], [WIDTH, paddle_pos[1] + PAD_HEIGHT]
    pad1_coord[3], pad2_coord[3] = [0, paddle_pos[0] + PAD_HEIGHT], [RIGHT_PAD_POINT, paddle_pos[1] + PAD_HEIGHT]

    # draw paddles
    canvas.draw_polygon(pad1_coord, 1, 'White', 'Lime')
    canvas.draw_polygon(pad2_coord, 1, 'White', 'Lime')

    # draw scores
    canvas.draw_text(str(score[0]), [200, 100], 24, 'White')
    canvas.draw_text(str(score[1]), [400, 100], 24, 'White')


def key_down(key):
    global paddle_vel
    if key == 87:  # Key W
        paddle_vel[0] -= 3
    elif key == 83:  # Key S
        paddle_vel[0] += 3
    elif key == 38:  # Key Up
        paddle_vel[1] -= 3
    elif key == 40:  # Key Down
        paddle_vel[1] += 3


def key_up(key):
    global paddle_vel
    if chr(key) in ('W', 'S'):
        paddle_vel[0] = 0
    if key in (38, 40):  # Key Up or Down
        paddle_vel[1] = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
frame.add_button('Reset', new_game, 200)

# start frame
new_game()
frame.start()
