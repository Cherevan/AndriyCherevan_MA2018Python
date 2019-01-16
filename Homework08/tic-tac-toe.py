"""
Monte Carlo Tic-Tac-Toe Player
"""
import random
import poc_ttt_gui
import poc_ttt_provided as provided

NTRIALS = 100  # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 2.0  # Score for squares played by the other player


def mc_trial(board, player):
    """
    This function takes a current board and the next player to move.
    """
    while board.check_win() == None:
        empty_cell_list = board.get_empty_squares()
        empty_cell = random.choice(empty_cell_list)
        board.move(empty_cell[0], empty_cell[1], player)
        player = provided.switch_player(player)


def mc_update_scores(scores, board, player):
    """
    The function should score the completed board and update the scores grid.
    """
    winner = board.check_win()
    size = board.get_dim()

    if winner != provided.DRAW:
        for row in range(size):
            for col in range(size):
                cell_owner = board.square(row, col)

                if cell_owner == player:
                    if winner == player:
                        scores[row][col] += SCORE_CURRENT
                    else:
                        scores[row][col] -= SCORE_CURRENT

                elif cell_owner != provided.EMPTY:
                    if winner == player:
                        scores[row][col] -= SCORE_OTHER
                    else:
                        scores[row][col] += SCORE_OTHER


def get_best_move(board, scores):
    """
    The function should find all of the empty squares with the maximum score
    and randomly return one of them as a (row,column) tuple.
    """
    size = board.get_dim()
    best_value = NTRIALS * -10
    best_step_list = []

    for row in range(size):
        for col in range(size):
            if board.square(row, col) == provided.EMPTY and scores[row][col] > best_value:
                best_value = scores[row][col]
                best_step_list = [(row, col)]
            elif board.square(row, col) == provided.EMPTY and scores[row][col] == best_value:
                best_step_list.append((row, col))

    # print(best_step_list)

    if len(best_step_list) > 0:
        return random.choice(best_step_list)
    else:
        return None


def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is, and the number of trials to run.
    """
    size = board.get_dim()
    scores = [[0.0 for _ in range(size)] for _ in range(size)]

    for _ in range(trials):
        clone_board = board.clone()
        mc_trial(clone_board, player)
        mc_update_scores(scores, clone_board, player)

    return get_best_move(board, scores)

# provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
