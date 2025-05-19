class SparseMatrix:
    def __init__(self, file_path=None):
        # Stores non-zero elements using (row, col) as key
        self.data = {}
        self.rows = 0
        self.cols = 0
        if file_path:
            self.load_from_file(file_path)

    def load_from_file(self, file_path):
        """
        Load matrix data from a file with format:
        rows=<num>
        cols=<num>
        (row, col, value)
        """
        with open(file_path, 'r') as file:
            lines = file.readlines()
            self.rows = int(lines[0].split('=')[1])
            self.cols = int(lines[1].split('=')[1])
            for line in lines[2:]:
                if line.strip():
                    row, col, val = map(int, line.strip()[1:-1].split(','))
                    self.set(row, col, val)

    def get(self, row, col):
        # Returns value at (row, col), or 0 if not set
        return self.data.get((row, col), 0)

    def set(self, row, col, value):
        # Adds or removes element depending on value
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]

    def add(self, other):
        # Add two matrices
        result = SparseMatrix()
        result.rows = self.rows
        result.cols = self.cols
        all_keys = set(self.data.keys()).union(other.data.keys())
        for key in all_keys:
            result.set(*key, self.get(*key) + other.get(*key))
        return result

    def subtract(self, other):
        # Subtract two matrices
        result = SparseMatrix()
        result.rows = self.rows
        result.cols = self.cols
        all_keys = set(self.data.keys()).union(other.data.keys())
        for key in all_keys:
            result.set(*key, self.get(*key) - other.get(*key))
        return result

    def multiply(self, other):
        # Multiply two matrices (A x B)
        result = SparseMatrix()
        result.rows = self.rows
        result.cols = other.cols
        for (i, k), val1 in self.data.items():
            for j in range(other.cols):
                val2 = other.get(k, j)
                if val2:
                    result.set(i, j, result.get(i, j) + val1 * val2)
        return result

    def __str__(self):
        # Returns string in file format
        lines = [f"rows={self.rows}", f"cols={self.cols}"]
        for (i, j), v in sorted(self.data.items()):
            lines.append(f"({i}, {j}, {v})")
        return "\n".join(lines)
