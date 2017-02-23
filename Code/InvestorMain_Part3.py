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

Investor_1 = Investor.Defensive_Investor(10000,'01/03/2009','31/12/2015')

Investor_1.invest()

#print(Investor_1.portfolio)
# Defensive Investor => Looks Good !

#Aggressive investor

Investor_2 = Investor.Aggressive_Investor(10000,'01/03/2009','31/12/2015')

Investor_2.invest()

#Mixed Investor