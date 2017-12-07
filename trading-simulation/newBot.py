#WIP
import copy
import matplotlib.pyplot as plt

i=j=k=0

class state:

    def __init__(self, period, price, money, stock, avgcost):
        self.period=period
        self.price=price
        self.money=money
        self.stock=stock
        self.avgcost=avgcost

    def show(self):        
        print("Period: "+str(self.period))
        print("Price: "+str(self.price))
        print("Money: "+str(self.money))
        print("Stock: "+str(self.stock))
        print("Average cost: "+str(self.avgcost))
        print("Market value: "+str(self.money+self.stock*self.price))

    def buy(self, amount, commission=0):
        if self.money>=self.price*amount*(1+commission) and amount>0:
            self.avgcost=(self.avgcost*self.stock+self.price*amount)/(self.stock+amount)
            self.stock+=amount
            self.money-=amount*self.price*(1+commission)
        return self
        
    def sell(self, amount, commission=0):
        if self.stock>=amount and amount>0:
            self.stock-=amount
            self.money+=(amount*self.price)*(1-commission)
        return self

    def getMktVal(self):
        return self.money+self.stock*self.price

def getPriceList(filename):
    priceList=[float(price.rstrip('\n')) for price in open(filename)]
    return priceList

def addState0(states, price, money):
    states.append(state(0,price,money,0,0))

def addState(states, price):
    states.append(copy.deepcopy(states[len(states)-1]))
    states[len(states)-1].period+=1
    states[len(states)-1].price=price
    return len(states)-1

def showProfit(states): 
    print("Market value now: "+str(states[len(states)-1].getMktVal()))
    print("Starting market value: "+str(states[0].getMktVal()))
    print("Profit: "+str(states[len(states)-1].getMktVal()-states[0].getMktVal()))  

def plot_results(states):
    plot_market=[]
    plot_price=[]
    for st in states:
        plot_market.append(st.getMktVal()/states[0].getMktVal())
        plot_price.append(st.price/states[0].price)
    plt_m=plt.plot(plot_market)
    plt_p=plt.plot(plot_price)
    plt.show()

def game_b1_s1(states, priceList):
    addState0(states, priceList[0], priceList[0]*10)
    for pr in priceList:
        i=addState(states, pr)
        if states[i].price<states[i-1].price:
            states[i].buy(1,0.01)
        if states[i].price>states[i-1].price:
            states[i].sell(1,0.01)
        states[i].show()
        print("")
    showProfit(states)

def game_martingale(states, priceList):
    losses=0
    addState0(states, priceList[0], priceList[0]*10)
    for pr in priceList:
        i=addState(states, pr)
        if i==1:
            states[i].buy(1,0.1)
        else:
            if states[i].price<states[i-1].price:
                losses=states[i].stock*(states[i].avgcost-states[i].price)
                states[i].buy(max(losses-states[i].stock+0.1, states[i].money/states[i].price))
            if states[i].price>states[i-1].price:
                states[i].sell(states[i].stock) 
        states[i].show()
        print("")
    showProfit(states)

def game_dca(states, priceList):
    addState0(states, priceList[0], priceList[0]*10)
    for pr in priceList:
        i=addState(states, pr)
        if i<len(priceList)-1:
            states[i].buy((len(priceList)-1)/states[i].money)
        else:
            states[i].sell(states[i].stock)
        states[i].show()
        print("")
    showProfit(states)

#price_file=input("Which pricelist should be used? (bear, btc, gold)")
#game_type=input("Please select trading strategy (s1b1, mart)")

price_file="btc"

priceList=getPriceList(price_file + '.csv')

states2=[]
game_b1_s1(states2, priceList)
plot_results(states2)

