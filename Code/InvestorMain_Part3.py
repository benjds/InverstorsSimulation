from Code import Investor
from matplotlib import style
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objs as go
import os

#########################################
#           Part 3: Investors           #
#########################################



# TEST

#Defensive investor

Investor_1 = Investor.Defensive_Investor(100000,'01/03/2008','01/02/2015')

Investor_1.invest()

# Defensive Investor => Looks Good !

#Aggressive investor

Investor_2 = Investor.Aggressive_Investor(100000,'01/03/2008','01/02/2015')

Investor_2.invest()

#Investor_2.profitReturnSeries()

#Mixed Investor

Investor_3 = Investor.Mixed_Investor(100000,'01/03/2008','01/02/2015')

Investor_3.invest()

#Investor_3.profitReturnSeries()



## MODELLING INVESTOR


data = []
data.append(go.Scatter(y=Investor_1.profitReturnSeries()[1], x=Investor_1.profitReturnSeries()[0], name='Investor 1 (Defensive)'))
data.append(go.Scatter(y=Investor_2.profitReturnSeries()[1], x=Investor_2.profitReturnSeries()[0], name='Investor 2 (Aggressive)'))
data.append(go.Scatter(y=Investor_3.profitReturnSeries()[1], x=Investor_3.profitReturnSeries()[0], name='Investor 3 (Mixed)'))

plotpath = os.path.abspath("../Results/Invest_modelling.html")

#Draw the graph
fig = go.Figure(data=data)
plotly.offline.plot(fig, filename=plotpath)

