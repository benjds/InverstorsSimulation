import pandas_datareader.data as web
import datetime
from matplotlib import style
import matplotlib.pyplot as plt
import os

####################################
#           Stock Class            #
####################################

#@Aim: Represent a stock on a market
#@Initialize_date: 16-02-2017
#@Updates:      - [22-02-2017] : Manage the datas get back and draw plot

class Stock(object):

    def __init__(self, ticker, numberB, startDate, endDate):
        self.sTicker = ticker           # Stock Name, ex: GOOGL
        self.sNumberB = numberB         # Number of stocks bought
        self.sStartDate = startDate     # Date when they bought the stock
        self.sEndDate = endDate

        sDate = str.split(startDate,'/')
        eDate = str.split(endDate, '/')

        start = datetime.datetime(int(sDate[2]), int(sDate[1]), int(sDate[0]))
        end = datetime.datetime(int(eDate[2]), int(eDate[1]), int(eDate[0]))

        self.data = web.DataReader(ticker, 'yahoo', start, end)['High']



    def plotStock(self):
        style.use('fivethirtyeight')
        self.data['High'].plot()
        plt.show()