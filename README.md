# Documentație MatxMatMul

## Clase

### `Processor`

Reprezintă un singur procesor în matricea sistolică.

#### Metode

- `__init__(self)`
  - Inițializează procesorul cu rezultatul acumulat zero și variabile pentru valorile matricilor A și B.

- `load_a(self, a)`
  - Încarcă o valoare din matricea A în procesor.

- `load_b(self, b)`
  - Încarcă o valoare din matricea B în procesor.

- `compute(self)`
  - Calculează produsul valorilor încărcate A și B dacă ambele sunt non-zero se adaugă la rezultatul acumulat.

- `pass_a_east(self)`
  - Transmite valoarea A la dreapta (est) și o resetează la zero.

- `pass_b_south(self)`
  - Transmite valoarea B în jos (sud) și o resetează la zero.

- `get_result(self)`
  - Returnează rezultatul acumulat al procesorului.

## Funcții

### `systolic_matrix_multiplication(A, B)`

Efectuează multiplicarea matricelor A și B

#### Parametri

- `A` (`np.ndarray`): Matricea din stânga în operația de multiplicare.
- `B` (`np.ndarray`): Matricea din dreapta în operația de multiplicare.

#### Returnează

- `C` (`np.ndarray`): Matricea rezultantă după multiplicare.

#### Descriere

Inițializează o grilă de instanțe `Processor` dimensionată conform matricilor de intrare A și B. Efectuează o serie de pași temporali, unde la fiecare pas:

- Încarcă noi valori în procesoare din matricile A și B.
- Propagă valorile A la dreapta (est) și valorile B în jos (sud) pe grilă.
- Calculează produsul valorilor curente A și B în fiecare procesor și acumulează rezultatul.

După finalizarea tuturor pașilor, funcția colectează rezultatele din procesoare în matricea rezultantă C.

## Utilizare

Pentru a efectua multiplicarea matricilor folosind această abordare sistolică, definiți matricile A și B ca tablouri NumPy și apelați funcția `systolic_matrix_multiplication` cu aceste tablouri.

```python
import numpy as np

# Definește matricile A și B
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Efectuează multiplicarea matricilor in stil sistolic
C = systolic_matrix_multiplication(A, B)
print(C)
