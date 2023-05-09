import numpy as np
N_ITERATIONS = 200
RES = 2000
x = np.linspace(-2, 2, RES)
y = np.linspace(-2, 2, RES)
X, Y = np.meshgrid(x, y, indexing = 'xy')
diverge, iterations = np.meshgrid(x, y, indexing = 'ij')
c = X + 1.j * Y

for i in range(RES):
    for j in range(RES):
        z = 0
        n = 0
        while abs(z) <= 100 and n < N_ITERATIONS:
            z = z**2 + c[i, j]
            n += 1
        if n == N_ITERATIONS:
            diverge[i, j] = 0
            iterations[i, j] = N_ITERATIONS
        else:
            diverge[i, j] = 1
            iterations[i, j] = n