#blockchain experiment 2
import hashlib

def hashit(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest().upper()

class trx:
    trxCount=0
    def __init__(self, sender, receiver, amount):
        trx.trxCount+=1
        self.no=trx.trxCount
        self.sender=sender
        self.receiver=receiver
        self.amount=amount

class block:
    blockCount=0
    def __init__(self, trxList, refPrev="0"):
        block.blockCount+=1
        self.no=block.blockCount
        self.refPrev=refPrev
        self.trxList=trxList
        self.valid=False
        textToHash=str(self.no)+refPrev
        for oneTrx in trxList:
            textToHash+=str(oneTrx.no)+oneTrx.sender+oneTrx.receiver+str(oneTrx.amount)
        self.hash=hashit(textToHash)
        
    def validate(self):
        self.valid=True
        ledger=getBalanceBlocks(allBlocks[0:self.no])
        for name,bal in ledger.items():
            if bal<0 and name!="o":
                self.valid=False
        if self.refPrev!=allBlocks[self.no-2].hash:
            self.valid=False

        

def getBalanceBlocks(blockArray):
    participants={}
    for oneBlock in blockArray:
        for oneTrx in oneBlock.trxList:
            if oneTrx.sender not in participants:
                participants[oneTrx.sender]=0
            if oneTrx.receiver not in participants:
                participants[oneTrx.receiver]=0
            participants[oneTrx.sender]-=oneTrx.amount
            participants[oneTrx.receiver]+=oneTrx.amount
    return participants

allTrx=[]

allTrx.append(trx('o','a1',10))
allTrx.append(trx('o','a2',20))
allTrx.append(trx('o','a3',10))
allTrx.append(trx('o','a4',10))
allTrx.append(trx('o','a5',10))
allTrx.append(trx('a1','a3',5))
allTrx.append(trx('a2','a5',5))
allTrx.append(trx('a2','a1',10))
allTrx.append(trx('a4','a2',5))
allTrx.append(trx('a3','a5',5))
allTrx.append(trx('a5','a2',10))
allTrx.append(trx('a1','a2',5))

allBlocks=[]

allBlocks.append(block([allTrx[0],allTrx[1]]))
allBlocks.append(block([allTrx[2],allTrx[3]],allBlocks[0].hash))
allBlocks.append(block([allTrx[4],allTrx[5]],allBlocks[1].hash))
allBlocks.append(block([allTrx[6],allTrx[7]],allBlocks[2].hash))
allBlocks.append(block([allTrx[8],allTrx[9]],allBlocks[3].hash))
allBlocks.append(block([allTrx[10],allTrx[11]],allBlocks[4].hash))

listToPrint=getBalanceBlocks(allBlocks)

for name,balance in listToPrint.items():
    print(name+": "+str(balance))

allBlocks[5].validate()
print(allBlocks[5].valid)
print(allBlocks[5].hash)

