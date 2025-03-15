# bfs_solver.py
from cube import RubiksCube
from collections import deque

def bfs_solve(start_cube):
    visited = set()
    queue = deque([(start_cube, [])])
    while queue:
        current, path = queue.popleft()
        if current.is_solved():
            return path
        state_key = str(current.faces)
        if state_key in visited:
            continue
        visited.add(state_key)
        for move in current.get_all_possible_moves():
            new_cube = current.copy()
            new_cube.apply_move(move)
            queue.append((new_cube, path + [move]))
    return []
