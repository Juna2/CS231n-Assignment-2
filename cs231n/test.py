import numpy as np

a = np.arange(0,120).reshape(5, 4, 3, 2)
b = a.reshape(5, 4*3*2)

c = np.array([1, 2, 3, 4, 5])
d = np.array([2, 2, 2])
f = np.array([[1, 2, 3],[4, 5, 6]])

# g = np.random.rand(1, 1000) * 100
g = np.random.normal(0, 100, (1, 1000))
g, counts = np.unique(np.floor(g), return_counts=True)

x = np.random.randn(4,5)
N = x.shape[0]
miso = 1e-8

dvar = (2/N) * (x-x.mean(axis=0))
real_dvar = np.zeros_like(x)

var1 = x.var(axis=0)
for i in range(N):
    mask = np.zeros_like(x, dtype=float)
    mask[i,:] += miso
    var2 = (x+mask).var(axis=0)
    real_dvar[i,:] = (var2-var1)/miso

print('dvar :\n', dvar)
print('real_dvar :\n', real_dvar)