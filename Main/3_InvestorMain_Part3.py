from Lib import Investor
import plotly
import plotly.graph_objs as go
import os
import time
start_time = time.time()

#########################################
#           Part 3: Investors           #
#########################################


### Warning, Modelling 1000 investors could be time consuming ... ;)
Numbers_of_investors = 10  #But you can change the number of investors here
Budget = 10000
start = '01/01/2011'
end = '31/12/2015'


#Defensive investor

defensive_investors = []

#create the 1000 defensive investor
for i in range(0,Numbers_of_investors):
    new_Investor = Investor.Defensive_Investor(Budget, start, end)
    new_Investor.invest()
    defensive_investors.append(new_Investor)


model_defensive_investor_series = Investor.mergeInvestorsSeries_Dataframe(defensive_investors,Numbers_of_investors)


######################

#Aggressive investor

aggressive_investors = []

for j in range(0,Numbers_of_investors):
    new_Investor = Investor.Aggressive_Investor(Budget, start, end)
    new_Investor.invest()
    aggressive_investors.append(new_Investor)


model_aggressive_investor_series = Investor.mergeInvestorsSeries_Dataframe(aggressive_investors,Numbers_of_investors)

#Mixed Investor

mixed_investors = []

for k in range(0,Numbers_of_investors):
    new_Investor = Investor.Mixed_Investor(Budget, start, end)
    new_Investor.invest()
    mixed_investors.append(new_Investor)

model_mixed_investor_series = Investor.mergeInvestorsSeries_Dataframe(mixed_investors,Numbers_of_investors)




## MODELLING INVESTOR

data = []

data.append(go.Scatter(y=model_defensive_investor_series['Interest'], x=model_defensive_investor_series.index, name='Investor Defensive (' + str(Numbers_of_investors) + ')'))
data.append(go.Scatter(y=model_aggressive_investor_series['Interest'], x=model_aggressive_investor_series.index, name='Investor Aggressive (' + str(Numbers_of_investors) + ')'))
data.append(go.Scatter(y=model_mixed_investor_series['Interest'], x=model_mixed_investor_series.index, name='Investor Mixed (' + str(Numbers_of_investors) + ')'))
#data.append(go.Scatter(y=model_mixed_investor_series[1], x=model_mixed_investor_series[0], name='Investor Mixed (' + str(Numbers_of_investors) + ')'))

plotpath = os.path.abspath("../Results/Invest_modelling.html")

#Draw the graph
fig = go.Figure(data=data)
plotly.offline.plot(fig, filename=plotpath)
#py.iplot(fig)
print("--- %s seconds ---" % (time.time() - start_time))