#Measuring the time to factorise 12..28 bit numbers

import time
import random

#generate an n bit random number

def generate_rand(size_bits):
    size = 2 ** size_bits
    return round(random.randint(0,size),0)

#find the factors of a number
#printing the factors is commented out to avoid skewing the numbers

def find_factors(num):
    factors=[]
    remaining=num
    i=2

    while remaining != 1:
        
        if remaining%i==0:
            #print(str(i), end="")
            factors.append(i)
            remaining=remaining/i
            i=1
            #if i!=remaining:
            #    print("*", end="")
        elif i==remaining:
            break
        i+=1

#factorising n_iter number of n_bit size numbers
#measuring the time elapsed and calculating the average
#printing is commented out to avoid skewing the numbers, except for displaying average times

def fact_bit_test(n_bit, n_iter):

    primes=[]
    for i in range(0,n_iter):
        primes.append(generate_rand(n_bit))
    
    times=[]
    
    for test_num in primes:
        start_time=time.time()
        #print("Factorising "+str(test_num))
        find_factors(test_num)
        end_time=time.time()
        times.append(end_time-start_time)
        #print("")
        #print("")

    total_time=0
    total_time_n=0
    for tm in times:
        total_time_n+=1
        total_time+=tm

    avg_time=total_time/total_time_n
    print("Average time of factorising "+str(n_bit)+" bit numbers: "+str(round(avg_time,4)))

#main loop, running the algorithm on 12..29 bit random numbers (100 times each)

def main():
    for j in range (12,29):
        fact_bit_test(j,100)

if __name__=="__main__":
    main()
