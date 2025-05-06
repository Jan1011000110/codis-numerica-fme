def metode_potencia_inversa(A, z, tol=1.e-10, maxIter=100):
    sigma = np.conjugate(z)@A@z
    for i in range(1, maxIter+1):
        nz = np.linalg.solve(A, z)
        nz = nz/np.linalg.norm(nz)
        nsigma = np.conjugate(nz)@A@nz
        dif = np.abs(nsigma - sigma)
        z, sigma = nz, nsigma
        if dif < tol:
            return sigma, z, i
    return sigma, z, -maxIter
