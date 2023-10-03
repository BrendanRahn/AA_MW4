
"""
CS 137 - Algorithm Analysis - Homework Assignment 5: Dynamic Programming



In this homework assignment, you will implement the merge sort and quicksort methods in Python,
and answer some questions about these algorithms in the comments.


TODO: Fill in the #TODO spaces with working code, and write additional tests to check your code for correctness.
TODO: Answer questions 1-3 at the bottom of this file. Put your answers in this file as well, below the question statements.

#IMPORTANT: Comment out ALL print statements before submitting to codePost
#IMPORTANT: Do NOT change the names of the methods, or codePost tests will fail and you will
# lose ALL points!!
#IMPORTANT: Make sure the file you submit is named sorting_soln.py.
"""


####################
#PROBLEM 1: MERGE SORT#

#Merges two lists
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        #TODO
    #TODO
    return result

#The merge sort algorithm
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = #TODO
    right = #TODO
    return #TODO



#A test - you should write more of these (but comment all of these out when you submit).
sorted = merge_sort([5, 2, 9, 1, 5, 6, 3])
print(sorted == [1,2,3,5,5,6,9])

####################
#PROBLEM 2: QUICK SORT#

#Returns an integer representing the partition location in arr.
def partition(arr, low, high):
    #TODO
    return TODO

#The quicksort algorithm
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)
    return arr

#A test - you should write more of these (but comment all of these out when you submit).
arr = [5, 2, 9, 1, 5, 6, 3]
sorted = quicksort([5, 2, 9, 1, 5, 6, 3], 0, len(arr)-1)
print(sorted == [1,2,3,5,5,6,9])



#############################################

"""
Question 1. You are tasked with sorting a large dataset that happens to be almost completely sorted, 
but has about five percent of its catalog out of order. Which sorting algorithm should you use? 
Explain why.


"""

"""
Question 2:  Suppose you work in a large library with thousands of books, each with a unique identifier. 
You need to sort the catalog of books based on their identifier. 
You decide to use quicksort to sort the catalog because it is a fast algorithm that can handle large amounts
of data. If the catalog has 10,000 books, how many comparisons (determine the exact number) will quicksort make to sort the catalog?
Assume the partition function always chooses the median of three randomly chosen elements as the pivot,
and that the data is not already sorted or mostly sorted.

The number of comparisons is ______ 
"""

"""
Question 3: Where does the log n term come from, in each of the algorithms' time complexities?


"""
