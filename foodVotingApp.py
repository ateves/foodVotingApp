def getName():
    return input("Enter your name: ")

def getVote():
    return input("Enter 1 for a Chinese food vote, 2 for a Mexican food vote, or 3 for an American food vote: ") 

n1 = getName()
vote = int(getVote())

def chineseFoodCheck(voteNum):
    chineseFoodCount = int(0)
    if voteNum == 1:
        chineseFoodCount += 1
        print(n1 + " you have chosen Chinese food for your vote.")
        return(chineseFoodCount)
    else:
        pass

def mexicanFoodCheck(voteNum):
    mexicanFoodCount = int(0)
    if voteNum == 2:
        mexicanFoodCount += 1
        print(n1 + " you have chosen Mexican food for your vote.")
        return(mexicanFoodCount)
    else: 
        pass

def americanFoodCheck(voteNum):
    americanFoodCount = int(0)
    if voteNum == 3:
        americanFoodCount += 1
        print(n1 + " you have chosen American food for your vote")
        return(americanFoodCount)
    else: 
        pass

c = chineseFoodCheck(vote)
m = mexicanFoodCheck(vote)
a = americanFoodCheck(vote)

print("Chinese food was voted for, " + str(c) + " times. Secondly, Mexican food was voted for, " + str(m) + " times. And lastly, American food was voted for, " + str(a) + " times.")