# the point of this problem is to learn how to write a list comprehesion instead of loops if you are dealing with lists
# so lets see how to do that and check the difference 

# normal for loop to create a new list which contain the first name and the last name 
name_list = ['Ali', 'Sara', 'Omar']
new_name_list = []
for name in name_list:
    name += ' Alomari'
    new_name_list.append(name)

print(new_name_list)
#------------------------------------#
#using a list comprehension 
# the structure 
# var_name = [desiredOutput/opperation for loop]
new_name_list = [name + ' Alomari' for name in name_list]
print(new_name_list) # and voila 

# another Example 
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
new_num_list = []

for num in num_list : 
    new_num_list.append(num * 11)

print(new_num_list)

# using list coprehension 
new_num_list = [num * 11 for num in num_list]
print(new_num_list) # and voila 

# Solve the actual problem 
# first let's break it down
# first you are given four values x, y, z, n
# print all the possible coordinates (الإحداثيات) given by (i, j, k) in a 3d grid 
# where the sum of i + j + k != n
# here it is like we are trying to figure out all the possible permutations of (i,j,k)
# x, y, z represetent the corrdinates 
# where 0 <= i <= x and so one for the other values 

# using a for loop 
x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
             print(i, j, k)

# this nested loop will print all the possible permutations of j, i, k\

# using comprehension list 
def permutation_3dgridlist(x, y, z, n):
    perm_list = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(perm_list)

# test
permutation_3dgridlist(x, y, z, n)








