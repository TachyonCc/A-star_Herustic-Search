"""Estimate moves from a 3x3 board to a goal; return an integer, ignoring 0."""


def hamming_distance(board, goal):
    misplaced = 0

    for row in range(3):
        for col in range(3):
            if board[row][col] != 0 and board[row][col] != goal[row][col]:
                misplaced += 1

    return misplaced


def manhattan_distance(board, goal):
    goal_positions = {}
    for row in range(3):
        for col in range(3):
            goal_positions[goal[row][col]] = (row, col)

    distance = 0

    for row in range(3):
        for col in range(3):
            value = board[row][col]
            if value == 0:
                continue

            target_row, target_col = goal_positions[value]

            distance += abs(row - target_row) + abs(col - target_col)

    return distance
