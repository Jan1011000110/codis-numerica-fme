def jacobi(A,tol=1.e-10,maxIter=1.e5):
    n = A.shape[0]
    Q = np.eye(n)
    for it in range(int(maxIter)):
        p, q = np.unravel_index(np.abs(np.triu(A, k=1)).argmax(), (n, n))
        if np.abs(A[p,q]) < tol:
            return A, Q, it
        eta = (A[p,p] - A[q,q])/(2*A[p,q])
        t = 1
        if eta > 0:
            t = -eta - np.sqrt(1 + eta**2)
        elif eta < 0:
            t = -eta + np.sqrt(1 + eta**2)
        cos_phi = (1/np.sqrt(1 + t**2))
        sin_phi = t*cos_phi
        
        A_pp = A[p,p]*(cos_phi**2) + 2*A[p,q]*cos_phi*sin_phi + A[q,q]*(sin_phi**2)
        A_qq = A[p,p]*(sin_phi**2) - 2*A[p,q]*cos_phi*sin_phi + A[q,q]*(cos_phi**2)
        A_pr = [A[p,r]*cos_phi + A[q,r]*sin_phi for r in range(n)]
        A_qr = [-A[p,r]*sin_phi + A[q,r]*cos_phi for r in range(n)]
        
        A[p,q] = A[q,p] = 0
        A[p,p], A[q,q] = A_pp, A_qq
        for r in range(n):
            if r != p and r != q:
                A[p,r] = A[r,p] = A_pr[r]
                A[q,r] = A[r,q] = A_qr[r]

        
        Q_rp = [Q[r,p]*cos_phi + Q[r,q]*sin_phi for r in range(n)]
        Q_rq = [-Q[r,p]*sin_phi + Q[r,q]*cos_phi for r in range(n)]
        for r in range(n):
            Q[r,p] = Q_rp[r]
            Q[r,q] = Q_rq[r]

    return A, Q, -maxIter
