import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np

####################################
#           Bond Class             #
####################################

#@Aim: Represent a short term or a long term bon with specifics criteria
#@Initialize_date: 16-02-2017
#@Updates:  - [18-02-2017]: Added profit attribute to classes ShortTerm and LongTerm
#           - [22-02-2017]: Attributes updates + add compoundedInterest() + Draw a plot for a bond
#           - [23-02-2017]: Add function getMinAmount()
#TODO: - Check the minimum Amount and Term


class Bond(object):
    def __init__(self, amount, term):
        self._amount = amount
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

    def interestSeriesByTime(self, Period):
        seriesI = []
        for i in range(0, Period):
            seriesI.append(self.coumpoundedInterest(i))

        return seriesI

    def coumpoundedInterest(self, time):
        return self._amount * ( 1 + self._interest)**time


    # GETTER & SETTER
    def getMinAmount(self):
        return self._mAmount

#------

# Short Term Bond, extends Bond

class ShortTerm(Bond):
    def __init__(self, amount, term):
        super(ShortTerm, self).__init__(amount, term)
        self._mTerm = 2          # in years
        self._mAmount = 1000
        self._interest = 0.01


# Long Term Bond, extends Bond

class LongTerm(Bond):
    def __init__(self, amount, term):
        super(LongTerm, self).__init__(amount, term)
        self._mTerm = 5          # in years
        self._mAmount = 3000
        self._interest = 0.03

