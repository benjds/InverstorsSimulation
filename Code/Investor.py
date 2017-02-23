import random
from Code import Bond
from Code import Stock
####################################
#         Investor Class           #
####################################

#@Aim: Represent different type of investors
#@Initialize_date: 17-02-2017
#@Updates:      - [23-02-2017] : Create the function invest for the Defensive and Aggressive Investors
#TODO: - Add Invest() functions for Mixed


class Investor(object):
    def __init__(self, budget, startDate, endDate):
        self.budget = budget
        self.startDate = startDate
        self.endDate = endDate
        self.portfolio = []
        self.default_stock = ['AAPL', 'GOOGL', 'YHOO', 'AXP', 'XOM', 'KO', 'NOK', 'MS', 'IBM', 'FDX']


# Defensive_Investor, extends Investor

class Defensive_Investor(Investor):
    def __init__(self, budget, startDate, endDate):
        super(Defensive_Investor, self).__init__(budget, startDate, endDate)

    def invest(self):
        #Default Bond
        STBond = Bond.ShortTerm(0, 0)
        LTBond = Bond.LongTerm(0, 0)

        year_s = int(str.split(self.startDate, '/')[2])
        year_e = int(str.split(self.endDate, '/')[2])

        Term =  year_e - year_s

        print('---------------------')
        print('Defensive Inv Log')
        print('---------------------')

        while self.budget >= STBond.getMinAmount() :
            print(self.budget)
            choice = random.randint(0, 1)

            if(self.budget < LTBond.getMinAmount()):
                newShortT = Bond.ShortTerm(1000, Term)
                self.budget = self.budget - 1000
                self.portfolio.append(newShortT)
            else:
                if(choice == 0):
                    newShortT = Bond.ShortTerm(1000, Term)
                    self.budget = self.budget - 1000
                    self.portfolio.append(newShortT)
                else:
                    newLongT = Bond.LongTerm(3000, Term)
                    self.budget = self.budget - 3000
                    self.portfolio.append(newLongT)
                #End If
            #End If

        #End while
        print(self.budget)
    #-----



# Aggressive_Investor, extends Investor

class Aggressive_Investor(Investor):
    def __init__(self, budget, startDate, endDate):
        super(Aggressive_Investor, self).__init__(budget, startDate, endDate)

    def invest(self):
        print('---------------------')
        print('Aggressive Inv Log')
        print('---------------------')

        while self.budget >= 100 :
            choiceS = random.randint(0, 9)
            stockName = self.default_stock[choiceS]

            stockToBuy = Stock.Stock(stockName, 0, self.startDate, self.endDate)

            MaxS = stockToBuy.maxStockAvailable(self.budget)

            choiceNb = random.randint(0, int(MaxS/2))
            stockToBuy.sNumberB = choiceNb

            if(choiceNb != 0):
                self.portfolio.append(stockToBuy)
                self.budget = self.budget - stockToBuy.amountInvest()

            print(self.budget)
        #End While

    #End invest




            # Mixed_Investor, extends Investor

class Mixed_Investor(Investor):
    def __init__(self, budget, startDate):
        super(Mixed_Investor, self).__init__(budget, startDate)


    def invest(self):
        print('---------------------')
        print('Mixed Inv Log')
        print('---------------------')