# this problem teaches you how to access the elements of a nested list
# and how to sort the list 
# a new thing that i learned is that you can write a line of code that sorts the nested list for example
# by the second element sort by nested_list[0][1] 
# list.sort(key = lambda x: x[1]) this is what we call a higher order function because we can pass
# a function as an argument 
# tools 
def sort_students(names_scores):
    scores = []
    for student in names_scores:
        scores.append(student[1])
    sorted_scores = sorted(set(scores))
    second_lowest = sorted_scores[1]
    
    names_second_lowest = []
    for student in names_scores:
        if student[1] == second_lowest:
           names_second_lowest.append(student[0])
    
    for name in sorted(names_second_lowest):
        print(name)
        
        
#execution 
names_scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    names_scores.append([name, score])

#use your tools  
sort_students(names_scores)
