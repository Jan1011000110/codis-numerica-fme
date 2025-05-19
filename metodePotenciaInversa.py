import numpy as np
from scipy.linalg import lu_factor, solve_triangular
    
def pivot_to_permutation(piv):
    perm = np.arange(len(piv))
    for i in range(len(piv)):
        perm[i], perm[piv[i]] = perm[piv[i]], perm[i]
    return perm

def metode_potencia_inversa(A, z, tol=1.e-10, maxIter=100):
    M, piv = lu_factor(A)
    p = pivot_to_permutation(piv)
    sigma = np.conjugate(z)@A@z

    for i in range(1, maxIter+1):
        y = solve_triangular(M, z[p], lower=True, unit_diagonal=True)
        nz = solve_triangular(M, y, lower=False)
        nz = nz/np.linalg.norm(nz)

        nsigma = np.conjugate(nz)@A@nz
        dif = np.abs(nsigma - sigma)
        z, sigma = nz, nsigma

        if dif < tol:
            return sigma, z, i

    return sigma, z, -maxIter
