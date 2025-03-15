# ida_star_solver_func.py

from cube import RubiksCube

# Heuristic: number of misplaced stickers
def heuristic(cube):
    misplaced = 0
    for face in cube.faces.values():
        color = face[4]
        misplaced += sum(1 for sticker in face if sticker != color)
    return misplaced

def ida_star_solve(start_cube):
    bound = heuristic(start_cube)
    path = [(start_cube, [])]

    def search(path, g, bound):
        node, moves = path[-1]
        f = g + heuristic(node)
        if f > bound:
            return f, None
        if node.is_solved():
            return f, moves

        min_bound = float('inf')
        for move in node.get_all_possible_moves():
            new_cube = node.copy()
            new_cube.apply_move(move)

            if any(str(new_cube.faces) == str(p[0].faces) for p in path):
                continue

            path.append((new_cube, moves + [move]))
            t, result = search(path, g + 1, bound)
            if result is not None:
                return t, result
            if t < min_bound:
                min_bound = t
            path.pop()
        return min_bound, None

    while True:
        t, result = search(path, 0, bound)
        if result is not None:
            return result
        if t == float('inf'):
            return None
        bound = t
