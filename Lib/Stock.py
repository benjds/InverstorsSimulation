import pandas_datareader.data as web
import datetime
from matplotlib import style
import matplotlib.pyplot as plt


####################################
#           Stock Class            #
####################################

#@Aim: Represent a stock on a market
#@Initialize_date: 16-02-2017
#@Updates:      - [22-02-2017] : Manage the datas get back and draw plot
#               - [23-02-2017]: add functions => selectDayPrice(), maxStockAvailable(), amountInvest(), setNumberB()
#               - [25-02-2017]: load the data just once
#               - [25-02-2017]: Optimize the dataframe managing
#               - [27-02-2017]: Clean the code and add comment

start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2016, 1, 1)

options = {'AAPL' : web.DataReader('AAPL', 'google', start, end),
           'GOOGL' : web.DataReader('GOOGL', 'google', start, end),
           'YHOO' : web.DataReader('YHOO', 'google', start, end),
           'AXP' : web.DataReader('AXP', 'google', start, end),
           'XOM' : web.DataReader('XOM', 'google', start, end),
           'KO' : web.DataReader('KO', 'google', start, end),
           'NOK' : web.DataReader('NOK', 'google', start, end),
           'MS' : web.DataReader('MS', 'google', start, end),
           'IBM' : web.DataReader('IBM', 'google', start, end),
           'FDX' : web.DataReader('FDX', 'google', start, end)
}

print("Stock data imported !")

class Stock(object):

    def __init__(self, ticker, numberB, startDate, endDate):
        self.sTicker = ticker           # Stock Name, ex: GOOGL
        self.sNumberB = numberB         # Number of stocks bought
        self.sStartDate = startDate     # Date when they bought the stock
        self.sEndDate = endDate

        self.sDate = str.split(startDate,'/')
        self.eDate = str.split(endDate, '/')

        self.start = datetime.datetime(int(self.sDate[2]), int(self.sDate[1]), int(self.sDate[0]))
        self.end = datetime.datetime(int(self.eDate[2]), int(self.eDate[1]), int(self.eDate[0]))

        #self.data = web.DataReader(ticker, 'google', self.start, self.end)
        self.data = options[ticker]
        self.data = self.data.truncate(self.start, self.end)



    # @FunctionName: whoIAm()
    # @Goal: Return the name of class type
    # @Parameters: Self, class instance
    # @Return: A string name of the class
    def whoIAm(self):
        return 'stock'


    # @FunctionName: plotStock()
    # @Goal: Make a simple plot
    # @Parameters: Self, class instance
    # @Return: None
    def plotStock(self):
        style.use('fivethirtyeight')
        self.data['High'].plot()
        plt.show()


    # @FunctionName: selectDayPrice()
    # @Goal: Give the first value of the stock
    # @Parameters: Self, class instance
    # @Return: None
    def selectDayPrice(self):
        return (self.data['High'][0])


    # @FunctionName: maxStockAvailable()
    # @Goal: Compute the maximum quantity of the stock available with a specific budget
    # @Parameters: - Self, class instance
    #              - budget, integer
    # @Return: None
    def maxStockAvailable(self, budget):
        dayPrice = self.selectDayPrice()

        return int(budget/dayPrice)

    # @FunctionName: amountInvest()
    # @Goal: Give the real value of the stock
    # @Parameters: Self, class instance
    # @Return: None
    def amountInvest(self):
        return self.sNumberB * self.selectDayPrice()


    # @FunctionName: interestSeriesByTime()
    # @Goal: Compute the value of the stock for each rows
    # @Parameters: Self, class instance
    # @Return: None
    def interestSeriesByTime(self):
        self.data['Interest'] = self.data['High'] * self.sNumberB

    # @FunctionName: setNumberB()
    # @Goal: Setter of the attribut sNumberB
    # @Parameters: Self, class instance
    # @Return: None
    def setNumberB(self, value):
        self.sNumberB = value

    # @FunctionName: interestSeriesComplete()
    # @Goal: Getter of the attribut data
    # @Parameters: Self, class instance
    # @Return: None
    def interestSeriesComplete(self):
        return self.data


    # @FunctionName: periodInterest()
    # @Goal: Get a period interest for the given period
    # @Parameters: Self, class instance
    # @Return: None
    def periodInterest(self):
        return self.data['Interest'][len(self.data)-1] - self.data['Interest'][0]