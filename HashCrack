import hashlib

def hash512(pw):    
    return hashlib.sha512(pw.encode('utf-8')).hexdigest().upper()

def crack512(hashToCrack):
    
    charSet='abcdefghijklmnopqrstuvwxyz'

    cracked=False

    for i in range(0, len(charSet)):
        for j in range(0, len(charSet)):
            for k in range(0, len(charSet)):
                PwTry=charSet[i]+charSet[j]+charSet[k]
                print("Trying: "+PwTry)
                if hash512(PwTry)==hashToCrack:
                    print("Pw found")
                    cracked=True
                    break
            if cracked==True:
                break
            j+=1
        if cracked==True:
            break
        i+=1
    if cracked==True:
        return PwTry
    else:
        return "0"


print("Insert the SHA 512 hash:")
hashInput=input()
print(crack512(hashInput))
