import numpy as np

def elimGauss(A,b,tol=1.e-10):
    n = b.shape[0]
    if U.shape[0] != U.shape[1]:
        raise ValueError(f"La matriu és {U.shape[0])}x{U.shape[1]} i ha de ser quadrada!")
    if n != U.shape[0]:
        raise ValueError(f"Dimensions incompatibles! (files matriu) {U.shape[0]} != {n} (elements vector)")
    for i in range(n):
        if np.abs(U[i,i]) < tol:
            raise ValueError("Element diagonal massa petit!")
  for k in range(0,n-1):
    for i in range(k+1,n):
      m = A[i,k]/A[k,k]
      b[i] -= m*b[k]

      A[i,k] = 0
      for j in range(k+1,n):
        A[i,j] -= m*A[k,j]
    return A,b
