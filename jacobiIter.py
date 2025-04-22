def jacobiIter(A, b, x, abstol=1.e-10, reltol=1.e-10, maxIter=100):
    n = A.shape[0]
    iter = 0  
    while True:
        iter += 1
        nx = np.array([(1/A[i,i])*(b[i] - np.dot(A[i,:], x) + A[i,i]*x[i]) for i in range(n)])
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
