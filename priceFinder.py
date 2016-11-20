import random
import math
import numpy as np

def main():
    # These are the amounts of items bought. Algorithm uses these
    amounts = [4, 3, 7]

    # These are the actual prices of the items. Algorithm does not use these
    prices = [35,48,52]
    # This is the ground truth, algorithm uses this
    totalTruePrice = 0

    learningRate = 1
    for i in range (0,3):
        totalTruePrice += amounts[i]*prices[i]

    totalTruePrice = (totalTruePrice)
    # totalTruePrice = sigmoid(totalTruePrice)
    #
    # totalTruePrice += amounts[0:3] * prices[0:3]
    # print totalTruePrice

    # Begin by initially randomizing weights and learned prices
    # weights = [34,79,10]
    weights = [random.random(),random.random(),random.random()]
    learnedPrices = [0,0,0]
    dErrdWeight = [0, 0, 0]

    totalLearnedPrice = 0

    prevError = 5
    error = 6
    while (error > .000001):
        totalLearnedPrice = 0

        for i in range (0,3):
            learnedPrices[i] = weights[i]*amounts[i]
            totalLearnedPrice += learnedPrices[i]

        totalLearnedPrice = (totalLearnedPrice)
        # totalLearnedPrice = sigmoid(totalLearnedPrice)
        print weights
        # print dErrdWeight

        # print totalLearnedPrice
        # print learnedPrices

        prevError = error
        error = 0.5*math.pow((totalTruePrice - totalLearnedPrice),2)

        dErrdOutput = (totalTruePrice - totalLearnedPrice) * (-1)
        # dOutputdWeight = amounts

        for i in xrange (0,3):
            # dErrdWeight[i] = weights[i] * dErrdOutput
            dErrdWeight[i] = amounts[i] * dErrdOutput

            # weights[i] -= (learningRate*dErrdWeight[i])
            weights[i] -= (learningRate*dErrdWeight[i])/1000


        print totalLearnedPrice

        # print dErrdWeight
        # print weights
        # print totalLearnedPrice
        # print dErrdOutput
        # print dOutputdWeight
        # print error

def sigmoid(x):
    return 1/(1*math.exp(-x))


main()

# X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
# y = np.array([[0,1,1,0]]).T
# syn0 = 2*np.random.random((3,4)) - 1
# syn1 = 2*np.random.random((4,1)) - 1
# for j in xrange(60000):
#     l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
#     l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
#     l2_delta = (y - l2)*(l2*(1-l2))
#     l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))
#     syn1 += l1.T.dot(l2_delta)
#     syn0 += X.T.dot(l1_delta)