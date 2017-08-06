import collections
import math
# O(logn) time O(1) space
def dtob(n):
    re=collections.deque()
    while n!=0:
        re.appendleft(n%2)
        n=int(n/2)
    print(list(re))


def dtobTest():
    n=7
    dtob(n)

# O(sqrtn) time O(1) space
def validPrime(n):
    if n<=1:
        return False
    root=int(math.sqrt(n))
    for i in range(2,root+1):
        if n%i==0:
            return False
    return True

def validPrimeTest():
    for i in range(-1,21):
        print("{} - {}".format(i,validPrime(i)))

# sieve of Eratosthenes
# O(nloglogn) time O(1) space
def allPrime(n):
    if n<=1: return []
    root=int(math.sqrt(n))
    prime=[1 for i in range(0,n+1)]
    prime[0]=0
    prime[1]=0
    for i in range(2,root+1):
        j=i
        while i*j<=n:
            prime[i*j]=0
            j+=1
    for i in range(0,n+1):
        if prime[i]==1: print(i)

def allPrimeTest():
    n=20
    allPrime(n)

# O(sqrt(n)) time O(1) space
def allFactors(n):
    root=int(math.sqrt(n))
    s=[]
    l=collections.deque()
    for i in range(1,root+1):
        if n%i==0:
            s.append(i)
            if i!=n/i:
                l.appendleft(n//i)
    s=s+list(l)
    print(s)
    return s

def allFactorTest():
    for i in range(1,11):
        print("{} {}".format(i,allFactors(i)))

# O(sqrtn) time O(1) space
def primeFactorization(n):
    print("-"*20)
    i=2
    while i<=int(math.sqrt(n)):
        count=0
        while n%i==0:
            n/=i
            count+=1
        if count>0:
            print("{}-{}".format(i,count))
        i+=1
    print("{}-1".format(int(n)))


def primeFactorizationTest():
    for n in range(2,23):
        primeFactorization(n)

# O(log(ab)) time
def euclidGCD(a,b):
    while b!=0:
        temp=b
        b=a % b
        a=temp
    return a

def euclidGCDTest():
    a=5
    b=45
    re=euclidGCD(a,b)
    print(re)

def LCM(a,b):
    lcm=int(a*b/euclidGCD(a,b))
    print(lcm)

def LCMTest():
    a=5*9*2
    b=45
    LCM(a,b)

if __name__ == '__main__':
    # dtobTest()
    # validPrimeTest()
    # allPrimeTest()
    # allFactorTest()
    primeFactorizationTest()
    # euclidGCDTest()
    # LCMTest()