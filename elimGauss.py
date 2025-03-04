import numpy as np

def elimGauss(A,b,tol=1.e-10):
  for k in range(0,n-1):
    for i in range(k+1,n):
      m = A[i,k]/A[k,k]
      b[i] -= m*b[k]

      A[i,k] = 0
      for j in range(k+1,n):
        A[i,j] -= m*A[k,j]
    return A,b
