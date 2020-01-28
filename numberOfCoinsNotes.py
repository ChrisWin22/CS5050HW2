def miinCoins(change):
	if change == 0:
		return 0
	if change < 0:
		return 1000000000
	return min(minCoins(change - 1),
                    minCoins(change - 7),
                    minCoins(change - 13),
                    minCoins(change - 26)) + 1



#META Algorithm
#Define the problem as a function f(<problem>)
#Identify simple problem
#Write as function calls
#Compute my solution from someone elses solution
#Clean up edge cases

#Test Speed
#develop f() calculates speed (aka number of calls)
#   f(0) = 1
#   f(n) = f(n -1) + f(n-7) + f(n-13) + f(n-26)
#   Worst case
#       f(n) = f(n-1) 
#            = 4 * 4(f(n-2))
#            = 4^n

#Count number of unique calls
#Review the problem description
#input to the function


#dynamic programming computes smallest to biggest
s = np.array(n+1)
s[0] = 0
for i in range (1, n+1):
    s[i] = ! + min(s[i - 1], s[i - 7], s[i - 13], s[i - 26])
return s[n]
    
#Knapsack problem
#Given a knapsack of size n
#Given a set of objects each of size 'size[i]'
#M objects
#find -is there a subset of objects that exactly fits in the sack?
#only use objects once
n = 13
size = {3,5,15,23}

def bool knap(n, m):
    if n == 0:
        return True
    if m == 0:
        return False
    #Two choices, put in or throw away
    #throw away = knap(n , m-1)
    #put in = knap(n-size[m], m-1)
        
        

