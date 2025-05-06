import numpy as np
def metode_potencia(A, z, tol=1.e-10, maxIter=100):
    sigma = z.T@A@z
    for i in range(1, maxIter+1):
        prod_Az = A@z
        nz = prod_Az/np.linalg.norm(prod_Az)
        nsigma = nz.T@A@nz
        dif = np.abs(nsigma - sigma)
        z, sigma = nz, nsigma
        if dif < tol:
            print(z,sigma)
            return sigma, z/(sigma**i), i
    return -maxIter
