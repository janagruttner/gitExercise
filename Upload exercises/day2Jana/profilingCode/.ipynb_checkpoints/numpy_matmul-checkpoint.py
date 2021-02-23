# Program to multiply two matrices using nested loops
import random
import numpy as np

N = 250
def multiplyMNP(N):
    
    X = np.random.uniform(0, 100, (N, N))
    
    Y = np.random.uniform(0, 100, (N,N+1))

    R = np.matmul(X, Y)
    
    return(R)

r = multiplyMNP(N)
print(r)