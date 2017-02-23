from Code import Stock
import plotly
import plotly.graph_objs as go
import os

######################################
#           Part 2: Stocks           #
######################################

list_stock = []


Start = '01/01/2005'
End = '31/12/2015'

# Create a list of stock
#AAPL, GOOGL, YHOO, AXP, XOM, KO, NOK, MS, IBM and FDX
list_stock.append(Stock.Stock('GOOGL', 4, Start, End))
list_stock.append(Stock.Stock('AAPL', 4, Start, End))
list_stock.append(Stock.Stock('YHOO', 4, Start, End))
list_stock.append(Stock.Stock('AXP', 4, Start, End))
list_stock.append(Stock.Stock('XOM', 4, Start, End))
list_stock.append(Stock.Stock('KO', 4, Start, End))
list_stock.append(Stock.Stock('NOK', 4, Start, End))
list_stock.append(Stock.Stock('MS', 4, Start, End))
list_stock.append(Stock.Stock('IBM', 4, Start, End))
list_stock.append(Stock.Stock('FDX', 4, Start, End))


data = []

#add stock into a graph object
for i in range(0,9):
    data.append(go.Scatter( x=list_stock[i].data['Dates'], y=list_stock[i].data['High'], name=list_stock[i].sTicker))


plotpath = os.path.abspath("../Results/final_plot.html")

#Draw the graph
fig = go.Figure(data=data)
plotly.offline.plot(fig, filename=plotpath)
