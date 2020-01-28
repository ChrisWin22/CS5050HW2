###########################
from random import random, randint

N = 7
K = 100

def maxValue(n, k1, k2):
    if k1 < 0:
        return 0
    if k2 < 0:
        return 0
    if n == None:
        return V[n]
    return max(maxValue(n-1, k1-S[n], k2) + V[n], maxValue(n-1, k1, k2-S[n]) + V[n], maxValue(n-1, k1, k2))

S=[None,6,8,10,7,13,4]
V=[None, 1,2,1,3,21,2]

print(maxValue(6,20,15))

       
        
        

def knapsackBool(i, size):
    # if the bag is exactly full, return success
    if size == 0:
        return True
    #ifbag is overfull, return falure
    if size < 0:
        return False
    #if you run out of items, return falure
    if i == 0:
        return False
    return knapsackBool(i-1, size) or knapsackBool(i-1, size - S[i])
    
for _ in range(0,100):
    S = [randint(1,K/2) for _ in range(0,N + 1)]
    #if knapsackBool(N, K):
    print("Solution exists")
    #else:
    print("Solution does not exist")
        
    
    
N = 5
K = 10
S = [None, 11,12,23,435,44,4,20]
#print(knapsackBool(N, K))
        

