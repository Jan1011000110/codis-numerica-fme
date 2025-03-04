'''
Implementeu una funció en Python anomenada triU que realitzi la substitució endarrere per a una matriu triangular superior:

def triU(U, b, tol=1e-10):

on

    U és una matriu triangular superior (és a dir, suposarem que tots els elements sota la diagonal principal són zero).

    b és un vector de termes independents.

    tol és un valor de tolerància per a elements diagonals petits. Si un element diagonal és menor que tol en valor absolut, la funció ha de llançar un error amb el missatge “Element diagonal massa petit!”. Això es pot fer amb el codi: raise ValueError("Element diagonal massa petit!")

La funció triU ha de retornar un vector x que sigui la solució del sistema lineal Ux = b.

A més, la funció ha de retornar els següents errors:

    Si la matriu U no és una matriu quadrada retornarà un error dient: “La matriu és {files}x{columnes} i ha de ser quadrada!” on {files} i {columnes} són el nombre de files i columnes que té la matriu U respectivament. Feu-ho emprant raise ValueError(f"...").

    Si la matriu U és quadrada però el vector b té dimensions incompatibles retorneu l'error: “Dimensions incompatibles! (files matriu) {files} != {elements_vector} (elements vector)” on {files} són el nombre de files de la matriu U i {elements_vector} és el nombre d'elements del vector b. Feu-ho emprant raise ValueError(f"...").
'''

import numpy as np

def triU(U, b, tol=1e-10):
    n = len(b)
    if len(U) > 0 and len(U) != len(U[0]):
        raise ValueError(f"La matriu és {len(U)}x{len(U[0])} i ha de ser quadrada!")
    if n != len(U):
        raise ValueError(f"Dimensions incompatibles! (files matriu) {len(U)} != {n} (elements vector)")
    for i in range(n):
        if np.abs(U[i][i]) < tol:
            raise ValueError("Element diagonal massa petit!")
    x = b
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]
    return x
