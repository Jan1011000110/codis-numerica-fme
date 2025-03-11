import numpy as np

def cholesky(A, tol=1.e-10):
    n = A.shape[0]
    if n != A.shape[1]:
        raise ValueError("La matriu no és quadrada!")
    L = np.zeros((n,n))  
    for k in range(n):
        L[k,k] = np.sqrt(A[k,k] - np.dot(L[k,:k],L[k,:k]))
        if np.abs(L[k,k]) < tol:
            raise ValueError("Element diagonal massa petit! Matriu (pròxima a) singular!")
        for i in range(k+1,n):
            L[i,k] = (A[i,k] - np.dot(L[i,:k],L[k,:k])) / L[k,k]
    return L

  
