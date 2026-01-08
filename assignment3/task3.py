import numpy as np
import os

class Process:
    def __init__(self, filename):
        self.filename = filename
        self.rows = self._read_file()
        self.A, self.b = self._build_system()

    # Read & parse file
    def _read_file(self):
        rows = []
        with open(self.filename, "r") as f:
            for line in f:
                tokens = line.split() # split by whitespace
                rows.append(tokens)
        return rows

    # Count coefficients & build matrices
    def _build_system(self):
        coef_rows = []
        b_vals = []

        # how many variables exist (x1..xN)
        max_var = 0
        for row in self.rows:
            for t in row:
                if t.startswith('x') or t.startswith('-x'):
                    num = int(t.replace('-','').replace('x',''))
                    max_var = max(max_var, num)

        for row in self.rows:
            counter = {}

            for token in row:
                if token not in counter:
                    counter[token] = 1
                else:
                    counter[token] += 1

            # coefficients for x1..xN
            coef = []
            for i in range(1, max_var + 1):
                pos = counter.get(f"x{i}", 0)
                neg = counter.get(f"-x{i}", 0)
                coef.append(pos - neg)

            # b value
            b_val = counter.get("b", 0) - counter.get("-b", 0)

            coef_rows.append(coef)
            b_vals.append(b_val)

        A = np.array(coef_rows, dtype=float)
        b = np.array(b_vals, dtype=float)

        return A, b

    # Solve using Cramer's rule
    def determinant(self):
        return np.linalg.det(self.A)

    def solve_cramer(self):
        detA = self.determinant()
        if abs(detA) < 1e-12:
            return None  # no unique solution

        n = len(self.b)
        roots = np.zeros(n)

        for i in range(n):
            Ai = self.A.copy()
            Ai[:, i] = self.b  # replace column
            roots[i] = np.linalg.det(Ai) / detA

        return roots

    def norm(self):
        sol = self.solve_cramer()
        if sol is None:
            return 0
        return np.linalg.norm(sol)
    
# Path to the data folder
data_folder = 'data'

# Get all files in the data folder
files = [f for f in os.listdir(data_folder) if os.path.isfile(os.path.join(data_folder, f))]
print("Files found:", files)

# Create Process objects for each file
processes = [Process(os.path.join(data_folder, f)) for f in files]

for p in processes:
    try:
        roots = p.solve_cramer()
        if roots is None:
            print(f"File {p.filename}: no unique solution")
        else:
            print(f"File {p.filename}: roots = {roots}")
    except np.linalg.LinAlgError:
        print(f"File {p.filename}: matrix is not square, cannot solve")