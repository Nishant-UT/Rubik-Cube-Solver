# iddfs_solver_func.py

from cube import RubiksCube

def iddfs_solve(start_cube, max_depth=20):
    def dls(cube, depth, path, visited):
        if cube.is_solved():
            return path
        if depth == 0:
            return None
        cube_key = str(cube.faces)
        if cube_key in visited:
            return None
        visited.add(cube_key)

        for move in cube.get_all_possible_moves():
            new_cube = cube.copy()
            new_cube.apply_move(move)
            result = dls(new_cube, depth - 1, path + [move], visited.copy())
            if result:
                return result
        return None

    for depth in range(1, max_depth + 1):
        result = dls(start_cube, depth, [], set())
        if result:
            return result
    return None
