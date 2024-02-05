n = int(input())
integer_list = map(int, input().split())
integer_tuple = tuple(integer_list)
print(hash(integer_tuple))

# an issue that happend to me while trying to solve the this problem is that my code is correct (semantics and syntax) but 
# each time i try to submit the code it fails ans the solution was basically to change the "language" from python 3 to Pypy 3 and that's it 