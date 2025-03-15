import copy

class RubiksCube:
    def __init__(self):
        self.faces = {
            'U': ['W'] * 9,
            'D': ['Y'] * 9,
            'F': ['G'] * 9,
            'B': ['B'] * 9,
            'L': ['O'] * 9,
            'R': ['R'] * 9
        }

    def is_solved(self):
        return all(all(sticker == face[0] for sticker in face) for face in self.faces.values())

    def copy(self):
        new_cube = RubiksCube()
        new_cube.faces = copy.deepcopy(self.faces)
        return new_cube

    def apply_move(self, move):
        move_name = move.replace("'", "prime")
        rotate_fn = getattr(self, f"_move_{move_name}", None)
        if rotate_fn:
            rotate_fn()

    def get_all_possible_moves(self):
        return ['U', "U'", 'D', "D'", 'F', "F'", 'B', "B'", 'L', "L'", 'R', "R'"]

    def _rotate_face_clockwise(self, face):
        f = self.faces[face]
        self.faces[face] = [f[6], f[3], f[0],
                            f[7], f[4], f[1],
                            f[8], f[5], f[2]]

    def _rotate_face_counterclockwise(self, face):
        f = self.faces[face]
        self.faces[face] = [f[2], f[5], f[8],
                            f[1], f[4], f[7],
                            f[0], f[3], f[6]]

    def _move_U(self):
        self._rotate_face_clockwise('U')
        self._cycle_edges(['F', 'R', 'B', 'L'], [0, 1, 2])

    def _move_Uprime(self):
        self._rotate_face_counterclockwise('U')
        self._cycle_edges(['F', 'L', 'B', 'R'], [0, 1, 2])

    def _move_D(self):
        self._rotate_face_clockwise('D')
        self._cycle_edges(['F', 'L', 'B', 'R'], [6, 7, 8])

    def _move_Dprime(self):
        self._rotate_face_counterclockwise('D')
        self._cycle_edges(['F', 'R', 'B', 'L'], [6, 7, 8])

    def _move_F(self):
        self._rotate_face_clockwise('F')
        self._cycle_four_edges([
            ('U', [6,7,8]),
            ('R', [0,3,6]),
            ('D', [2,1,0]),
            ('L', [8,5,2])
        ])

    def _move_Fprime(self):
        self._rotate_face_counterclockwise('F')
        self._cycle_four_edges([
            ('U', [6,7,8]),
            ('L', [8,5,2]),
            ('D', [2,1,0]),
            ('R', [0,3,6])
        ])

    def _move_B(self):
        self._rotate_face_clockwise('B')
        self._cycle_four_edges([
            ('U', [0,1,2]),
            ('L', [0,3,6]),
            ('D', [8,7,6]),
            ('R', [8,5,2])
        ])

    def _move_Bprime(self):
        self._rotate_face_counterclockwise('B')
        self._cycle_four_edges([
            ('U', [0,1,2]),
            ('R', [8,5,2]),
            ('D', [8,7,6]),
            ('L', [0,3,6])
        ])

    def _move_L(self):
        self._rotate_face_clockwise('L')
        self._cycle_four_edges([
            ('U', [0,3,6]),
            ('F', [0,3,6]),
            ('D', [0,3,6]),
            ('B', [8,5,2])
        ])

    def _move_Lprime(self):
        self._rotate_face_counterclockwise('L')
        self._cycle_four_edges([
            ('U', [0,3,6]),
            ('B', [8,5,2]),
            ('D', [0,3,6]),
            ('F', [0,3,6])
        ])

    def _move_R(self):
        self._rotate_face_clockwise('R')
        self._cycle_four_edges([
            ('U', [2,5,8]),
            ('B', [6,3,0]),
            ('D', [2,5,8]),
            ('F', [2,5,8])
        ])

    def _move_Rprime(self):
        self._rotate_face_counterclockwise('R')
        self._cycle_four_edges([
            ('U', [2,5,8]),
            ('F', [2,5,8]),
            ('D', [2,5,8]),
            ('B', [6,3,0])
        ])

    def _cycle_edges(self, faces, indices):
        temp = [self.faces[faces[0]][i] for i in indices]
        for i in range(3):
            self.faces[faces[0]][indices[i]] = self.faces[faces[3]][indices[i]]
            self.faces[faces[3]][indices[i]] = self.faces[faces[2]][indices[i]]
            self.faces[faces[2]][indices[i]] = self.faces[faces[1]][indices[i]]
            self.faces[faces[1]][indices[i]] = temp[i]

    def _cycle_four_edges(self, positions):
        temp = [self.faces[positions[0][0]][i] for i in positions[0][1]]
        for i in range(3):
            self.faces[positions[0][0]][positions[0][1][i]] = self.faces[positions[3][0]][positions[3][1][i]]
            self.faces[positions[3][0]][positions[3][1][i]] = self.faces[positions[2][0]][positions[2][1][i]]
            self.faces[positions[2][0]][positions[2][1][i]] = self.faces[positions[1][0]][positions[1][1][i]]
            self.faces[positions[1][0]][positions[1][1][i]] = temp[i]
