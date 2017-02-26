import random
from Lib import Bond
from Lib import Stock
import pandas as pd

####################################
#         Investor Class           #
####################################

#@Aim: Represent different type of investors
#@Initialize_date: 17-02-2017
#@Updates:      - [23-02-2017] : Create the function invest for the Defensive and Aggressive Investors
#               - [25-02-2017] : Create a method in order to merge different data series
#               - [25-02-2017] : Optimize function with Dataframe computation
#               - [26-02-2017] : Update function merge and join data



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
        STBond = Bond.ShortTerm(0, 0, 0)
        LTBond = Bond.LongTerm(0, 0, 0)

        year_s = int(str.split(self.startDate, '/')[2])
        year_e = int(str.split(self.endDate, '/')[2])

        Term =  year_e - year_s


        while self.budget >= STBond.getMinAmount() :

            choice = random.randint(0, 1)

            if(self.budget < LTBond.getMinAmount()):
                newShortT = Bond.ShortTerm(1000, self.startDate, self.endDate)
                self.budget = self.budget - 1000
                self.portfolio.append(newShortT)
            else:
                if(choice == 0):
                    newShortT = Bond.ShortTerm(1000, self.startDate, self.endDate)
                    self.budget = self.budget - 1000
                    self.portfolio.append(newShortT)
                else:
                    newLongT = Bond.LongTerm(3000, self.startDate, self.endDate)
                    self.budget = self.budget - 3000
                    self.portfolio.append(newLongT)
                #End If
            #End If

        #End while

    #-----


    def profitReturnSeries(self):
        Data = pd.DataFrame(index=self.portfolio[0].interestSeriesComplete().index, data=self.portfolio[0].interestSeriesComplete()['Interest'], columns=['Interest'])
        for i in range(1, len(self.portfolio)):
            Data = Data.add(self.portfolio[i].interestSeriesComplete(), fill_value=0)

        return Data


# Aggressive_Investor, extends Investor

class Aggressive_Investor(Investor):
    def __init__(self, budget, startDate, endDate):
        super(Aggressive_Investor, self).__init__(budget, startDate, endDate)

    def invest(self):


        while self.budget >= 100 :
            choiceS = random.randint(0, 9)
            stockName = self.default_stock[choiceS]

            stockToBuy = Stock.Stock(stockName, 0, self.startDate, self.endDate)

            MaxS = stockToBuy.maxStockAvailable(self.budget)


            choiceNb = random.randint(0, int(MaxS/2))
            stockToBuy.setNumberB(choiceNb)

            if(choiceNb != 0):
                stockToBuy.interestSeriesByTime()
                self.portfolio.append(stockToBuy)
                self.budget = self.budget - stockToBuy.amountInvest()

        #End While

    #End invest


    def profitReturnSeries(self):
        Data = pd.DataFrame(index=self.portfolio[0].interestSeriesComplete().index,
                            data=self.portfolio[0].interestSeriesComplete()['Interest'], columns=['Interest'])
        for i in range(1, len(self.portfolio)):
            tmp_Data = pd.DataFrame(index=self.portfolio[i].interestSeriesComplete().index,
                            data=self.portfolio[i].interestSeriesComplete()['Interest'], columns=['Interest'])
            Data = Data.add(tmp_Data, fill_value=0)

        return Data



# Mixed_Investor, extends Investor

class Mixed_Investor(Investor):
    def __init__(self, budget, startDate, endDate):
        super(Mixed_Investor, self).__init__(budget, startDate, endDate)


    def invest(self):

        #Default Bond
        STBond = Bond.ShortTerm(0, 0, 0)
        LTBond = Bond.LongTerm(0, 0, 0)

        year_s = int(str.split(self.startDate, '/')[2])
        year_e = int(str.split(self.endDate, '/')[2])

        Term = year_e - year_s

        while self.budget >= STBond.getMinAmount():
            choice = random.randint(0, 1)

            if (choice == 1):
                #It's a bond

                choice = random.randint(0, 1)

                if (self.budget < LTBond.getMinAmount()):
                    newShortT = Bond.ShortTerm(1000, self.startDate, self.endDate)
                    self.budget = self.budget - 1000
                    self.portfolio.append(newShortT)
                else:
                    if (choice == 0):
                        newShortT = Bond.ShortTerm(1000, self.startDate, self.endDate)
                        self.budget = self.budget - 1000
                        self.portfolio.append(newShortT)
                    else:
                        newLongT = Bond.LongTerm(3000, self.startDate, self.endDate)
                        self.budget = self.budget - 3000
                        self.portfolio.append(newLongT)
                    # End If
                # End If

            else:
                #It's a stock
                choiceS = random.randint(0, 9)
                stockName = self.default_stock[choiceS]

                stockToBuy = Stock.Stock(stockName, 0, self.startDate, self.endDate)

                MaxS = stockToBuy.maxStockAvailable(self.budget)

                choiceNb = random.randint(0, int(MaxS / 2))
                stockToBuy.sNumberB = choiceNb

                if (choiceNb != 0):
                    stockToBuy.interestSeriesByTime()
                    self.portfolio.append(stockToBuy)
                    self.budget = self.budget - stockToBuy.amountInvest()

                #End if
            #End If

        #End while



    def profitReturnSeries(self):
        firstDraw_B = True
        firstDraw_S = True

        for i in range(0, len(self.portfolio)):
            if (self.portfolio[i].whoIAm() == 'stock'):
                if(firstDraw_S):
                    DataS = pd.DataFrame(index=self.portfolio[i].interestSeriesComplete().index,
                                        data=self.portfolio[i].interestSeriesComplete()['Interest'],
                                        columns=['Interest'])
                    firstDraw_S = False
                else:
                    tmp_Data = pd.DataFrame(index=self.portfolio[i].interestSeriesComplete().index,
                                    data=self.portfolio[i].interestSeriesComplete()['Interest'], columns=['Interest'])
                    DataS = DataS.add(tmp_Data, fill_value=0)
                #End If
            #End If
            else:
                if (firstDraw_B):
                    DataB = pd.DataFrame(index=self.portfolio[i].interestSeriesComplete().index,
                                        data=self.portfolio[i].interestSeriesComplete()['Interest'],
                                        columns=['Interest'])
                    firstDraw_B = False
                else:
                    tmp_Data = pd.DataFrame(index=self.portfolio[i].interestSeriesComplete().index,
                                            data=self.portfolio[i].interestSeriesComplete()['Interest'],
                                            columns=['Interest'])
                    DataB = DataB.add(tmp_Data, fill_value=0)

        #End For

        if(firstDraw_B == False ):
            if(firstDraw_S == False):
                Data = DataB.join(DataS, how='inner', lsuffix='_l', rsuffix='_r')
                Data['Interest'] = Data['Interest_l'] + Data['Interest_r']

            else:
                Data = DataB
        else:
            if(firstDraw_S == True):
                Data = None
            else:
                Data = DataS


        return Data


#### STATIC METHODS ####



def mergeInvestorsSeries_Dataframe(list_of_investors, number_investors):
    # Now do the sum of each values
    # initialize the final series

    data_investors = list_of_investors[0].profitReturnSeries()
    Data = pd.DataFrame(index= data_investors.index, data=data_investors['Interest'], columns=['Interest'])

    for i in range(1, len(list_of_investors)):
        data_investors = list_of_investors[i].profitReturnSeries()

        Data['Interest'] = data_investors['Interest'] + Data['Interest']



    Data['Interest'] = Data['Interest'] / number_investors

    return Data