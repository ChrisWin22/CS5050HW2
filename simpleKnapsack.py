###########################
from random import random, randint
import time
import numpy as np
import matplotlib.pyplot as plt

def DPMaxValue(N, K1, K2):
    if K1 < 0 or K2 < 0:
        return -1000000000000
    if cache[N, K1, K2] != None:
        return cache[N, K1, K2]
    if N == 0:
        cache[N, K1, K2] = 0
        return 0
    cache[N, K1, K2] = max(DPMaxValue(N-1, K1-S[N], K2) + V[N], DPMaxValue(N-1, K1, K2-S[N]) + V[N], DPMaxValue(N-1, K1, K2))
    return cache[N, K1, K2]


def timeDPFunction(N, K1, K2):
    start = time.time()
    for i in range(0, N + 1):
        DPMaxValue(i, K1, K2)
        #print(cache)
    return time.time() - start

def memoiMaxValue(n, k1, k2):
    if k1 < 0 or k2 < 0:
        return -1000000000000
    if n == 0:
        return 0
    key = str(n) + str(k1) + str(k2)
    if key in dictionary:
        return dictionary[key]
    dictionary[key] = max(memoiMaxValue(n-1, k1-S[n], k2) + V[n], memoiMaxValue(n-1, k1, k2-S[n]) + V[n], memoiMaxValue(n-1, k1, k2))
    return dictionary[key]

def timeMemFunction(n, k1, k2):
    start = time.time()
    memoiMaxValue(n,k1,k2)
    return time.time() - start

def generator(N, aveSize):
    S = []
    V = []
    S.append(None)
    V.append(None)
    for _ in range(0, N):
        S.append(randint(1, 2*aveSize))
        V.append(random() * 20)
    return S, V



def maxValue(n, k1, k2):
    if k1 < 0 or k2 < 0:
        return -1000000000000
    if n == 0:
        return 0
    return max(maxValue(n-1, k1-S[n], k2) + V[n], maxValue(n-1, k1, k2-S[n]) + V[n], maxValue(n-1, k1, k2))      
        

def timeFunction(N, K1, K2):
    start = time.time()
    print(maxValue(N, K1, K2))
    return time.time() - start

N = 300
K1 = 60
K2 = 37

aveSizeArray = []
memTimes = []
dpTimes = []

for i in range(0,10):
    aveSize = randint(1, 2*N)
    aveSizeArray.append(aveSize)
    S, V = generator(N, aveSize)
    #print(timeFunction(N, K1, K2))
    memTimes.append(0)
    dpTimes.append(0)
    for _ in range(0,20):
        #Memoiziung
        dictionary = dict()
        memTimes[i] = memTimes[i] + timeMemFunction(N, K1, K2)
        dictionary.clear()
        #DP
        cache = np.full((N + 1, K1 + 1, K2 + 1), None)
        dpTimes[i] = dpTimes[i] + timeDPFunction(N, K1, K2)
    memTimes[i] = memTimes[i]/20
    dpTimes[i] = dpTimes[i]/20

plt.plot(aveSizeArray, memTimes, color='blue', label = "Memoized")
plt.plot(aveSizeArray, dpTimes, color='red', label = "Dynamic")
plt.xlabel('aveSize')
plt.ylabel('Run Time (seconds)')
plt.title("Memoized vs Dynamic Run Times")
plt.legend()
plt.show()




















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
    
#for _ in range(0,100):
 #   S = [randint(1,K/2) for _ in range(0,N + 1)]
    #if knapsackBool(N, K):
  #  print("Solution exists")
    #else:
  #  print("Solution does not exist")
        
    
    
N = 5
K = 10
S = [None, 11,12,23,435,44,4,20]
#print(knapsackBool(N, K))
        

