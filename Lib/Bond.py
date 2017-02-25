import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import datetime

####################################
#           Bond Class             #
####################################

#@Aim: Represent a short term or a long term bon with specifics criteria
#@Initialize_date: 16-02-2017
#@Updates:  - [18-02-2017]: Added profit attribute to classes ShortTerm and LongTerm
#           - [22-02-2017]: Attributes updates + add compoundedInterest() + Draw a plot for a bond
#           - [23-02-2017]: Add function getMinAmount() + whoIAm()
#           - [25-02-2017]: Use of dataframe instead of list
#TODO: - Check the minimum Amount and Term
#      - Implement new method with only profit


class Bond(object):
    def __init__(self, amount, term, start_date):
        self._amount = amount
        self._start_date = start_date
        self._term = term
        self._mTerm = 0
        self._mAmount = 0
        self._interest = 0

        self.checkValue() # Check the minimum value f



    def checkValue(self):
        if(self._amount < self._mAmount):
            self._amount = self._mAmount

        if (self._term < self._mTerm):
            self._term = self._mTerm



    def drawPlot(self):
        plt.plot(self.interestSeries())
        plt.ylabel('Interest time series')
        plt.show()


    def interestSeries(self):
        seriesI = []
        for i in range(0,self._term):
            seriesI.append(self.coumpoundedInterest(i))

        return seriesI

    def addOneMonth(self,current_date):
        date = str.split(current_date, '-')

        if(int(date[1]) == 12) :
            date[0] = str(int(date[0]) + 1)
            date[1] = '1'
        else:
            date[1] = str(int(date[1]) + 1)

        return str(date[0] + '-' + date[1].zfill(2) + '-' + date[2].zfill(2))

    def interestSeriesComplete(self):
        Dates = []
        Interest = []
        date = str.split(self._start_date, '/')
        tmp_date = date[2] + '-' + date[1] + '-' + date[0]
        first_date = datetime.datetime(int(date[2]),int(date[1]),int(date[0]))

        Dates.append(first_date)
        Interest.append(self.coumpoundedInterest(0))

        nbMM = 12 * self._term
        currentDate = tmp_date

        for i in range(1,nbMM):
            currentDate = self.addOneMonth(currentDate)
            #seriesI[0].append(currentDate)
            #seriesI[1].append(self.coumpoundedInterest(i, (1/12)))
            date = str.split(currentDate, '-')
            Dates.append(datetime.datetime(int(date[0]),int(date[1]),int(date[2])))
            Interest.append(self.coumpoundedInterest(i, (1/12)))

        seriesI = pd.DataFrame(data= Interest, columns=['Interest'], index=Dates)

        return seriesI



    def interestSeriesByTime(self, Period):
        seriesI = []
        for i in range(0, Period):
            seriesI.append(self.coumpoundedInterest(i))

        return seriesI

    def coumpoundedInterest(self, time, n=1):
        return self._amount * ( 1 + self._interest)**(time * n)


    # GETTER & SETTER
    def getMinAmount(self):
        return self._mAmount

    def whoIAm(self):
        return 'bond'

#------

# Short Term Bond, extends Bond

class ShortTerm(Bond):
    def __init__(self, amount, term, start_date):
        super(ShortTerm, self).__init__(amount, term, start_date)
        self._mTerm = 2          # in years
        self._mAmount = 1000
        self._interest = 0.01


# Long Term Bond, extends Bond

class LongTerm(Bond):
    def __init__(self, amount, term, start_date):
        super(LongTerm, self).__init__(amount, term, start_date)
        self._mTerm = 5          # in years
        self._mAmount = 3000
        self._interest = 0.03


