"""
Clone of 2048 game.
"""
import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result = []
    list_len = len(line)

    while len(line) > 1:
        number = line.pop(0)

        while len(line) > 0 and line[0] == 0:
            line.pop(0)

        if len(line) and number == line[0]:
            line.pop(0)
            result.append(number * 2)
        else:
            if number != 0:
                result.append(number)

    if len(line) != 0:
        result.append(line.pop())

    result += [0 for _ in range(list_len - len(result))]

    # replace with your code
    return result


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.table = []
        self.reset()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        result = ''

        for row in self.table:
            result += str(row) + '\n'

        return result

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.table = []
        for col in range(self.grid_height):
            self.table.append([0 for _ in range(self.grid_width)])

        for _ in range(2):
            self.new_tile()

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if_changed = False

        if direction == UP or direction == DOWN:
            number_of_cells = self.grid_height
            number_of_lines = self.grid_width
        else:
            number_of_cells = self.grid_width
            number_of_lines = self.grid_height

        down_or_right = True if direction == DOWN or direction == RIGHT else False

        change_lines = [1 if OFFSETS[direction][k] == 0 else 0 for k in range(2)]

        for i in range(number_of_lines):
            line = []

            for cell in range(number_of_cells):  # Read a line
                row = OFFSETS[direction][0] * (cell + down_or_right) + change_lines[0] * i
                col = OFFSETS[direction][1] * (cell + down_or_right) + change_lines[1] * i
                line.append(self.table[row][col])

            old_line = list(line)
            line = merge(line)

            if old_line != line:  # If was change in a line
                if_changed = True

            for cell in range(number_of_cells):  # Write this line in our table
                row = OFFSETS[direction][0] * (cell + down_or_right) + change_lines[0] * i
                col = OFFSETS[direction][1] * (cell + down_or_right) + change_lines[1] * i
                self.table[row][col] = line[cell]

        if if_changed:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        tabula_rasa = []
        value = 2 if random.randrange(10) < 9 else 4

        for zero_row in range(self.grid_height):
            for zero_col in range(self.grid_width):
                if self.table[zero_row][zero_col] == 0:
                    tabula_rasa.append([zero_row, zero_col])

        if len(tabula_rasa) != 0:
            random_zero = random.choice(tabula_rasa)
            self.set_tile(random_zero[0], random_zero[1], value)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.table[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.table[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
