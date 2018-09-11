import numpy as np

a = np.arange(0,120).reshape(5, 4, 3, 2)
b = a.reshape(5, 4*3*2)

c = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 45, 3, 4, 45, 6, 7, 8, 9]])
c_ = np.array([3])
d = np.arange(9).reshape(3, 3)
f = np.arange(120).reshape(2, 3, 4, 5)
g = np.array([1, 2])
g = g[np.newaxis, :, np.newaxis, np.newaxis]

N, C, H, W = f.shape
print('f :\n', f)
print('f.shape :\n', f.shape)
print('f[:,0,:,:] :\n', f[:,0,:,:])
print('f.transpose(0,2,3,1).reshape(N*H*W, C) :\n', f.transpose(0,2,3,1).reshape(N*H*W, C))