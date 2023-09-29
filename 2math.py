from math import *
import numpy as np

print('[',end='')
for i in np.arange(-50, 50, 0.05):
    print('(', i, ',' , floor(i + i * floor(i)), '),', end='')
print(']')
