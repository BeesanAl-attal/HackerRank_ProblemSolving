# Drawing, graphing (what ever you wanna call it), is fun and good way to improve your programming skills 
# This problem here teaches you the functions (ljust(), center(), rjust()) to graph your desired pattern  
# also one of the most important things you need to know, a complicated looking graph is just a 'combination' of simple shapes 
# so what you need to do is to divide the shape to partitions "simple shapes" then start writing your code
# I would recommend to use the (try and fail method) till you get the write shape 

N, M = map(int, input().split())
for i in range(1, N, 2):
    print(('.|.' * i).center(M, '-'))
    # Center
print('WELCOME'.center(M, '-'))
    # bottom 
for i in range((N - 2), -1, -2):
    print(('.|.' * i).center(M, '-'))