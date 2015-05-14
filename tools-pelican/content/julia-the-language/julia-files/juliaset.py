def julia_set(z, c, maxit=2000):
    for n in range(1,maxit+1):
        if abs(z) > 4:
            return n-1
        z = z*z+c
    return maxit
