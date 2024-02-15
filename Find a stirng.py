
def count_substring(string, sub_string):
    start = 0 # pointer one 
    end = len(sub_string) # pointer two 
    # the start and end variables are like two pointers that move together to find the substring  and these two pointers 
    counter = 0 # to count the substring 
    # when searching for a substring in a string  you need to consider the length of
    # the substring , because  we need to compare between to substrings to start counting 
    while end <= len(string):
        # here we need to use slicing one of the most important methods for strings
        if sub_string == string[start:end]:
            counter += 1
        start += 1
        end += 1
    return counter
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# general notes 
# an important thing when you come up with the solution of your problem, it should be implementable, what i mean
# you should have a step by step solution so the complier can actually implement your solution 
# what i am trying to say, is that when solving a problem via codding you need to change your mindset its not like normal problem solving skill 
# you should now how your compiler reads, interprets and compile your code 