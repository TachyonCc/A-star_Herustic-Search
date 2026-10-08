
Start_Board = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

Goal_Board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


def print_board(board):
    """Print the puzzle as a 3x3 grid."""
    for row in board:
        print(row)


print_board(Start_Board)