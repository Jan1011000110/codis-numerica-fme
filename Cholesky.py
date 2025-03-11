import numpy as np

def cholesky(A, tol=1.e-10):
  n = A.shape[0]
  L = np.zeros((n,n))  
  
