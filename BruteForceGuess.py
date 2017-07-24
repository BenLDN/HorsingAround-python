#How long does it take to "brute force" gues your password

import time
import itertools

chars="abcdefghijklmnopqrstuvwxyz"
length=5
done=False

start = time.time()

pw=input("Give me the pw (only small English letters please): ")

while True:
    def pwGuess(i):
        guesses=itertools.product(chars,repeat=i)
        for guess in guesses:
            yield ''.join(guess)

    for j in range(1,length+1):
        print("Trying "+str(j)+" length.")
        guessGenerator=pwGuess(j)
        for guess in guessGenerator:
            if guess==pw:
                print("Got it.")
                done=True
                break
        if done:
            break
    if done:
        break


end = time.time()
print("Time elapsed: "+str(end - start))
