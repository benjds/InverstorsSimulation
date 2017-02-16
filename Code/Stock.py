

####################################
#           Stock Class            #
####################################

#@Aim: Represent a stock on a market
#@Initialize_date: 16-02-2017
#@Updates:      - [00-00-2017] :

class Stock(object):
    def __init__(self, term, amount, name, numberB, buyDate):
        self.sTerm = term           # Period of the stock
        self.sAmount = amount       # Amount invest
        self.sName = name           # Stock Name, ex: GOOGL
        self.sNumberB = numberB     # Number of stocks bought
        self.sBuyDate = buyDate     # Date when they bought the stock
