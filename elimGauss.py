import numpy as np

def elimGauss(A,b,tol=1.e-10):
    n = b.shape[0]
    if A.shape[0] != A.shape[1]:
        raise ValueError(f"La matriu és {A.shape[0]}x{A.shape[1]} i ha de ser quadrada!")
    if n != A.shape[0]:
        raise ValueError(f"Dimensions incompatibles! (files matriu) {A.shape[0]} != {n} (elements vector)")
    for i in range(n):
        if np.abs(A[i,i]) < tol:
            raise ValueError(f"El pivot del pas {i} està per sota la tolerància ({tol})")
    for k in range(0,n-1):
        for i in range(k+1,n):
            m = A[i,k]/A[k,k]
            b[i] -= m*b[k]

            A[i,k] = 0
            for j in range(k+1,n):
                A[i,j] -= m*A[k,j]
    return A,b
