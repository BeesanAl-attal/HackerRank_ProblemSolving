'''
THE ABSTRACT EXPLANITION
Here the problem is that we have a shoe shop owned by Raghu
he has X number of shoes and depending on the context all the shoes in his shop,
are the same style for example,  he has 10 white sneakers but 10 different sizes
and the different sizes have different prices.
the next thing that we should point it out is the customer will buy if and only if 
he/she finds her desired "shoe size"
'''
'''
The Data structure
first the needed data to compute the earned money is entered via the user
X --> the number of shoes in the store 
list_of_sizes --> list of sizes availble 
N --> the number of customers 
the last entered values are the tricky part because here 
we are going to enter two values spreated by space as follows ->
the desired shoe size the price of the shoe 
6 55
8 22
here we need to check if the size is availble
'''
# without using collections.Counter
# total prices
EarnedMoney = 0

# number of shoeses in the shop
X = int(input())

#list of the sizes
listOfSizes = input().split()

# number of customers
N = int(input())

# entering the desired size and its price 
# then calculating the total
for i in range(0,N):
  SizeAndPrice = input().split()
  if SizeAndPrice[0] in listOfSizes:
      listOfSizes.remove(SizeAndPrice[0])
      EarnedMoney += int(SizeAndPrice[1])
print(EarnedMoney)

# another solution
# with using the collections.Counter
from collections import Counter
num_of_shoes = int(input())
list_of_sizes = list(map(int, input().split()))
num_of_customers = int(input())
counter_of_sizes = Counter(list_of_sizes)

total = 0 
for customer in range(num_of_customers):
   size, price = list(map(int, input().split()))
   if size in counter_of_sizes.keys():
      if counter_of_sizes[size] > 0:
         total = total + price # of total += price
         counter_of_sizes[size] = counter_of_sizes[size] - 1
         
print(total)

# i concluded that the advantage for using Counter function is to mantain a good structure for storing the shoes sizes
# and a good way to work with the shoe size as the key for your dictionary 






