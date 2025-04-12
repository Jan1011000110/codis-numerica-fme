def qrsys(A,b):
    m, n = A.shape
    R = A.copy()
    Qtb = b.copy()
    for k in range(n):
        u = np.array(R[k:,k]).reshape(-1, 1)
        u[0] = u[0] + np.sign(u[0])*np.linalg.norm(u)
        u = u/np.linalg.norm(u)
        R[k:,k:] = R[k:,k:] - u @ (2 * u.T @ R[k:,k:])
        Qtb[k:] = Qtb[k:] - u @ (2 * u.T @ Qtb[k:])
    return R, Qtb
