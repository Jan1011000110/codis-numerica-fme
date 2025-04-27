# We are actually solving a triangular internally
def GaussSeidel(A, b, x, abstol=1.e-10, reltol=1.e-10, maxIter=100):
    n = A.shape[0]
    iter = 0  
    while True:
        iter += 1
        nx = np.zeros(n)
        for i in range(n):
            nx[i] = (1/A[i,i])*(b[i] - np.dot(A[i,:i], nx[:i]) - np.dot(A[i,i+1:], x[i+1:]))
        abs_norm = np.linalg.norm(nx - x)
        rel_norm = abs_norm/np.linalg.norm(nx)
        x = nx
        if abs_norm < abstol and rel_norm < reltol:
            return x, iter
        if iter == maxIter:
            if abs_norm < abstol:
                return x, -2
            elif rel_norm < reltol:
                return x, -1
            else:
                return x, -3
