import time
import random
#selection sort is O(n**2) time complexity


def selectionSort(items):
    ''' Sort through a list using a selection sort method


        pre: items is a list of unordered integers 
        post: returns a list ordered integers'''
    
    sorted = 0                          #index of sorted elements
    n = len(items)                      #n steps          #number of elements in the list
    while sorted < (n-2):               #n - 2 number of times, still close to n
        m = findSmallest(items[sorted:])    

        #swapping the next min value with the element at the current position
        temp = items[sorted]
        items[sorted] = items[m+sorted]
        items[m+sorted] = temp

        sorted += 1     #incrementing the current index, the number of elements in the list



def findSmallest(items):
    ''' finds the smallest value in a list

        pre: items is a list of integers
        post: returns the smallest integer'''

    s = 0   #index of smallest element
    i = 0   #index/counter variable
    while i < len(items):
        if items[s] > items[i]:
            s = i
        i += 1
    return s


# Time varies by computer
def list1():                    #took about 3 seconds
    ''' finds the time it takes selection sort to go through a list of 10000 integers

        pre: no preconditions
        post: returns the time it takes in seconds'''
    
    start = time.time()
    selectionSort(list(random.randrange(1,10000000) for i in range(10001)))
    end = time.time()
    print (end - start,"seconds")
    

def list2():                #took too long
    ''' finds the time it takes selection sort to go through a list of 100000 integers

        pre: no preconditions
        post: returns the time it takes in seconds'''
    start = time.time()
    selectionSort(list(random.randrange(1,10000000) for i in range(100001)))
    end = time.time()
    print (end - start,"seconds")
    

def list3():                #didn't even try to run it
    ''' finds the time it takes selection sort to go through a list of 1000000 integers

        pre: no preconditions
        post: returns the time it takes in seconds'''
    start = time.time()
    selectionSort(list(random.randrange(1,10000000) for i in range(1000001)))
    end = time.time()
    print (end - start,"seconds")




print("Selection sort using the first ten thousand integers took: \n")
list1()

