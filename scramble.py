import random

def scramble_cube(cube, num_moves=8):
    moves = ["U", "U'"]
    scramble_moves = []

    for _ in range(num_moves):
        move = random.choice(moves)
        cube.move(move)
        scramble_moves.append(move)

    return scramble_moves
