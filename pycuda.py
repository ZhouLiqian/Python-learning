from concurrent.futures import thread
from numba import cuda,float32
import numpy as np
import time
import math

"""矩阵相乘"""
TPB = 16
@cuda.jit
def matmul_gpu(A,B,C):
    row,col = cuda.grid(2)
    if row < C.shape[0] and col < C.shape[1]:
        tmp = 0
        for k in range(A.shape[1]):
            tmp += A[row,k]*B[k,col]
        C[row,col] = tmp

AA = np.full((TPB*50,TPB*50), 3, np.float)
BB = np.full((TPB*50,TPB*50), 4, np.float)

# 传入变量
A_global_mem = cuda.to_device(AA)
B_global_mem = cuda.to_device(BB)
C_global_mem = cuda.device_array((AA.shape[0],BB.shape[1]))
threadsperblock = (TPB,TPB)
blockspergrid_x = int(math.ceil(AA.shape[0]/threadsperblock[0]))
blockspergrid_y = int(math.ceil(BB.shape[1]/threadsperblock[1]))
blockspergrid = (blockspergrid_x,blockspergrid_y)
cuda.synchronize()
start_gpu = time.time()
matmul_gpu[blockspergrid,threadsperblock](A_global_mem, B_global_mem, C_global_mem)
cuda.synchronize()
end_gpu = time.time() - start_gpu
print(end_gpu)
# 返回
C_global_gpu = C_global_mem.copy_to_host()
print(C_global_gpu)