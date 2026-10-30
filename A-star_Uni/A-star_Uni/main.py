
from puzzle_generator import generate_random_puzzle
from heuristic_funcs import hamming_distance, manhattan_distance
from A_star_impementation import astar
import time

Goal_Board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


def print_board(board):
    for row in board:
        print(row)


def run_experiments(puzzles, heuristic):
    total_nodes = 0
    total_time = 0

    for board in puzzles:
        start_time = time.perf_counter()

        path, expanded_nodes = astar(board, Goal_Board, heuristic)

        end_time = time.perf_counter()

        if path is None:
            print("No solution found!")
            continue

        total_nodes += expanded_nodes
        total_time += end_time - start_time

    average_nodes = total_nodes / len(puzzles)
    average_time = (total_time / len(puzzles)) * 1000

    return average_nodes, average_time


def main():
    #Generate 100 puzzles for both heuristics
    puzzles = [generate_random_puzzle() for i in range(100)]

    print("=== 8-Puzzle A* Comparison ===")

    #Hamming
    hamming_nodes, hamming_time = run_experiments(
        puzzles, hamming_distance
    )

    #Manhattan
    manhattan_nodes, manhattan_time = run_experiments(
        puzzles, manhattan_distance
    )

    #Print comparison results
    print("\nResults from 100 random puzzles:")
    print("----------------------------------")

    print("Hamming Distance:")
    print(f"Average expanded nodes: {hamming_nodes:.2f}")
    print(f"Average computation time: {hamming_time:.3f} ms")

    print("\nManhattan Distance:")
    print(f"Average expanded nodes: {manhattan_nodes:.2f}")
    print(f"Average computation time: {manhattan_time:.3f} ms")

    #Show one example solution
    print("\n=== Example Solution ===")
    print("Starting puzzle:")
    print_board(puzzles[0])

    path, expanded = astar(puzzles[0], Goal_Board, manhattan_distance)

    if path is not None:
        print(f"\nPuzzle solved in {len(path) - 1} moves!")
        print(f"Expanded nodes: {expanded}")

        print("\nSolved board:")
        print_board(path[-1])
    else:
        print("No solution found!")


if __name__ == "__main__":
    main()