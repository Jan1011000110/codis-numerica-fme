'''
Implementeu una funció en Python anomenada triL que realitzi la substitució endavant per a una matriu triangular inferior:

def triL(L, b, tol=1e-10)
'''

import numpy as np

def triL(L, b, tol=1e-10):
    n = len(b)
    if len(L) > 0 and len(L) != len(L[0]):
        raise ValueError(f"La matriu és {len(L)}x{len(L[0])} i ha de ser quadrada!")
    if n != len(L):
        raise ValueError(f"Dimensions incompatibles! (files matriu) {len(L)} != {n} (elements vector)")
    for i in range(n):
        if np.abs(L[i][i]) < tol:
            raise ValueError("Element diagonal massa petit!")
    x = b
    for i in range(n):
        for j in range(i):
            x[i] -= L[i][j] * x[j]
        x[i] /= L[i][i]
    return x
