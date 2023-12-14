# Documentație MatxMat

## Clase

## Clasa `Processor`
Reprezintă un procesor individual în aranjamentul de matrici `AxB[1]`. Fiecare procesor stochează valorile curente din matricile A și B, efectuează calcule și acumulează rezultatul.

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

1. **Inițializarea matricii rezultatului și a procesoarelor:**
   - Matricea C este inițializată ca o matrice de zerouri cu dimensiunile rezultatului final al multiplicării.
   - Se creează un grid de procesoare, cu fiecare procesor reprezentând un element în matricea C.

2. **Parcurgerea pașilor de calcul:**
   - Funcția iterează printr-o serie de pași, fiecare pas corespunzând unei faze a calculelor în aranjamentul sistolic.
   - Numărul total de pași este `a_rows + a_cols - 1`, asigurându-se că toate valorile din matricile A și B sunt procesate.

3. **Încărcarea valorilor în procesoare:**
   - La fiecare pas, valorile corespunzătoare din matricile A și B sunt încărcate în procesoare.
   - Pentru matricea A, valorile sunt încărcate în coloana 0 a procesoarelor, iar pentru matricea B, în rândul 0.
   - Indicii `a_index` și `b_index` sunt calculați pentru a determina ce valori trebuie încărcate în fiecare procesor.

4. **Calcul și propagare:**
   - Fiecare procesor efectuează un calcul (înmulțirea valorilor A și B curente) și adaugă rezultatul la valoarea acumulată.
   - După calcul, fiecare procesor pasează valorile A și B către procesorii vecini (dreapta și jos).

5. **Colectarea rezultatelor:**
   - După ce toți pașii sunt finalizați, rezultatele acumulate de fiecare procesor sunt colectate pentru a forma matricea C finală.

#### Parametri

- `A` : Matricea din stânga în operația de multiplicare.
- `B` : Matricea din sus în operația de multiplicare.

#### Returnează

- `C` : Matricea rezultantă după multiplicare.

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
