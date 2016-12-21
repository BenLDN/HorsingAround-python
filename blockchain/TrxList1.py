#blockchain experiment 1

class trx:
    def __init__(self, trID, sender, receiver, amount):
        self.trID=trID
        self.sender=sender
        self.receiver=receiver
        self.amount=amount

def showBalances(trxArray):
    participants={}
    for oneTrx in trxArray:
        if oneTrx.sender not in participants:
            participants[oneTrx.sender]=0
        if oneTrx.receiver not in participants:
            participants[oneTrx.receiver]=0
        participants[oneTrx.sender]-=oneTrx.amount
        participants[oneTrx.receiver]+=oneTrx.amount
    for participant,balance in participants.items():
        print(participant+" balance: "+str(balance))
    

allTrx=[]

allTrx.append(trx('t1','o','a1',10))
allTrx.append(trx('t2','o','a2',20))
allTrx.append(trx('t3','o','a3',10))
allTrx.append(trx('t4','o','a4',10))
allTrx.append(trx('t5','o','a5',10))

allTrx.append(trx('t6','a1','a3',5))
allTrx.append(trx('t7','a2','a5',5))
allTrx.append(trx('t8','a2','a1',10))
allTrx.append(trx('t9','a4','a2',5))
allTrx.append(trx('t10','a3','a5',5))
allTrx.append(trx('t11','a5','a2',10))
allTrx.append(trx('t12','a1','a2',5))

showBalances(allTrx)
