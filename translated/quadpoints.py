import numpy as np
from math import floor, cos, pi

def quadpoints(n, lbnd, ubnd):
    x = np.zeros((n, 1))
    w = np.copy(x)
    EPS = 3e-14
    m = floor((n + 1) / 2)
    xm = (ubnd + lbnd) / 2
    xl = (ubnd - lbnd) / 2
    i = 1
    z1 = 1e99

    while i <= m:
        z = cos(pi * (i - 0.25) / (n + 0.5))
        while abs(z - z1) > EPS:
            p1 = 1
            p2 = 0
            j = 1
            while j <= n:
                p3, p2 = p2, p1
                p1 = ((2*j - 1) * z * p2 - (j - 1) * p3) / j
                j += 1
            pp = n * (z * p1 - p2) / (z * z - 1)
            z1 = z
            z  = z1 - p1 / pp
        x[i - 1] = xm - xl * z
        x[n - i] = xm + xl * z
        w[i - 1] = 2 * xl / ((1 - z * z) * pp * pp)
        w[n - i] = w[i - 1]
        
        i += 1

    return [x, w]