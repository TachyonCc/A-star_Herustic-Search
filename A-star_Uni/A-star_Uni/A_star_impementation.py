import heapq

def astar(start_board, goal_board, heuristic_distance):
    #Convert boards to tuples 
    def to_tuple(board):
        return tuple(tuple(row) for row in board)

    start = to_tuple(start_board)
    goal = to_tuple(goal_board)

    #Open list stores (f_score, g_score, board)
    open_list = []
    heapq.heappush(open_list, (heuristic_distance(start_board, goal_board), 0, start))

    #Best known cost to reach each board
    g_scores = {start: 0}

    #Store previous boards to reconstruct the solution
    parents = {start: None}

    #Count expanded nodes for the experiment
    expanded_nodes = 0

    while open_list:
        f, g, current = heapq.heappop(open_list)

        #Skip outdated entries if a shorter path was already found
        if g > g_scores[current]:
            continue

        #Goal reached
        if current == goal:
            path = []

            while current is not None:
                path.append([list(row) for row in current])
                current = parents[current]

            path.reverse()
            return path, expanded_nodes

        expanded_nodes += 1

        #Convert tuple back to a 2D list for get_neighbors()
        current_board = [list(row) for row in current]

        for neighbor_board in get_neighbors(current_board):
            neighbor = to_tuple(neighbor_board)

            #Each move costs 1
            new_g = g + 1

            #Update only if this path is better
            if new_g < g_scores.get(neighbor, float("inf")):
                g_scores[neighbor] = new_g
                parents[neighbor] = current

                h = heuristic_distance(neighbor_board, goal_board)
                new_f = new_g + h

                heapq.heappush(open_list, (new_f, new_g, neighbor))

    #No solution found
    return None, expanded_nodes



def get_neighbors(board):
    neighborsCoordinates = []
    neighborsBoards = []
    row = -1
    column = -1

    #Find the empty tile
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                row = i
                column = j
                break

    #Safety Guard        
    if (row <0 or column <0):
        return  []

    #Determine which moves are valid
    if (row + 1 < len(board) ):
        neighborsCoordinates.append((row + 1, column))
    if (row - 1 >= 0 ):
        neighborsCoordinates.append((row - 1, column))
    if (column + 1 < len(board[0]) ):
        neighborsCoordinates.append((row, column + 1))
    if (column - 1 >= 0 ):
        neighborsCoordinates.append((row, column - 1))

    #Create a new board for each move
    for coord in neighborsCoordinates:
        newBoard = [r.copy() for r in board]
        
    #Swap the empty tile with its neighbor
        newRow, newCol = coord
        newBoard[row][column] = newBoard[newRow][newCol]
        newBoard[newRow][newCol] = 0

        neighborsBoards.append(newBoard)

    return neighborsBoards
