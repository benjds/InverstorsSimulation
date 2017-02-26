from Lib import Investor
import plotly
import plotly.graph_objs as go
from plotly import tools
import os
import plotly.plotly as py

###########################################
#           Part 4: Simulations           #
###########################################


Numbers_of_investors = 1000
Budget = 10000
Years = ['2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']
#Years = ['2005']




### FOR EACH YEAR #####

fig = tools.make_subplots(rows=10, cols=3,
                          print_grid=False,
                          subplot_titles=("Defensive investors","Aggressive investors", "Mixed investors"))

for x in range(0, len(Years)):
    start = '01/01/' + Years[x]
    end = '31/12/' + Years[x]

    defensive_investors = []

    #create the 1000 defensive investor
    for i in range(0,Numbers_of_investors):
        new_Investor = Investor.Defensive_Investor(Budget, start, end)
        new_Investor.invest()
        defensive_investors.append(new_Investor)


    model_defensive_investor_series = Investor.mergeInvestorsSeries_Dataframe(defensive_investors,Numbers_of_investors)

    ####

    aggressive_investors = []

    for j in range(0,Numbers_of_investors):
        new_Investor = Investor.Aggressive_Investor(Budget, start, end)
        new_Investor.invest()
        aggressive_investors.append(new_Investor)


    model_aggressive_investor_series = Investor.mergeInvestorsSeries_Dataframe(aggressive_investors,Numbers_of_investors)

    ####
    mixed_investors = []

    for k in range(0, Numbers_of_investors):
        new_Investor = Investor.Mixed_Investor(Budget, start, end)
        new_Investor.invest()
        mixed_investors.append(new_Investor)

    model_mixed_investor_series = Investor.mergeInvestorsSeries_Dataframe(mixed_investors, Numbers_of_investors)

    #data = []

    #data.append(go.Scatter(y=model_defensive_investor_series['Interest'], x=model_defensive_investor_series.index,
    #                      name='Investor Defensive (' + str(Numbers_of_investors) + ')'))
    #data.append(go.Scatter(y=model_aggressive_investor_series['Interest'], x=model_aggressive_investor_series.index,
    #                       name='Investor Aggressive (' + str(Numbers_of_investors) + ')'))
    #data.append(go.Scatter(y=model_mixed_investor_series['Interest'], x=model_mixed_investor_series.index,
    #                       name='Investor Mixed (' + str(Numbers_of_investors) + ')'))

    fig.append_trace(go.Scatter(y=model_defensive_investor_series['Interest'], x=model_defensive_investor_series.index,
                          name='Investor Defensive (' + str(Numbers_of_investors) + ')'), (x + 1), 1)
    fig.append_trace(go.Scatter(y=model_aggressive_investor_series['Interest'], x=model_aggressive_investor_series.index,
                           name='Investor Aggressive (' + str(Numbers_of_investors) + ')'), (x + 1), 2)
    fig.append_trace(go.Scatter(y=model_mixed_investor_series['Interest'], x=model_mixed_investor_series.index,
                           name='Investor Mixed (' + str(Numbers_of_investors) + ')'), (x + 1), 3)

    #plotpath = os.path.abspath("../Results/Invest_modelling_for_"+Years[x]+".html")

    # Draw the graph
    #fig = go.Figure(data=data)
    #plotly.offline.plot(fig, filename=plotpath)


plotpath = os.path.abspath("../Results/Invest_modelling_by_year.html")
# Draw the graph
#plotly.offline.plot(fig, filename=plotpath)
py.iplot(fig)




