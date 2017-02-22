from Code import Stock
from matplotlib import style
import matplotlib.pyplot as plt

######################################
#           Part 2: Stocks           #
######################################



# TEST

list_stock = []

Google = Stock.Stock('GOOGL', 4, '01/01/2005', '31/12/2015')
Yahoo = Stock.Stock('YHOO', 4, '01/01/2005', '31/12/2015')
American = Stock.Stock('AXP', 4, '01/01/2005', '31/12/2015')
Apple = Stock.Stock('AAPL', 4, '01/01/2005', '31/12/2015')

#AAPL, GOOGL, YHOO, AXP, XOM, KO, NOK, MS, IBM and FDX
list_stock.append(Stock.Stock('GOOGL', 4, '01/01/2005', '31/12/2015'))
list_stock.append(Stock.Stock('AAPL', 4, '01/01/2005', '31/12/2015'))
list_stock.append(Stock.Stock('YHOO', 4, '01/01/2005', '31/12/2015'))
list_stock.append(Stock.Stock('AXP', 4, '01/01/2005', '31/12/2015'))
list_stock.append(Stock.Stock('XOM', 4, '01/01/2005', '31/12/2015'))
list_stock.append(Stock.Stock('KO', 4, '01/01/2005', '31/12/2015'))
list_stock.append(Stock.Stock('NOK', 4, '01/01/2005', '31/12/2015'))
list_stock.append(Stock.Stock('MS', 4, '01/01/2005', '31/12/2015'))
list_stock.append(Stock.Stock('IBM', 4, '01/01/2005', '31/12/2015'))
list_stock.append(Stock.Stock('FDX', 4, '01/01/2005', '31/12/2015'))

style.use('fivethirtyeight')

for i in range(0,9):
    list_stock[i].data.plot()

plt.title('All stocks plot')
plt.show()
