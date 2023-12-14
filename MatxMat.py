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
    a_rows, a_cols = A.shape
    b_cols = B.shape[1]
    C = np.zeros((a_rows, b_cols))

    processors = [[Processor() for _ in range(b_cols)] for _ in range(a_rows)]

    for step in range(a_rows + a_cols - 1):
        print(f'\n--- TIME STEP {step} ---')
        # incarca valorile in procesoare
        for i in range(a_rows):
            a_index = step - i
            if 0 <= a_index < a_cols:
                print(f'PROCESSOR {i, 0} LOAD A: {A[i, a_index]}')
                processors[i][0].load_a(A[i, a_index])

        for j in range(b_cols):
            b_index = step - j
            if 0 <= b_index < a_cols:
                print(f'PROCESSOR {0, j} LOAD B: {B[b_index, j]}')
                processors[0][j].load_b(B[b_index, j])

        # calculeaza, paseaza si reseteaza pentru urmatoarea iteratie
        for i in reversed(range(a_rows)):
            for j in reversed(range(b_cols)):
                processors[i][j].compute()
                print(f'PROCESSOR {i, j} COMPUTE {processors[i][j].a} * {processors[i][j].b} = {processors[i][j].c} ')
                if j < b_cols - 1:
                    a_to_pass = processors[i][j].pass_a_east()
                    print(f'PROCESSOR {i, j} PASS A {a_to_pass}')
                    processors[i][j + 1].load_a(a_to_pass)
                if i < a_rows - 1:
                    b_to_pass = processors[i][j].pass_b_south()
                    print(f'PROCESSOR {i, j} PASS B {b_to_pass}')
                    processors[i + 1][j].load_b(b_to_pass)

    for i in range(a_rows):
        for j in range(b_cols):
            C[i, j] = processors[i][j].get_result()

    return C


A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

C = systolic_matrix_multiplication(A, B)

print("\nC:")
print(C)
