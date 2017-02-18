####################################
#           Bond Class             #
####################################


# @Aim: Represent a short term or a long term bon with specifics criteria
# @Initialize_date: 16-02-2017
# @Updates:      - [18-02-2017]: Added profit attribute to classes ShortTerm and LongTerm
# TODO: Add plots


from math import pow


class Bond(object):
    def __init__(self, amount):
        self.amount = amount


# Short Term Bond, extends Bond


class ShortTerm(Bond):
    def __init__(self, amount, term):
        super(int)
        self.term = term
        self.mTerm = 2          # in years
        self.mAmount = 1000
        self.interest = 0.01
        self.profit = amount * (pow((1 + self.interest), self.term))

# Long Term Bond, extends Bond


class LongTerm(Bond):
    def __init__(self, amount, term):
        super(int)
        self.term = term
        self.mTerm = 5          # in years
        self.mAmount = 3000
        self.interest = 0.03
        self.profit = amount * (pow((1 + self.interest), self.term))


y = Bond(3000)

x = ShortTerm(y.amount, 2)
print(x.profit)

z = LongTerm(y.amount, 5)
print(z.profit)
