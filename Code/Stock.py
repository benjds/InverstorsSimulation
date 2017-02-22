

####################################
#           Stock Class            #
####################################

#@Aim: Represent a stock on a market
#@Initialize_date: 16-02-2017
#@Updates:      - [00-00-2017] :

class Stock(object):
    def __init__(self, term, name, numberB, startDate, endDate):
        self.sTerm = term           # Period of the stock
        self.sName = name           # Stock Name, ex: GOOGL
        self.sNumberB = numberB     # Number of stocks bought
        self.sStartDate = startDate     # Date when they bought the stock
        self.sEndDate = endDate