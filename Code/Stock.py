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
#               - [23-02-2017]: add functions => selectDayPrice(), maxStockAvailable(), amountInvest()

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

        self.data = web.DataReader(ticker, 'google', self.start, self.end)

        dates = []

        for x in range(len(self.data )):
            newdate = str(self.data .index[x])
            newdate = newdate[0:10]
            dates.append(newdate)

        self.data['Dates'] = dates



    def plotStock(self):
        style.use('fivethirtyeight')
        self.data['High'].plot()
        plt.show()


    def selectDayPrice(self):
        return (self.data.ix[self.data['Dates'][0]]['Close'])


    def maxStockAvailable(self, budget):
        #First find price
        #dayPrice = self.data.ix[self.sDate[2] + '-' + self.sDate[1] + '-' + self.sDate[0]]['Close']
        dayPrice = self.selectDayPrice()
        #print('day price = '+ str(dayPrice))

        return int(budget/dayPrice)


    def amountInvest(self):
        return self.sNumberB * self.selectDayPrice()