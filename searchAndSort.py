import random
import unittest
import sys


def binarySearchI(A, key):
    left,right=0,len(A)-1
    while left<=right:
        mid=int((left+right)/2)
        if key==A[mid]: return mid
        elif key>A[mid]: left=mid+1
        else: right=mid-1
    return -1

def binarySearchR(A, left, right, key):
    if right>left: return -1
    mid=int((left+right)/2)
    if key==A[mid]: return mid
    elif key>A[mid]: return binarySearchR(A, mid + 1, right, key)
    else: return binarySearchR(A, 0, mid, key)

def linearSearch(A,key):
    for i in range(0,len(A)):
        if A[i]==key: return i
    return -1

def insertionSort(A):
    m=len(A)
    for i in range(1,m):
        temp=A[i]
        j=i-1
        while j>=0 and A[j]>temp:
            A[j+1]=A[j]
            j-=1
        A[j+1]=temp
def merge(left,right):
    left+=[sys.maxsize]
    right+=[sys.maxsize]
    result=[]
    i,j=0,0
    while i<len(left)-1 or j<len(right)-1:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    return result

def mergeSort(A):
    if len(A)<=1: return A
    mid=int(len(A)/2)
    left=mergeSort(A[0:mid])
    right=mergeSort(A[mid:])
    return merge(left,right)
def swap(A,a,b):
    temp=A[a]
    A[a]=A[b]
    A[b]=temp


def randomPartition(A,l,h):
    rand=random.randint(l,h)
    swap(A,rand,h)
    return partition(A,l,h)
def partition(A,l,h):
    key=A[h]
    i=l
    while l<=h-1:
        if A[l]<=key:
            swap(A,i,l)
            i+=1
        l+=1
    swap(A,i,h)
    return i
def quickSort(A,l,h):
    if l<h:
        pivot=randomPartition(A,l,h)
        quickSort(A,l,pivot-1)
        quickSort(A,pivot+1,h)

def quickSortTest():
    A=[6,2,3,4,2,4,5,5,3,4,3]
    quickSort(A,0,len(A)-1)
    print(A)

def countSort(A):
    myMax=max(A)
    C=[0 for i in range(0,myMax+1)]
    for n in A:
        C[n]+=1
    for i in range(1,len(C)):
        C[i]+=C[i-1]
    for i in range(0,len(C)):
        C[i]-=1
    B=A
    for n in A[::-1]:
        B[C[n]]=n
        C[n]-=1
    return B
def countSort(A,exp):
    C=[0 for i in range(0,10)]
    for n in A:
        digit=n//exp%10
        C[digit]+=1
    for i in range(1,len(C)):
        C[i]+=C[i-1]
    for i in range(0,len(C)):
        C[i]-=1
    B=A
    for n in A[::-1]:
        digit=n//exp%10
        B[C[digit]]=n
        C[digit]-=1
    return B
def radixSort(A):
    myMax=max(A)
    exp=1
    while myMax/exp>0:
        countSort(A,exp)
        exp*=10
    return A


def radixSortTest():
    A=[104,113,122]
    return radixSort(A)



def is_prime(number):
    """Return True if *number* is prime."""
    if number<=1: return False
    for element in range(2,number):
        if number % element == 0:
            return False

    return True

def print_next_prime(number):
    """Print the closest prime number larger than *number*."""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)
class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))
    def test_is_zero_not_prime(self):
        """Is zero correctly determined not to be prime?"""
        self.assertFalse(is_prime(0))
    def test_insertion_sort(self):
        """Is a negative number correctly determined not to be prime?"""
        for i in range(0,10):
            size=random.randint(0,20)
            A=[]
            for i in range(0,size+1):
                num=random.randint(0,20)
                A.append(num)
            B=A[:]
            insertionSort(A)
            B.sort()
            self.assertEqual(A,B)
    def test_merge_sort(self):
        """Is a negative number correctly determined not to be prime?"""
        for i in range(0,10):
            size=random.randint(0,20)
            A=[]
            for i in range(0,size+1):
                num=random.randint(0,20)
                A.append(num)
            B=A[:]
            B.sort()
            self.assertEqual(mergeSort(A),B)
    def test_quick_sort(self):
        """Is a negative number correctly determined not to be prime?"""
        for i in range(0,10):
            size=random.randint(0,20)
            A=[]
            for i in range(0,size+1):
                num=random.randint(0,20000)
                A.append(num)
            B=A[:]
            radixSort(A)
            B.sort()
            self.assertEqual(A,B)
    def test_binary_search(self):
        for i in range(0,10):
            size=random.randint(1,20)
            max=100
            A=[]
            mySet=set()
            for i in range(0,size):
                num=random.randint(0,max)
                while num in mySet:
                    num=random.randint(0,max)
                mySet.add(num)
                A.append(num)
            A.sort()
            #print("sorted: {}".format(str(A)))
            #i=random.randint(0,size-1)
            #key=A[i]
            key=sys.maxsize
            self.assertEqual(binarySearchR(A, 0, len(A), key), binarySearchI(A, key))
if __name__ == '__main__':
    unittest.main()