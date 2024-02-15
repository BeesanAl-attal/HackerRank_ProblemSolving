# here you need to use the slicing method to solve the problem

def wrap(string, max_width):
    i = 0
    while i < len(string) : # or for i in range(0, len(string), max_width) then remove 'i += max_width'
        sub_string = string[i: i+max_width]
        i += max_width # to skip the sub string that you just print it and go to the beginning of the 'next' sub string
        if len(sub_string) == max_width:
            print(sub_string)
        else:
            return sub_string 
        
        

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# note 
# Problem Solving websites add some restrictions to the way you implement your code