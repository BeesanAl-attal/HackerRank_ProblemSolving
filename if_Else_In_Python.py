# this problem is straight forward no explanation needed
# the aim of this problem is to teach you how to use the if - else in python 
if __name__ == '__main__':
    n = int(input().strip())
if (n % 2 == 0):
    if n in range(2, 6):
        print("Not Weird")
    elif(n in range(6, 21)):
        print("Weird")
    elif (n > 20):
        print("Not Weird")
else:
    print("Weird")    