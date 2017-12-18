#Hopefully I'll find a more efficient algorithm to factorise numbers

num=int(input("Give me an integer:"))

print("Factorising "+str(num))

factors=[]
remaining=num
i=2

while True:
    
    if remaining%i==0:
        print("Factor found: "+str(i))
        factors.append(i)
        remaining=remaining/i
        i=1
    elif i==remaining:
        print("Factor found: "+str(i))
        factors.append(i)
        break

    i+=1

