import numpy as np


class Processor:
    def __init__(self):
        self.c = 0
        self.a = 0
        self.b = 0

    def load_a(self, a):
        self.a = a

    def load_b(self, b):
        self.b = b

    def compute(self):
        self.c += self.a * self.b

    def pass_a_east(self):
        passed_value = self.a
        self.a = 0  # reseteaza a = 0
        return passed_value

    def pass_b_south(self):
        passed_value = self.b
        self.b = 0  # # reseteaza b = 0
        return passed_value

    def get_result(self):
        return self.c


def systolic_matrix_multiplication(A, B):

    runtime=5;

    a_rows, a_cols = A.shape
    b_cols, b_rows = B.shape
    C = np.zeros((a_rows, b_cols))

    processors = [[Processor() for _ in range(b_cols)] for _ in range(a_rows)]

    for step in range(a_rows + a_cols + runtime):
        print(f'\n--- TIME STEP {step} ---')
        # incarca valorile in procesoare
        for i in reversed(range(a_rows)):
            for j in reversed(range(b_cols)):
                processors[i][j].a = processors[i][j - 1].a if j > 0 else A[i, step - i] if 0 <= step - i < a_rows else 0
                processors[i][j].b = processors[i - 1][j].b if i > 0 else B[step - j, j] if 0 <= step - j < b_cols else 0
                processors[i][j].compute()

        # afiseaza date
        for i in range(a_rows):
            for j in range(b_cols):
                print(f'PROCESSOR {i, j} COMPUTE: + {processors[i][j].a} * {processors[i][j].b} = {processors[i][j].c}')

    #colecteaza datele
    for i in range(a_rows):
        for j in range(b_cols):
            C[i, j] = processors[i][j].get_result()

    return C


A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

C = systolic_matrix_multiplication(A, B)

print("\nC:")
print(C)
