from heuristic_funcs import heuristic_funcs

def astar(start_board, goal_board, heuristic_distance):
    pass

def get_neighbors(board):
    neighborsCoordinates = []
    neighborsBoards = []
    row = -1
    column = -1

    # 1. Find the empty tile
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                row = i
                column = j
                break

    #Safety Guard        
    if (row <0 or column <0):
        return None

    # 2. Determine which moves are valid
    if (row + 1 < len(board) ):
        neighborsCoordinates.append((row + 1, column))
    if (row - 1 >= 0 ):
        neighborsCoordinates.append((row - 1, column))
    if (column + 1 < len(board[0]) ):
        neighborsCoordinates.append((row, column + 1))
    if (column - 1 >= 0 ):
        neighborsCoordinates.append((row, column - 1))

    # 3. Create a new board for each move
    for coord in neighborsCoordinates:
        newBoard = [r.copy() for r in board]
        
    # 4. Swap the empty tile with its neighbor
        newRow, newCol = coord
        newBoard[row][column] = newBoard[newRow][newCol]
        newBoard[newRow][newCol] = 0

        neighborsBoards.append(newBoard)

    return neighborsBoards
