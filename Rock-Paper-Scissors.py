import random

#Rock Paper Scissors
def putInFull(choice):
    if choice == "r":
        return "Rock"
    elif choice == 's':
        return "Scissors"
    else:
        return "Paper"



def rspLogic(games):
    humanScore = 0
    CompScore = 0

    CompOptions = ['r', 's', 'p']
    
    for i in range(games):
        hand = input("\nRound {i}\n R for Rock, P for Paper, S for Scissors: \n ".format(i = i+1)).lower()
        CompChoice = CompOptions[random.randint(0,2)]
        if (hand == "r" or hand == "p" or hand == "s"):
            print("Computer chose {CompChoice}, You chose {userChoice}".format(CompChoice = putInFull(CompChoice).upper(), userChoice = putInFull(hand).upper()))
            if(hand == CompChoice):
                print(" It's A Draw ")   
            elif(hand == 'r' and CompChoice == 's' or hand == 'p' and CompChoice == 'r' or hand == 's' and CompChoice == 'p'):
                print("You win this round")
                humanScore +=1
            else:
                print("Computer Wins this round...")
                CompScore += 1
        else:
            print("invalid selection")
            break
    
    print("\n Final Scoreboard: \n")
    if(humanScore > CompScore):
        print("You {humanScore} - {CompScore} Computer \n You've Won!!!!".format(humanScore = humanScore, CompScore = CompScore))    
    if(humanScore == CompScore):
        print("You {humanScore} - {CompScore} Computer \n It's all square".format(humanScore = humanScore, CompScore = CompScore))    
    elif(humanScore < CompScore):
        print("You {humanScore} - {CompScore} Computer \n Computer has Won!!!!".format(humanScore = humanScore, CompScore = CompScore))    

print("You are about to play Rock-Paper-Scissors with the Computer \n How many games do you wish to play? (odd numbers only!) ")

numOfGames = int(input(" Best of ?: "))

try:
    if numOfGames % 2 == 0 and numOfGames < 10:
        print("We will play {games} games instead ".format(games  = numOfGames + 1))
        rspLogic(numOfGames+1)
    else:
        rspLogic(numOfGames) 

except:
    print("that's an invalid number")


