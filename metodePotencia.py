def metode_potencia(A, z, tol=1.e-10, maxIter=100):
    sigma = np.conjugate(z)@A@z
    for i in range(1, maxIter+1):
        prod_Az = A@z
        nz = prod_Az/np.linalg.norm(prod_Az)
        nsigma = np.conjugate(nz)@A@nz
        dif = np.abs(nsigma - sigma)
        z, sigma = nz, nsigma
        if dif < tol:
            return sigma, z, i
    return sigma, z, -maxIter
