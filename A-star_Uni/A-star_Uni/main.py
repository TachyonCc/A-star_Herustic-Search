"""Compare two heuristics on 100 boards; print mean and sample std. dev."""

import statistics
import time

from A_star_impementation import astar
from heuristic_funcs import hamming_distance, manhattan_distance
from puzzle_generator import generate_random_puzzle


GOAL_BOARD = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0],
]


def print_board(board):
    for row in board:
        print(row)


def run_experiments(puzzles, heuristic):
    nodes_results = []
    time_results = []

    for board in puzzles:
        start_time = time.perf_counter()
        path, expanded_nodes = astar(board, GOAL_BOARD, heuristic)
        elapsed_ms = (time.perf_counter() - start_time) * 1000

        if path is None:
            raise RuntimeError("A generated solvable puzzle could not be solved.")

        nodes_results.append(expanded_nodes)
        time_results.append(elapsed_ms)

    return {
        "mean_nodes": statistics.mean(nodes_results),
        "std_nodes": statistics.stdev(nodes_results),
        "mean_time_ms": statistics.mean(time_results),
        "std_time_ms": statistics.stdev(time_results),
    }


def print_results(name, results):
    print(f"\n{name}:")
    print(f"Mean expanded nodes: {results['mean_nodes']:.2f}")
    print(f"Sample std. dev. of expanded nodes: {results['std_nodes']:.2f}")
    print(f"Mean computation time: {results['mean_time_ms']:.3f} ms")
    print(f"Sample std. dev. of computation time: {results['std_time_ms']:.3f} ms")


def main():
    puzzles = [generate_random_puzzle() for _ in range(100)]

    print("=== 8-Puzzle A* Comparison ===", flush=True)
    print("Results from the same 100 random solvable puzzles:")

    hamming_results = run_experiments(puzzles, hamming_distance)
    print_results("Hamming Distance", hamming_results)

    manhattan_results = run_experiments(puzzles, manhattan_distance)
    print_results("Manhattan Distance", manhattan_results)

    print("\n=== Example Solution (Manhattan) ===")
    print("Starting puzzle:")
    print_board(puzzles[0])

    path, expanded = astar(puzzles[0], GOAL_BOARD, manhattan_distance)
    if path is None:
        raise RuntimeError("The example puzzle could not be solved.")

    print(f"\nPuzzle solved in {len(path) - 1} moves!")
    print(f"Expanded nodes: {expanded}")
    print("\nSolved board:")
    print_board(path[-1])


if __name__ == "__main__":
    main()
