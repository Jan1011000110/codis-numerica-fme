def gradConj(A,b,x0,atol=1.e-10,rtol=1.e-10,maxIter=100):
    r = b - A@x0
    p = r
    gamma = r.T@r
    x = x0
    b_norm = np.linalg.norm(b)
    for niter in range(0, maxIter+1):
        a_norm = np.linalg.norm(r)
        r_norm = a_norm/b_norm  
        if a_norm < atol and r_norm < rtol:
            return x, niter
        if niter == maxIter:
            if a_norm > atol and r_norm > rtol:
                return x, -3
            elif a_norm > atol:
                return x, -1
            else:
                return x, -2
        y = A@p
        alpha = gamma/(p.T@y)
        x = x + alpha*p
        r = r - alpha*y
        prod_rTr = r.T@r
        beta = prod_rTr/gamma
        gamma = prod_rTr
        p = r + beta*p
