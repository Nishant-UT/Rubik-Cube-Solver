import tkinter as tk
from threading import Thread
import time
from cube import RubiksCube
from bfs_solver import bfs_solve
from dfs_solve import dfs_solve
from iddfs_solve import iddfs_solve
from ida_star_solve import ida_star_solve

ALGORITHMS = {
    "BFS": bfs_solve,
    "DFS": dfs_solve,
    "IDDFS": iddfs_solve,
    "IDA*": ida_star_solve
}

SCRAMBLE_SEQUENCE = ["U", "R", "U'", "L"]

class SolverVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Rubik's Cube Solver - Algorithm Comparison")
        self.frames = {}

        for i, algo in enumerate(ALGORITHMS):
            frame = tk.LabelFrame(root, text=algo, padx=10, pady=10)
            frame.grid(row=0, column=i, padx=10, pady=10)
            self.frames[algo] = {
                'frame': frame,
                'canvas': self.create_cube_display(frame),
                'status': tk.Label(frame, text="Status: Ready"),
                'time': tk.Label(frame, text="Time: 0.0s")
            }
            self.frames[algo]['status'].pack()
            self.frames[algo]['time'].pack()

        self.start_button = tk.Button(root, text="Start All Solvers", command=self.run_all_solvers)
        self.start_button.grid(row=1, column=0, columnspan=4, pady=10)

    def create_cube_display(self, parent):
        canvas = tk.Canvas(parent, width=150, height=150)
        canvas.pack()
        squares = []
        for row in range(3):
            for col in range(3):
                rect = canvas.create_rectangle(10+col*30, 10+row*30, 40+col*30, 40+row*30, fill='white')
                squares.append(rect)
        return canvas

    def update_cube_display(self, canvas, cube_face):
        face_colors = {
            'W': 'white', 'Y': 'yellow', 'G': 'green',
            'B': 'blue', 'R': 'red', 'O': 'orange'
        }
        for i, sticker in enumerate(cube_face):
            canvas.itemconfig(i+1, fill=face_colors.get(sticker, 'gray'))

    def run_solver(self, algo_name, solver_func):
        start_time = time.time()
        cube = RubiksCube()
        for move in SCRAMBLE_SEQUENCE:
            cube.apply_move(move)

        self.update_cube_display(self.frames[algo_name]['canvas'], cube.faces['F'])

        solution = solver_func(cube)

        for move in solution:
            cube.apply_move(move)
            self.update_cube_display(self.frames[algo_name]['canvas'], cube.faces['F'])
            time.sleep(0.3)

        end_time = time.time()
        self.frames[algo_name]['status'].config(text="Status: Done")
        self.frames[algo_name]['time'].config(text=f"Time: {round(end_time - start_time, 2)}s")

    def run_all_solvers(self):
        for algo_name, solver_func in ALGORITHMS.items():
            thread = Thread(target=self.run_solver, args=(algo_name, solver_func))
            thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = SolverVisualizer(root)
    root.mainloop()
