def grad(A,b,x0,atol=1.e-10,rtol=1.e-10,maxIter=100):
    r = b - A@x0
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
        prod_Ar = A@r
        alpha = (r.T@r)/(r.T@prod_Ar)
        x = x + alpha*r
        r = r - alpha*prod_Ar
