def qrHouseholder(A):
    m, n = A.shape
    Q = np.eye(n)
    for k in range(n):
        u = np.array(A[k:,k]).reshape(-1, 1)
        u[0] = u[0] + np.sign(u[0])*np.linalg.norm(u)
        u = u/np.linalg.norm(u)
        A[k:,k:] = A[k:,k:] - u @ (2 * u.T @ A[k:,k:])
        H_k = np.eye(m-k) - 2 * u @ u.T
        Q[k:,:] = H_k @ Q[k:,:]
    return Q.T, A
