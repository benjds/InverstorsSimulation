####################################
#         Investor Class           #
####################################

#@Aim: Represent different type of investors
#@Initialize_date: 17-02-2017
#@Updates:      - [00-00-2017] :
#TODO: - Add Invest() functions


class Investor(object):
    def __init__(self, budget, startDate):
        self.budget = budget
        self.startDate = startDate


# Defensive_Investor, extends Investor

class Defensive_Investor(Investor):
    def __init__(self, budget, startDate):
        super(budget, startDate)



# Aggressive_Investor, extends Investor

class Aggressive_Investor(Investor):
    def __init__(self, budget, startDate):
        super(budget, startDate)



# Mixed_Investor, extends Investor

class Mixed_Investor(Investor):
    def __init__(self, budget, startDate):
        super(budget, startDate)

