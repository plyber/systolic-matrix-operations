import numpy as np

class Processor:
    def __init__(self):
        self.v = 0  # valoarea acumulata a v
        self.u_prime = 0

    def compute(self, a, u):
        # calculul v pe baza a si u
        self.v += a * u
        print(f"Processor compute: a={a}, u={u}, v={self.v}")
        # stocarea u pentru a fi transmis
        self.u_prime = u

    def get_u_prime(self):
        # return u_prime pentru a fi transmis
        return self.u_prime

    def get_result(self):
        # return valoarea finala acumulata
        return self.v

def linear_systolic_matrix_vector_multiplication(A, U):
    n, m = A.shape
    processors = [Processor() for _ in range(n)]
    V = np.zeros(n)  # Result vector

    for step in range(m + n - 1):
        print(f"\nTime step {step}:")

        # determinarea elementului corespunzator din U
        u_input = U[step] if step < m else 0

        # atribuirea in procesoare a elementelor corespunzatoare din U si A
        for i in reversed(range(n)):
            # atribuirea elementului corespunator din A in contextul time stepului curent
            a_input = A[i, step - i] if 0 <= step - i < m else 0
            # primul procesor primește u_input, restul primesc de la procesorul anterior
            u_to_process = u_input if i == 0 else processors[i - 1].get_u_prime()
            processors[i].compute(a_input, u_to_process)

    for i, proc in enumerate(processors):
        V[i] = proc.get_result()
        print(f"Final result from processor {i}: v={V[i]}")

    return V


A = np.array([[1, 2, 3, 4, 5], [5, 6, 7, 8, 5], [9, 10, 11, 12, 5]])
U = np.array([1, 2, 3, 4, 5])

V = linear_systolic_matrix_vector_multiplication(A, U)
print("\nFinal result vector V:", V)
