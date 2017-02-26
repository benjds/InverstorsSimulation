from Lib import Stock
import plotly
import plotly.graph_objs as go
import os
import plotly.plotly as py

######################################
#           Part 2: Stocks           #
######################################

list_stock = []


Start = '01/01/2005'
End = '31/12/2015'

# Create a list of stock
#AAPL, GOOGL, YHOO, AXP, XOM, KO, NOK, MS, IBM and FDX
list_stock.append(Stock.Stock('GOOGL', 1, Start, End))
list_stock.append(Stock.Stock('AAPL', 1, Start, End))
list_stock.append(Stock.Stock('YHOO', 1, Start, End))
list_stock.append(Stock.Stock('AXP', 1, Start, End))
list_stock.append(Stock.Stock('XOM', 1, Start, End))
list_stock.append(Stock.Stock('KO', 1, Start, End))
list_stock.append(Stock.Stock('NOK', 1, Start, End))
list_stock.append(Stock.Stock('MS', 1, Start, End))
list_stock.append(Stock.Stock('IBM', 1, Start, End))
list_stock.append(Stock.Stock('FDX', 1, Start, End))

#print("Stock")
#print(list_stock[0].data)

data = []

#add stock into a graph object
for i in range(0,9):
    list_stock[i].interestSeriesByTime()
    data.append(go.Scatter( x=list_stock[i].interestSeriesComplete().index, y=list_stock[i].interestSeriesComplete()['Interest'], name=list_stock[i].sTicker))

plotpath = os.path.abspath("../Results/final_plot.html")

#Draw the graph
fig = go.Figure(data=data)
plotly.offline.plot(fig, filename=plotpath)
#py.iplot(fig)