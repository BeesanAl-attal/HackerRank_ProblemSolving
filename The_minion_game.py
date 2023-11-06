# Things to note in this Problem 
# 1. what is a consonants ? is any letter that is not a vowel 
# 2. what is a vowel ?  the vowels in english are the following [A, E, Y, U, O]
# NOTE : in this problem we are working with uppercase letters only 
# the key in this problem is the constrain for each player which is :
# player one gets to create words starting only with a vowel
# and the other player gets to create words starting only with a consonants

#---------------------------------# 
def minion_game(string):
    vowels = 'AEIOU' # to check for vowels 
    kevin_scores = stuart_scores = 0 # multiple variable assignment.
    lenght  = len(string) # This one is needed to calculate the score and for the loop as you will see 
    
    # the loop to used for the string and calculating the score for each player 
    for i in range(lenght):
        if string[i] in vowels : 
            kevin_scores += lenght - i
        else : 
            stuart_scores += lenght - i
    
    if stuart_scores > kevin_scores : 
        print (f'Stuart {stuart_scores}')
    elif kevin_scores > stuart_scores:
        print(f'Kevin {kevin_scores}')
    else :
        print('Draw')
    
# how did we calculated the score explained 
# first as we stated previously That the key of solving this problem is in the players constrains
# first you determin wether the charcter in the string is a vowel or a consonants from their you start calculating The score 
# to calculate the score you need to understand that if the letter is a vowel the first player will have lenght - i combinations 
# and so on  





