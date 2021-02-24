# Program to multiply two matrices using nested loops
import random
import numpy as np

N = 250
import numpy as np

N = 250

X = np.random.uniform(0, 100, (N, N))
    
Y = np.random.uniform(0, 100, (N,N+1))

R = np.matmul(X, Y)

print(R)