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
                newShortT = Bond.ShortTerm(1000, Term, self.startDate)
                self.budget = self.budget - 1000
                self.portfolio.append(newShortT)
            else:
                if(choice == 0):
                    newShortT = Bond.ShortTerm(1000, Term, self.startDate)
                    self.budget = self.budget - 1000
                    self.portfolio.append(newShortT)
                else:
                    newLongT = Bond.LongTerm(3000, Term, self.startDate)
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
                    newShortT = Bond.ShortTerm(1000, Term, self.startDate)
                    self.budget = self.budget - 1000
                    self.portfolio.append(newShortT)
                else:
                    if (choice == 0):
                        newShortT = Bond.ShortTerm(1000, Term, self.startDate)
                        self.budget = self.budget - 1000
                        self.portfolio.append(newShortT)
                    else:
                        newLongT = Bond.LongTerm(3000, Term, self.startDate)
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
                    self.portfolio.append(stockToBuy)
                    self.budget = self.budget - stockToBuy.amountInvest()

                #End if
            #End If

        #End while


    def profitReturnSeries_Details(self):

        series = [[], []]
        firstDraw = True

        for i in range(0, len(self.portfolio)):
            # print(self.portfolio[i].whoIAm())


            if(self.portfolio[i].whoIAm() == 'stock'):
                # We get back the bond instance
                myStock = self.portfolio[i]
                myStock.interestSeriesByTime()

                if(firstDraw):
                    length = len(myStock.data['Dates'])
                else:
                    length = min(len(myStock.data['Dates']), len(series[0]))

                for j in range(0, length):
                    if (firstDraw):
                        series[0].append(myStock.data['Dates'][j])
                        series[1].append(myStock.data['Interest'][j])
                    else:
                        series[1][j] = series[1][j] + myStock.data['Interest'][j]

                    # End If

                # End For

                firstDraw = False
            #End If

        #End For

        for i in range(0, len(self.portfolio)):
            if (self.portfolio[i].whoIAm() == 'bond'):

                myBond = self.portfolio[i]
                list_return = myBond.interestSeriesComplete()

                if(len(series[0])):
                    for j in range(0, len(list_return[0])):

                        for k in range(0, len(series[0])):
                            date_tmp_1 = str.split(series[0][k],'-')
                            date_tmp_2 = str.split(list_return[0][j],'-')
                            if((date_tmp_1[0] == date_tmp_2[0]) & (date_tmp_1[1] == date_tmp_2[1])):
                                series[1][k] = series[1][k] + list_return[1][j]
                            #End if
                        #End for

                    # End For
                else:
                    for j in range(0, len(list_return[0])):
                        if (i == 0):
                            series[0].append(list_return[0][j])
                            series[1].append(list_return[1][j])
                        else:
                            series[1][j] = series[1][j] + list_return[1][j]
                        # End if

                    # End For
                #End if

            #End if
        #End For


        return series

    def profitReturnSeries(self):

        series = [[], []]
        firstDraw = True

        for i in range(0, len(self.portfolio)):
            # print(self.portfolio[i].whoIAm())


            if(self.portfolio[i].whoIAm() == 'stock'):
                # We get back the bond instance
                myStock = self.portfolio[i]
                myStock.interestSeriesByTime()

                if(firstDraw):
                    length = len(myStock.data['Dates'])
                else:
                    length = min(len(myStock.data['Dates']), len(series[0]))

                for j in range(0, length):
                    day = str.split(myStock.data['Dates'][j], '-')[2]

                    if (day == '01'):
                        if (firstDraw):
                            series[0].append(myStock.data['Dates'][j])
                            series[1].append(myStock.data['Interest'][j])
                        else:
                            series[1][j] = series[1][j] + myStock.data['Interest'][j]
                        #End if

                    # End If

                # End For

                firstDraw = False
            #End If

        #End For

        for i in range(0, len(self.portfolio)):
            if (self.portfolio[i].whoIAm() == 'bond'):

                myBond = self.portfolio[i]
                list_return = myBond.interestSeriesComplete()

                if(len(series[0])):
                    for j in range(0, len(list_return[0])):

                        for k in range(0, len(series[0])):
                            date_tmp_1 = str.split(series[0][k],'-')
                            date_tmp_2 = str.split(list_return[0][j],'-')
                            if((date_tmp_1[0] == date_tmp_2[0]) & (date_tmp_1[1] == date_tmp_2[1])):
                                series[1][k] = series[1][k] + list_return[1][j]
                            #End if
                        #End for

                    # End For
                else:
                    for j in range(0, len(list_return[0])):
                        if (i == 0):
                            series[0].append(list_return[0][j])
                            series[1].append(list_return[1][j])
                        else:
                            series[1][j] = series[1][j] + list_return[1][j]
                        # End if

                    # End For
                #End if

            #End if
        #End For


        return series

#### STATIC METHODS ####

def mergeInvestorsSeries(list_of_investors, number_investors):
    # Now do the sum of each values
    # initialize the final series
    model_investor_series = [[], []]

    for i in range(0, number_investors):

        list_value = list_of_investors[i].profitReturnSeries()[1]

        if (i == 0):
            list_date = list_of_investors[i].profitReturnSeries()[0]
            length = len(list_date)
        else:
            length = min(len(list_value),len(model_investor_series[0]))

        for j in range(0, length):
            if (i == 0):
                model_investor_series[0].append(list_date[j])
                model_investor_series[1].append(list_value[j])
            else:
                model_investor_series[1][j] = model_investor_series[1][j] + list_value[j]
                # End if
                # End for
    # End for

    # Divide the value by the number of investors

    for k in range(0, len(model_investor_series[1])):
        model_investor_series[1][k] = model_investor_series[1][k] / number_investors
    #End for

    return model_investor_series



def mergeInvestorsSeries_Dataframe(list_of_investors, number_investors):
    # Now do the sum of each values
    # initialize the final series

    data_investors = list_of_investors[0].profitReturnSeries()
    Data = pd.DataFrame(index= data_investors.index, data=data_investors['Interest'], columns=['Interest'])

    for i in range(1, len(list_of_investors)):
        data_investors = list_of_investors[i].profitReturnSeries()
        Data = Data.add(data_investors)


    Data['Interest'] = Data['Interest'] / number_investors

    return Data