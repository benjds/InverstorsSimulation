import random
from Code import Bond
from Code import Stock
####################################
#         Investor Class           #
####################################

#@Aim: Represent different type of investors
#@Initialize_date: 17-02-2017
#@Updates:      - [23-02-2017] : Create the function invest for the Defensive and Aggressive Investors
#TODO: - Add a method in order to sum all the data series


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

        print('---------------------')
        print('Defensive Inv Log')
        print('---------------------')

        while self.budget >= STBond.getMinAmount() :
            print(self.budget)
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
        print(self.budget)
    #-----

    def profitReturnSeries(self):

        series = [[],[]]

        for i in range(0,len(self.portfolio)) :
            #print(self.portfolio[i].whoIAm())

            myBond = self.portfolio[i]

            list_return = myBond.interestSeriesComplete()

            for j in range(0, len(list_return[0])):
                if(i == 0):
                    series[0].append(list_return[0][j])
                    series[1].append(list_return[1][j])
                else:
                    series[1][j] = series[1][j] + list_return[1][j]

                #End if

            #End For

        return series



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
            stockToBuy.setNumberB(choiceNb)

            if(choiceNb != 0):
                self.portfolio.append(stockToBuy)
                self.budget = self.budget - stockToBuy.amountInvest()

            print(self.budget)
        #End While

    #End invest


    def profitReturnSeries(self):

        series = [[],[]]

        for i in range(0,len(self.portfolio)) :
            #print(self.portfolio[i].whoIAm())

            # We get back the bond instance
            myStock = self.portfolio[i]
            myStock.interestSeriesByTime()

            for j in range(0, len(myStock.data['Dates'])):
                if(i == 0):
                    series[0].append(myStock.data['Dates'][j])
                    series[1].append(myStock.data['Interest'][j])
                else:
                    series[1].append(series[1][j] + myStock.data['Interest'][j])

                #End If

            #End For
        #End For


        return series




# Mixed_Investor, extends Investor

class Mixed_Investor(Investor):
    def __init__(self, budget, startDate, endDate):
        super(Mixed_Investor, self).__init__(budget, startDate, endDate)


    def invest(self):
        print('---------------------')
        print('Mixed Inv Log')
        print('---------------------')

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

            print(self.budget)
        #End while


    def profitReturnSeries(self):

        series = [[], []]
        firstDraw = True

        for i in range(0, len(self.portfolio)):
            # print(self.portfolio[i].whoIAm())


            if(self.portfolio[i].whoIAm() == 'stock'):
                # We get back the bond instance
                myStock = self.portfolio[i]
                myStock.interestSeriesByTime()

                for j in range(0, len(myStock.data['Dates'])):
                    if (firstDraw):
                        series[0].append(myStock.data['Dates'][j])
                        series[1].append(myStock.data['Interest'][j])
                    else:
                        series[1].append(series[1][j] + myStock.data['Interest'][j])

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