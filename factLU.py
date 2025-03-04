import numpy as np

def factLU(A, tol = 1.e-10):
    M =
    n = A.shape[0]
    if n != A.shape[1]:
        raise ValueError("La matriu no és quadrada!")
    for i in range(n):
        if np.abs(A[i,i]) < tol:
            raise ValueError("Pivot massa petit! Matriu (pròxima a) singular!")
            
    for k in range(0,n-1):
        for i in range(k+1,n):
            m = A[i,k]/A[k,k]
            b[i] -= m*b[k]

            A[i,k] = 0
            for j in range(k+1,n):
                A[i,j] -= m*A[k,j]
