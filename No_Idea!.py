# Things to note in this problem
# two disjoint sets --> a pair of sets that does not have any common elements between them 

# based of the input format 
# 1. The first kine contains integers n and m sperated by a space
n, m = map(int, input().split()) # note : n, m = ...: This is a technique called tuple unpacking in Python. It assigns the first element of the list to the variable n and the second element to the variable m. This assumes that the user entered two values separated by spaces.
# we also add the .split function that splits the values by default at whitespace so we will have two values to unpack not one 

# 2. the second line contains n integers, the element of the array 
array = list(map(int, input().split()))

# the third line and fourht lines contain m integers A, and B repectively 
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(sum(((i in A) - (i in B) for i in array)))
''' 
 the input to test the solution 
 3 2
 1 5 3
 3 1 
 5 7 
'''
# in this problem we used something called the generator expression 
# which is an iterable sequence of values. It is similar in concept to a list comprehension but produces values one at a time on-the-fly rather than creating a list in memory.
# The syntax for a generator expression is similar to that of a list comprehension, with the primary difference being the use of parentheses () instead of square brackets [].
