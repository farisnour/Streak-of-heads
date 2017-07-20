import math

def flipCoins(n,k):
    
    p = [0 for i in range(k+1)]
    p[0] = 1 #p[0] = math.pow(2,n)
    q = [0 for i in range(k+1)]
    #print(p)
    
    for i in range(0,n):
        for j in range(0,k):
            q[0] += p[j]/2
            q[j+1] += p[j]/2
        q[k] += p[k]
        for j in range(0,k+1):
            p[j] = q[j]
        q = [0 for l in range(k+1)]
        #print(p, "FLIP ", i+1)
        
    print("Probability of a streak of at least", k, "heads in", n, "flips:", p[k])
