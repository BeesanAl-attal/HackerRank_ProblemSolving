#build your tools
def list_commands(N):
    lst = []
    for i in range(N):
        command, *line = input().split() # such an intersting way to handle input when a string and a list is entered in one line 
        argument = list(map(int, line))
        if (command == 'insert'):
            lst.insert(argument[0], argument[1])
        elif (command == 'print'):
            print(lst)
        elif (command == 'remove'):
            lst.remove(argument[0])
        elif (command == 'append'):
            lst.append(argument[0])
        elif (command == 'sort'):
            lst.sort()
        elif (command == 'pop'):
            lst.pop()
        elif (command == 'reverse'):
            lst.reverse()
        else:
            print("The entered command is not validm reenter")

 

#execution
if __name__ == '__main__':
    N = int(input())
    
#use your tools
list_commands(N)

# a great source to learn problem solving is 'Amir Charkhi' youtube channle and from there i learned how to divide my code to 
# 1) bulid your tools 2) execution 3) use your tools, such a game changer when trying to solve a problem, so make sure to check out his channle 
