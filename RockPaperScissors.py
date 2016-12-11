import random

#initialisnig the list of possible choices and the boolean that keeps repeating the game

RPS=["R","P","S"]
stay=True

def whowon(you,me):

    #deciding who the winner is based on the two choices
    
    if (you not in RPS) or (me not in RPS):
        return "error"
    elif you==me:
        return "draw"
    elif (you=="R") and (me=="S"):
        return "you"
    elif (you=="R") and (me=="P"):
        return "me"                   
    elif (you=="S") and (me=="P"):
        return "you"
    elif (you=="S") and (me=="R"):
        return "me"
    elif (you=="P") and (me=="R"):
        return "you"
    elif (you=="P") and (me=="S"):
        return "me"

def chooserandom():
    
    #chossing R, P or S randomly
    
    i=random.randint(1,3)
    if i==1:
        return "R"
    elif i==2:
        return "P"
    elif i==3:
        return "S"
    else:
        return "error"

def choosewisely():

    #choosing R, P or S that is most likely to win based on the user's previous choices
    
    hist=histchoices()
    if hist["R"]>=hist["P"] and hist["R"]>=hist["S"]:
        return "P"
    elif hist["P"]>=hist["R"] and hist["P"]>=hist["S"]:
        return "S"
    elif hist["S"]>=hist["P"] and hist["S"]>=hist["R"]:
        return "R"
    else:
        return chooserandom()
    
def lettertoword(letter):
    
    #converting letters (R,P,S) into words (Rock, Paper, Scissors)
    
    if letter=="R":
        return "Rock"
    if letter=="P":
        return "Paper"
    if letter=="S":
        return "Scissors"

def oneround():
    
    #playing one round of RPS
    
    yourchoice=""
    mychoice=choosewisely()

    #only accepting R, P or S as input
    while yourchoice not in RPS:
        yourchoice=input("(R)ock, (P)aper or (S)cissors? ").upper()

    print("Your choice is: "+lettertoword(yourchoice)+", my choice is: "+lettertoword(mychoice))
    print("The winner is: "+whowon(yourchoice,mychoice))

    #saving the result into a file
    savetofile(yourchoice,mychoice)

def asknewround():
    
    #ask the user whether they want to play another round
    
    s=input("Quit: q/Q, another round: any other input.")
    if s.upper()=="Q":
        return False
    return True

def savetofile(you,me):
    
    #save the result in RPS.txt (your choice, my choice, winner)
    
    f=open('RPS.txt','a')
    f.write(you+me+whowon(you,me)[0].upper()+"\n")
    f.close()

def histchoices():

    #retrieving the number of choices for R, P and S from file into a dictionary variable
    
    choices={"R":0,"P":0,"S":0}
    f=open('RPS.txt','r')
    for line in f:
        userchoice=line[0]
        choices[userchoice]+=1
    f.close()
    return choices
    
#as long as the user chooses to play another round, keep repeating the RPS game

while stay:
    oneround()
    stay=asknewround()

#showing history before quitting
whathappened=histchoices()
print("Your choices so far:")
print("R: "+str(whathappened["R"]))
print("P: "+str(whathappened["P"]))
print("S: "+str(whathappened["S"]))

