from Lib import Bond
import plotly
import plotly.graph_objs as go
import os

#########################################################
#           PArt1: SHORT AND LONGTERM BONDS             #
#########################################################



# TEST

STBond = Bond.ShortTerm(1000, 100, '01/01/2005')
LTBond = Bond.LongTerm(3000, 100, '01/01/2005')

data = []
data.append(go.Scatter(y=STBond.interestSeriesComplete()['Interest'], x=STBond.interestSeriesComplete().index, name='Short Term Interest'))
data.append(go.Scatter(y=LTBond.interestSeriesComplete()['Interest'], x=LTBond.interestSeriesComplete().index, name='Long Term Interest'))


#STBond.drawPlot()
#LTBond.drawPlot()



plotpath = os.path.abspath("../Results/Bond_Interest_Plot.html")

#Draw the graph
fig = go.Figure(data=data)
plotly.offline.plot(fig, filename=plotpath)
