chineseFoodCount = int(0)
mexicanFoodCount = int(0)
americanFoodCount = int(0)

def getName():
    return input("enter your name: ")

def getVote():
    return input("Enter 1 for Chinese food, 2 for Mexican food, or 3 for American food: ") 

n1 = getName()

v1 = int(getVote())

if v1 == 1:
    chineseFoodCount += 1
    print(chineseFoodCount)
    print(n1 + " you have chosen Chinese food for your vote.")
elif v1 == 2:
    mexicanFoodCount += 1
    print(n1 + " you have chosen Mexican food for your vote.")
elif v1 == 3:
    americanFoodCount += 1
    print(n1 + " you have chosen American food for your vote")

