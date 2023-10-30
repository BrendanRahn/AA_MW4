"""
CS 137 - Algorithm Analysis - Homework Assignment 5: 
Floyd-Warhsall algorithm for shortest paths, and Held-Karp algorithm for Traveling Salesperson Problem


In this homework assignment, you will 
1. Use Floyd's algorithm to solve a problem by hand.
2. Use the Held-Karp algorithm to solve an instance of the Traveling Salesperson Problem by hand.
3. Implement the Held-Karp algorithm to solve the Traveling Salesperson Problem.


TODO: Fill in the #TODO spaces with working code, and write additional tests to check your code for correctness.

#IMPORTANT: In total, this homework requires you to upload three files to codepost: Floyd_table.JPEG, TSP_soln.py, and TSP_table.JPEG.
Make sure you have uploaded all three.

"""

import itertools
from itertools import combinations, chain
import sys #for sys.maxint - representing a maximum integer size in Python


"""
Problem 1: Using Floyd's algorithm (p.108 of Neapolitan), solve problem 5 at the end of Neapolitan Chapter 3.
This problem is on pages 146-147. 

Upload your solution containing the final matrix D^k with the filename Floyd_table.JPEG to codepost,
along with your TSP_soln.py file.

"""


"""
Problem 2: Using the Held-Karp algorithm pseudocode, find an optimal tour of the following graph
by filling out a table D of values like those on p.133 of Neapolitan.

You may prefer to first draw the graph (given by the following adjacency matrix):

              v0   v1   v2   v3
         v0   0    10   15   20
         v1   10   0    35   25
         v2   15   35   0    30
         v3   20   25   30   0

Upload an image of the table you filled out to codepost along with your TSP_soln.py file
Make sure it is named TSP_table.JPEG

"""


"""
Problem 3 (main): Implementation of the Held-Karp algorthm 
(A note - you may NOT implement the naive version. The solution must use dynamic programming.)

See p.134 Neapolitan /Foundations of Algorithms/ 8th Ed. 
"""
"""
Your tasks: 
1. Understand the parts of the code that are available. You may modify these, but the end result cannot be the 
naive algorithm - it MUST be Held-Karp. 
2. Fill in the sections marked #TODO to get this code working. Refer to Neapolitan p.134 for the algorithm.
3. Write test cases that demonstrate (to you) that the code works on a variety of situations.
4. Comment out those test cases before you submit. I will not grade submissions that fail to do this.
Moreover, submissions that call the travel(...) method may take up more time than codepost allows for tests.
Include the travel(...) method but do not call it, in your submission.
"""
def travel(n, G):
    D  = [{} for x in range(n)] #each vertex has a dictionary of subsets
    P = [{} for x in range(n)] #each vertex has a dictionary of subsets
    #Tip: Use the frozenset type - dictionaries/sets are not
    # hashable, so you will get an error if you try to index with them. 
    # Instead, we can make a mutable version of the set/dict type using the frozenset type.

    # Book starts with index 1. We use index 0. So, ranges are adjusted accordingly. 
    for i in range(1,n,1):
        D[i][frozenset({})] = G[i][1]

    for k in range(1,n-1,1):
        size_k_subsets = generate_subsets(set(range(1,n,1)), k )
        for A in size_k_subsets:
            X = frozenset(range(1, len(G))) - A
            #TODO # X contains the vertices that are not v0 and aren't in A
            for i in X:
                #We define an inline function dist_via so that we can use it as the sorting key.
                #This just happens to be the least silly way to do this in Python. REmember, 
                #we also need to obtain the actual vertex j itself. So using min (...) on the set of distances
                #won't do that. 
                #Why define this inline instead of outside travel? Because it refers to i, which is an internal
                #variable.
                def dist_via(u):
                    if frozenset(A - {u}) in D[u]:
                        return G[i][u] + D[u][frozenset(A - {u})]
                    else: 
                        return sys.maxsize
                
                #The list of things in X sorted by that criterion. See documentation for sorted(...).
                sorted_by  = sorted(list(A), key = dist_via)

                #TODO: Implement this part

    #Same idea as the loop above, except ONLY with the first vertex
    def dist_via_fin(u):
        #TODO
    sorted_by  = sorted(list(range(1,n,1)),key = dist_via_fin)
    j = P[0][frozenset(set(range(n))-{0})] = sorted_by[0] 
    min_length = D[0][frozenset(set(range(n))-{0})] = G[0][j] + D[j][frozenset(set(range(n)) - {0,j})]
    tour = get_opt_tour(P,j) #Retrieve the tour itself
    return min_length , tour

""" Retrieve the optimal tour from P: work backwards through P. 
Note this relies on us knowing the last j value at the end of the main algorithm above."""
#Requirements:
#1. Make sure the tour goes in the forward order, not reverse
#2. Make sure the tour both starts and ends with 0
#3. See below for sample output
#4. Feel free to rewrite as you see fit, as long as the input and output convention stays the same.
def get_opt_tour(P,j):
    tour = [0]
    A = frozenset(range(1,len(P)))
    #TODO
    return tour




#Tip: How to generate all subsets: 
# https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset

#Tip: How to get all subsets of a particular size
# https://www.geeksforgeeks.org/python-program-to-get-all-subsets-of-given-size-of-a-set/

""" See itertools import in file header"""
""" Generate all the size k subsets of Y """
def generate_subsets(Y, k):
    return list(map(set, itertools.combinations(Y, k)))


dist = [[0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]]


min_cost, opt_tour = travel(len(dist), dist)
print("Optimal tour length:", min_cost)
print("Optimal tour:", opt_tour)

#prints 
# Optimal tour length: 80
# Optimal tour: [0, 1, 3, 2, 0]