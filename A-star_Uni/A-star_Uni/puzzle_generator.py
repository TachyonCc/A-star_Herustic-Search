import random

def count_inversions(puzzle):
    inversions = 0
    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            if puzzle[i] != 0 and puzzle[j] != 0:  # Ignore the blank tile (0)
                if puzzle[i] > puzzle[j]:
                    inversions += 1
    return inversions

def is_solvable(puzzle):
    if count_inversions(puzzle) % 2 == 0:
        return True
    return False

def generate_random_puzzle():
    random_puzzle = list(range(9))
    random.shuffle(random_puzzle)
    if is_solvable(random_puzzle):
        return random_puzzle
    return generate_random_puzzle()

for _ in range(5):
    print(generate_random_puzzle())