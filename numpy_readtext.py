import numpy as np
from numpy import loadtxt

fname = "demo.txt"

data = np.array([[1,2,3],[4,5,6],[7,6,9]],np.int32)
np.savetxt(fname,data)
# data_stored = loadtxt(fname).astype(np.float16)
# print(data_stored)