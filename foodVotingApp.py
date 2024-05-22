'''Our function for taking a name entry from the user'''
def getName():
    return input("Enter your name: ")

'''Our function for taking a number from 1 through however max options of food'''
'''CAUTION, still needs an error check for options that are not numbers, like letters, doubles, and strings'''
def getVote():
    return input("Enter 1 for a Chinese food vote, 2 for a Mexican food vote, or 3 for an American food vote: ") 

'''The methods above called and stored in two different variable names, n1 and vote'''
n1 = getName()
vote = int(getVote())

'''This is our function for checking if the input from our user matches CHINESE FOOD'''
def chineseFoodCheck(voteNum):
    chineseFoodCount = int(0)
    if voteNum == 1:
        chineseFoodCount += 1
        print(n1 + " you have chosen Chinese food for your vote.")
        return(chineseFoodCount)
    else:
        pass

'''This is our function for checking if the input from our user matches MEXICAN FOOD'''
def mexicanFoodCheck(voteNum):
    mexicanFoodCount = int(0)
    if voteNum == 2:
        mexicanFoodCount += 1
        print(n1 + " you have chosen Mexican food for your vote.")
        return(mexicanFoodCount)
    else: 
        pass

'''This is our function for checking if the input from our user matches AMERICAN FOOD'''
def americanFoodCheck(voteNum):
    americanFoodCount = int(0)
    if voteNum == 3:
        americanFoodCount += 1
        print(n1 + " you have chosen American food for your vote")
        return(americanFoodCount)
    else: 
        pass

"""We have here, all three food check functions being run and stored as c m and a"""
c = chineseFoodCheck(vote)
m = mexicanFoodCheck(vote)
a = americanFoodCheck(vote)

"""Finally, we are presented with the syntatic console response, a sort of tally, of all food votes"""
print("Chinese food was voted for, " + str(c) + " times. Secondly, Mexican food was voted for, " + str(m) + " times. And lastly, American food was voted for, " + str(a) + " times.")

'''This program was written by Anthony T'''