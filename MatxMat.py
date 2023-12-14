import numpy as np

class Processor:
    def __init__(self):
        self.c = 0  # rezultatul acumulat
        self.a = 0  # valoarea din matricea A
        self.b = 0  # valoarea din matricea B

    def load_a(self, a):
        self.a = a

    def load_b(self, b):
        self.b = b

    def compute(self):
        # calculeaza si paseaza doar daca a si b !=0
        if self.a != 0 and self.b != 0:
            self.c += self.a * self.b

    def pass_a_east(self):
        # paseaza A la dreapta
        passed_value = self.a
        self.a = 0  # reseteaza a dupa pasarea la est
        return passed_value

    def pass_b_south(self):
        # Pass B value down
        passed_value = self.b
        self.b = 0  # reseteaza b dupa pasarea la sud
        return passed_value

    def get_result(self):
        return self.c


def systolic_matrix_multiplication(A, B):
    a_rows, a_cols = A.shape
    b_cols = B.shape[1]
    C = np.zeros((a_rows, b_cols))

    processors = [[Processor() for _ in range(b_cols)] for _ in range(a_rows)]

    for step in range(a_rows + a_cols - 1):
        print(f'TIME STEP {step}')
        # incarca valorile in procesoare
        for i in range(a_rows):
            if step < a_cols:
                processors[i][0].load_a(A[i, step])
                print(f'PROCESSOR {i, 0} LOAD A: {A[i, step]}')
        for j in range(b_cols):
            if step < b_cols:
                processors[0][j].load_b(B[step, j])
                print(f'PROCESSOR {0, j} LOAD B: {B[step, j]}')

        # propagă A și B și calculează
        for i in range(a_rows):
            for j in range(b_cols):
                processors[i][j].compute()
                print(f'PROCESSOR {i, j} COMPUTE {processors[i][j].a}*{processors[i][j].b}={processors[i][j].c}')
                if j < b_cols - 1:

                    a_to_pass = processors[i][j].pass_a_east()
                    print(f'PROCESSOR {i, j} PASS a {a_to_pass}')

                    processors[i][j + 1].load_a(a_to_pass)
                    print(f'PROCESSOR {i, j+1} LOAD a {a_to_pass}')
                if i < a_rows - 1:

                    b_to_pass = processors[i][j].pass_b_south()
                    print(f'PROCESSOR {i, j} PASS b {b_to_pass}')

                    processors[i + 1][j].load_b(b_to_pass)
                    print(f'PROCESSOR {i+1, j} LOAD b {b_to_pass}')

    # colectarea rezultatului c
    for i in range(a_rows):
        for j in range(b_cols):
            C[i, j] = processors[i][j].get_result()

    return C


A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])


C = systolic_matrix_multiplication(A, B)

print(C)