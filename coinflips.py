#Simulation of the martingale strategy in a double or nothing coin flip game
#Try it with 100, 100 & first

import random
import matplotlib.pyplot as plt

#An instance of the coinGame class is one game with a specific amount of starting chips and rounds
#The game is simulated in __init__ & there is a function defined to show the results
#Print results method not used right now, left in to make future improvement easier

class coinGame:
    def __init__(self, startingChips, noRounds):
        self.startingChips=startingChips
        self.noRounds=noRounds
        self.chipList=[]

        chips=startingChips
        previousWin=True
        betAmount=1
        betOn=1
        self.minChips=startingChips
        self.maxChips=startingChips
        self.noWins=0
        self.noLosses=0

        for thisRound in range(1,noRounds+1):

            if previousWin==True:
                betAmount=1
            else:
                betAmount*=2
            
            coin = random.randint(1, 2)
            
            if coin==betOn:
                previousWin=True
                chips+=betAmount;
                self.noWins+=1
                if chips>self.maxChips:
                    self.maxChips=chips
                    
            else:
                previousWin=False
                chips-=betAmount;
                self.noLosses+=1
                if chips<self.minChips:
                    self.minChips=chips

            self.chipList.append(chips)

        self.finalChips=chips

    def printResults(self):
        print("Number of rounds: "+str(self.noRounds))
        print("Number of wins: "+str(self.noWins))
        print("Number of losses: "+str(self.noLosses))
        print("Starting chips: "+str(self.startingChips))
        print("Final chips: "+str(self.finalChips))
        print("Lowest chip level during the game: "+str(self.minChips))
        print("Highers chip level during the game: "+str(self.maxChips))

#User input for all relevant variables
simStartingChips=int(input("Starting chips: "))
simRounds=int(input("Number of rounds in a game: "))
simGames=int(input("Number of games: "))

#List of games: not needed right now but kept in to make future improvement easier
games=[]

#Play the game n times and plot the chip level during the game
for i in range(1,simGames+1):
    games.append(coinGame(simStartingChips,simRounds))
    plt.plot(games[i-1].chipList)

plt.show()
