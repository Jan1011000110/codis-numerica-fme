'''
Implementeu una funció en Python anomenada triL que realitzi la substitució endavant per a una matriu triangular inferior:

def triL(L, b, tol=1e-10)
'''

import numpy as np

def triL(L, b, tol=1e-10):
    n = b.shape[0]
    if L.shape[0] != L.shape[1]:
        raise ValueError(f"La matriu és {L.shape[0]}x{L.shape[1]} i ha de ser quadrada!")
    if n != L.shape[0]:
        raise ValueError(f"Dimensions incompatibles! (files matriu) {L.shape[0]} != {n} (elements vector)")
    for i in range(n):
        if np.abs(L[i,i]) < tol:
            raise ValueError("Element diagonal massa petit!")
    x = b.copy()
    for i in range(n):
        for j in range(i):
            x[i] -= L[i,j]*x[j]
        x[i] /= L[i,i]
    return x

'''
Modifica la funció triL del dia anterior de manera que hi hagi un paràmetre opcional anomenat ones que, quan ones=True presuposi que la matriu d'entrada té uns a la diagonals i no faci la divisió per l'element L[i,i]. És a dir, la funció ara serà:

triL(L, b, ones=False, tol=1.e-10)
'''

def triL(L, b, ones=False, tol=1.e-10):
    n = b.shape[0]
    if L.shape[0] != L.shape[1]:
        raise ValueError(f"La matriu és {L.shape[0]}x{L.shape[1]} i ha de ser quadrada!")
    if n != L.shape[0]:
        raise ValueError(f"Dimensions incompatibles! (files matriu) {L.shape[0]} != {n} (elements vector)")
    for i in range(n):
        if np.abs(L[i,i]) < tol:
            raise ValueError("Element diagonal massa petit!")
    x = b.copy(
    for i in range(n):
        for j in range(i):
            x[i] -= L[i,j]*x[j]
        if not ones:
            x[i] /= L[i,i]
    return x
