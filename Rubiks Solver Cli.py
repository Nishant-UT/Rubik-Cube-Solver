import argparse
import time
from cube import RubiksCube
from scramble import scramble_cube
from bfs_solver import bfs_solver
from dfs_solve import dfs_solver
from iddfs_solve import iddfs_solver
from ida_star_solve import ida_star_solver


def main():
    parser = argparse.ArgumentParser(description="Rubik's Cube Solver CLI")
    parser.add_argument("--scramble", type=int, default=8, help="Number of random moves to scramble the cube")
    parser.add_argument("--algo", type=str, default="ida_star",
                        choices=["bfs", "dfs", "iddfs", "ida_star"], help="Algorithm to solve the cube")
    args = parser.parse_args()

    print(f"\nInitializing 3x3 Rubik's Cube and scrambling with {args.scramble} moves...")
    cube = RubiksCube()
    scramble_moves = scramble_cube(cube, args.scramble)
    print("Scramble moves:", ' '.join(scramble_moves))

    start_time = time.time()

    if args.algo == "bfs":
        solution = bfs_solver(cube)
    elif args.algo == "dfs":
        solution = dfs_solver(cube)
    elif args.algo == "iddfs":
        solution = iddfs_solver(cube)
    else:
        solution = ida_star_solver(cube)

    end_time = time.time()

    print("\nSolution:", ' '.join(solution))
    print(f"Solved in {len(solution)} moves and {end_time - start_time:.3f} seconds.")


if __name__ == "__main__":
    main()
