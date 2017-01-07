import random

class coinGame:
    def __init__(self, startingChips, noRounds):
        self.startingChips=startingChips
        self.noRounds=noRounds

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
            self.finalChips=chips

    def printResults(self):
        print("Number of rounds: "+str(self.noRounds))
        print("Number of wins: "+str(self.noWins))
        print("Number of losses: "+str(self.noLosses))
        print("Starting chips: "+str(self.startingChips))
        print("Lowest chip level during the game: "+str(self.minChips))
        print("Highers chip level during the game: "+str(self.maxChips))

        

game=coinGame(100,100)
game.printResults()
