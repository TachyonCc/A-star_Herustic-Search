from puzzle_generator import generate_random_puzzle
from heuristic_funcs import heuristic_funcs
import time


Start_Board = generate_random_puzzle()

Goal_Board = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

#2 heuristics for A* algorithm

def print_board(board):
    """Print the puzzle as a 3x3 grid."""
    for row in board:
        print(row)

#Here actual usage of algs.


#Print solved or unsolvablepuzzle


print_board(Start_Board)