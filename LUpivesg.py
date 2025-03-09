import numpy as np

def LUpivesg(A, tol = 1.e-10):
    M = A.copy()
    n = A.shape[0]
    p = np.arange(n)
    if n != A.shape[1]:
        raise ValueError("La matriu no és quadrada!")
    
    for k in range(n-1):
        s = np.max(np.abs(M[k:,k:]), axis=1)
        index = k + np.argmax(np.abs(M[k:,k]/s)) 
        p[[k,index]] = p[[index,k]]
        M[[k,index]] = M[[index,k]]
        for i in range(k+1,n):
            if np.abs(M[k,k]) < tol:
                raise ValueError("Pivot massa petit! Matriu (pròxima a) singular!")
            m = M[i,k]/M[k,k]
            M[i,k] = m
            for j in range(k+1,n):
                M[i,j] -= m*M[k,j]
    return M, p
