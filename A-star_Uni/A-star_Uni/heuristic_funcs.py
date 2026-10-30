#Hamming Distance
def hamming_distance(board, goal):
    misplaced = 0

    for row in range(3):
        for col in range(3):
            if board[row][col] != 0 and board[row][col] != goal[row][col]:
                misplaced += 1

    return misplaced

#Manhattan Distance
def manhattan_distance(board, goal):
    distance = 0

    for row in range(3):
        for col in range(3):
            value = board[row][col]
            if (value == 0):
                continue  #Skip the empty tile

            targetRow = (value - 1) // 3
            targetCol = (value - 1) % 3

            distance += abs(row - targetRow) + abs(col - targetCol)

    return distance
