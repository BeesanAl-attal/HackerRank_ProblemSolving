# Drawing, graphing (what ever you wanna call it), is fun and good way to improve your programming skills 
# This problem here teaches you the functions (ljust(), center(), rjust()) to graph your desired pattern  
# also one of the most important things you need to know, a complicated looking graph is just a 'combination' of simple shapes 
# so what you need to do is to divide the shape to partitions "simple shapes" then start writing your code
# I would recommend to use the (try and fail method) till you get the write shape 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))