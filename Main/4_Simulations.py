from Lib import Investor
import plotly
import plotly.graph_objs as go
import os

###########################################
#           Part 4: Simulations           #
###########################################


Numbers_of_investors = 10
Budget = 10000
Years = ['2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']


#Defensive investor

defensive_investors = []

#create the 1000 defensive investor
for i in range(0,Numbers_of_investors):
    new_Investor = Investor.Defensive_Investor(Budget,'01/03/2011','15/02/2015')
    new_Investor.invest()
    defensive_investors.append(new_Investor)


model_defensive_investor_series = Investor.mergeInvestorsSeries(defensive_investors,Numbers_of_investors)