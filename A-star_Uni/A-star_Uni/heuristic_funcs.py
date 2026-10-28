import random

#Hamming Distance

def hamming_distance(board, goal):
    misplaced = 0

    for row in range(3):
        for col in range(3):
            if board[row][col] != 0 and board[row][col] != goal[row][col]:
                misplaced += 1

    return misplaced

#Manhattan Distance
