import heapq

##A* takes start, goal and heuristic; returns (path, expanded_nodes).
##Path is None if unreachable. get_neighbors returns boards one legal move away.

def astar(start_board, goal_board, heuristic_distance):
    # Tuples let us use boards as dictionary keys.
    def to_tuple(board):
        return tuple(tuple(row) for row in board)

    start = to_tuple(start_board)
    goal = to_tuple(goal_board)

    # The priority queue orders entries by (f_score, g_score, board).
    open_list = [(heuristic_distance(start_board, goal_board), 0, start)]
    g_scores = {start: 0}
    parents = {start: None}
    expanded_nodes = 0

    while open_list:
        _, g_score, current = heapq.heappop(open_list)

        # A board may still have an older, longer route in the queue.
        if g_score > g_scores[current]:
            continue

        if current == goal:
            path = []
            while current is not None:
                path.append([list(row) for row in current])
                current = parents[current]

            path.reverse()
            return path, expanded_nodes

        expanded_nodes += 1
        current_board = [list(row) for row in current]

        for neighbor_board in get_neighbors(current_board):
            neighbor = to_tuple(neighbor_board)
            new_g_score = g_score + 1

            if new_g_score < g_scores.get(neighbor, float("inf")):
                g_scores[neighbor] = new_g_score
                parents[neighbor] = current

                h_score = heuristic_distance(neighbor_board, goal_board)
                f_score = new_g_score + h_score
                heapq.heappush(open_list, (f_score, new_g_score, neighbor))

    return None, expanded_nodes


def get_neighbors(board):
    blank_row = -1
    blank_col = -1

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                blank_row, blank_col = row, col
                break
        if blank_row != -1:
            break

    if blank_row == -1:
        return []

    neighbor_positions = [
        (blank_row + 1, blank_col),
        (blank_row - 1, blank_col),
        (blank_row, blank_col + 1),
        (blank_row, blank_col - 1),
    ]

    neighbors = []
    for row, col in neighbor_positions:
        if 0 <= row < len(board) and 0 <= col < len(board[0]):
            new_board = [r.copy() for r in board]
            new_board[blank_row][blank_col] = new_board[row][col]
            new_board[row][col] = 0
            neighbors.append(new_board)

    return neighbors
