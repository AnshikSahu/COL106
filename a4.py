import random
import math

#To generate random prime less than N
def randPrime(N):
	primes = []
	for q in range(2,N+1):
		if(isPrime(q)):
			primes.append(q)
	return primes[random.randint(0,len(primes)-1)]

# To check if a number is prime
def isPrime(q):
	if(q > 1):
		for i in range(2, int(math.sqrt(q)) + 1):
			if (q % i == 0):
				return False
		return True
	else:
		return False

#pattern matching
def randPatternMatch(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatch(q,p,x)
# Time complexity=O((m+n)*log2(m/e))
# Space complexity=O(k+log(n)+log(m/e))

#pattern matching with wildcard
def randPatternMatchWildcard(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatchWildcard(q,p,x)
# Time complexity=O((m+n)*log2(m/e))
# Space complexity=O(k+log(n)+log(m/e))

def binary_search(low,high,value,error):
    while(low<high-1):# total iterations=floor(log(high-low))
        mid=low+high//2 # time=O(log(high)) space=O(log(high))
        x=mid/(math.log(mid)) # time=O(log(high)) space=O(log(high))
        if(math.abs(value-x)<=error): return mid # time=O(log(high))
        elif(x<value): high=mid# time=O(log(high))
        else: low=mid# time=O(log(high))
    return low
# Time complexity=O((log2(high))^2)
# Space complexity=O(log(high))
    
# return appropriate N that satisfies the error bounds
def findN(eps,m):

    low=2*m/eps*math.log2(26)# time=O(log(m/e)) space=O(log(m/e))
    high=low*low*eps # time=O(log(m/e)) space=O(log(m/e))
    return high # time=O(1)
#Time complexity=O((log2(m/e)))
# Space complexity=O(log(m/e))
# use this for better approximation
"""
    return binary_search(low, high, low, 1) # time=O((log(m/e))^2) space=O(log(m/e))
# Time complexity=O((log2(m/e))^2)
# Space complexity=O(log(m/e))"""

# Explaination for the value of N
# let x be the hash value of our pattern which matches with the hash value y
# thus abs(y-x) must be divisible by q
# as q is prime the probablity of this is (number of prime factors of abs(y-x))/(total primes less than N)
# as the max value of (y-x) is 26^m
# log2(26^m)/(N/(2log2(N))) < e
# N/log2(N)>2*log2(26)*m/e


# Return sorted list of starting indices where p matches x
def modPatternMatch(q,p,x):
    n=len(x) # time=O(1) space=O(log(n))
    m=len(p) # time=O(log(q)) space=O(log(m))
    ans=[]  #  space=O(k)
    factor=1 #  space=O(log(q))
    constant=26%q # space=O(log(q))
    remainder=0 # space=O(log(q))
    match=0 # space=O(log(q))
    if(n>=m): # time=O(log(q))
        for i in range(m-1,-1,-1):# total iterations=m
            remainder=(remainder+((ord(x[i])-65)%q)*factor)%q # time=O(log(q))
            match=(match+((ord(p[i])-65)%q)*factor)%q # time=O(log(q)) 
            factor=(factor*constant)%q # time=O(log(q)) 
        for i in range(0,n-m):# total iterations=n-m
            if(match==remainder): ans.append(i) # time=O(log(q)) 
            remainder=((remainder*constant)%q+(ord(x[i+m])-65)%q-(((ord(x[i])-65)%q)*factor)%q)%q # time=O(log(q)) 
            if(remainder<0): remainder+=q # time=O(log(q)) 
        if(match==remainder): ans.append(n-m) # time=O(log(q))
    return ans # time=O(1)
# Time complexity=O((n+1)*log2(q))
# Space complexity=O(k+log(n)+log(q))

# Return sorted list of starting indices where p matches x
def modPatternMatchWildcard(q,p,x):
    n=len(x) # time=O(1) space=O(log(n))
    m=len(p) # time=O(1) space=O(log(n))
    ans=[]  #  space=O(k)
    factor=1  #  space=O(log(q))
    constant=26%q  # space=O(1)
    remainder=0  #  space=O(log(q))
    match=0  #  tspace=O(log(q))
    wild=1;  #   space=O(k)
    if(n>=m): # time=O(log(q))
        k=p.index("?") #  time=O(m) space=O(log(k))
        for i in range(0,m-k-1):# total iterations=m-k
            wild=(wild*constant)%q# time=O(log(q))
        for i in range(m-1,-1,-1):# total iterations=m
            remainder=(remainder+((ord(x[i])-65)%q)*factor)%q # time=O(log(q))
            match=(match+((ord(p[i])-65)%q)*factor)%q # time=O(log(q))
            factor=(factor*constant)%q # time=O(log(q))
        match=match-(wild*((ord(p[k])-65)%q))%q if match-(wild*((ord(p[k])-65)%q))%q >=0 else match-(wild*((ord(p[k])-65)%q))%q+q# time=O(log(q))
        for i in range(0,n-m):# total iterations=n-m
            remainder_=remainder-(wild*((ord(x[i+k])-65)%q))%q if remainder-(wild*((ord(x[i+k])-65)%q))%q >=0 else remainder-(wild*((ord(x[i+k])-65)%q))%q+q# time=O(log(q))
            if(match==remainder_): ans.append(i)# time=O(log(q))
            remainder=((remainder*constant)%q+(ord(x[i+m])-65)%q-(((ord(x[i])-65)%q)*factor)%q)%q # time=O(log(q))
            if(remainder<0): remainder+=q # time=O(log(q))
        remainder_=remainder-(wild*((ord(x[n-m+k])-65)%q))%q if remainder-(wild*((ord(x[n-m+k])-65)%q))%q >=0 else remainder-(wild*((ord(x[n-m+k])-65)%q))%q+q# time=O(log(q))
        if(match==remainder_): ans.append(n-m)# time=O(log(q))
    return ans # time=O(1)
# Time complexity=O((m+n)log2(q))
# Space complexity=O(k+ logn+log(q))