# dfs_solver_func.py

from cube import RubiksCube

def dfs_solve(start_cube, max_depth=10):
    visited = set()
    path = []

    def dfs(cube, depth):
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
            path.append(move)
            result = dfs(new_cube, depth - 1)
            if result:
                return result
            path.pop()
        return None

    return dfs(start_cube, max_depth)
