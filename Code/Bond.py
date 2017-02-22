
####################################
#           Bond Class             #
####################################

#@Aim: Represent a short term or a long term bon with specifics criteria
#@Initialize_date: 16-02-2017
#@Updates:      - [22-02-2017] : Attributes updates + add compoundedInterest()
#TODO: - Add a plot for a n years interest


class Bond(object):
    def __init__(self, amount, term):
        self.amount = amount
        self.term = term
        self.mTerm = 0
        self.mAmount = 0
        self.interest = 0


    def coumpoundedInterest(self, time):
        return self.amount * ( 1 + self.interest)**time


#------

# Short Term Bond, extends Bond

class ShortTerm(Bond):
    def __init__(self, amount, term):
        super(ShortTerm, self).__init__(amount, term)
        self.mTerm = 2          # in years
        self.mAmount = 1000
        self.interest = 0.1



#------

# Long Term Bond, extends Bond

class LongTerm(Bond):
    def __init__(self, amount, term):
        super(LongTerm, self).__init__(amount, term)
        self.mTerm = 5          # in years
        self.mAmount = 3000
        self.interest = 0.3

