# this problem teaches you two functions split join and how to use them 
def split_and_join(line):
    line =  line.split(' ')
    line = '-'.join(line)
    return line 
    
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)