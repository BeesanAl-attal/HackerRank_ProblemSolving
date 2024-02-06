# Loved this problem, although it is ranked "easy", but it taught me a lot 
# first what is the meaning of "Runner-Up Score" --> the competitor that does not win first place in a contest
# when we are dealing with 'ranking' highest, lowest, second highest and so on the first thing that comes up to your mind is sorting your list 
# then printing the value by accessing the element via the index operator [], but you should keep in mind that we might have some duplicates and
# to solve the issue we convert our list to a set then the list to a set, so you can use the list methods but on unique values(elements) only 
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    A =  list(arr)
    s = set(A)
    unique_scores = list(s)
    unique_scores.remove(max(unique_scores))
    print(max(unique_scores))

# i think we can use the n value to restrict the users number of entered integers if you want to make this code better 

