from Code import Bond
import matplotlib.pyplot as plt

#########################################################
#           PArt1: SHORT AND LONGTERM BONDS             #
#########################################################



# TEST

STBond = Bond.ShortTerm(1000, 100)
LTBond = Bond.LongTerm(3000, 100)


#STBond.drawPlot()
#LTBond.drawPlot()

plt.plot(STBond.interestSeries())
plt.plot(LTBond.interestSeries())
plt.show()