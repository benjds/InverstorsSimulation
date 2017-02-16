
####################################
#           Bond Class             #
####################################

#@Aim: Represent a short term or a long term bon with specifics criteria
#@Initialize_date: 16-02-2017
#@Updates:      - [00-00-2017] :
#TODO: - Add a coumpoundedInterest function for each bond type


class Bond(object):
    def __init__(self, amount):
        self.amount = amount




#------

# Short Term Bond, extends Bond

class ShortTerm(Bond):
    def __init__(self, amount):
        super(amount)
        self.mTerm = 2          # in years
        self.mAmount = 1000
        self.interest = 0.1



#------

# Long Term Bond, extends Bond

class LongTerm(Bond):
    def __init__(self, amount):
        super(amount)
        self.mTerm = 5          # in years
        self.mAmount = 3000
        self.interest = 0.3
