import random
import math
import numpy as np

def main():
    # These are the amounts of items bought. Algorithm uses these
    # amounts = np.array([random.randint(0,10), random.randint(0,10), random.randint(0,100)])
    amounts = [random.randint(1,10), random.randint(1,10), random.randint(1,10)]

    # These are the actual prices of the items. Algorithm does not use these
    # prices = np.array([random.randint(0,100),random.randint(0,100),random.randint(0,100)])
    prices = [random.randint(1,100),random.randint(1,100),random.randint(1,100)]

    # This is the ground truth, algorithm uses this
    totalTruePrice = 0

    learningRate = 0.005
    for i in range (0,3):
        totalTruePrice += amounts[i]*prices[i]

    # Begin by initially randomizing weights and learned prices
    weights = np.array([random.random(),random.random(),random.random()])
    # weights = [random.random(),random.random(),random.random()]
    # learnedPrices = np.array([0,0,0])
    learnedPrices = [0,0,0]
    # dErrdWeight = np.array([0,0,0])
    dErrdWeight = [0,0,0]

    error = 1
    while (error > .000001):
        totalLearnedPrice = 0

        for i in range (0,3):
            learnedPrices[i] = weights[i]*amounts[i]
            totalLearnedPrice += learnedPrices[i]

        # totalLearnedPrice = sigmoid(totalLearnedPrice)

        # Compute the error given a mean squared error function
        error = 0.5*math.pow((totalTruePrice - totalLearnedPrice),2)

        # The derivative of the error with respect to the value passed to it
        dErrdOutput = (totalTruePrice - totalLearnedPrice) * (-1)

        for i in xrange (0,3):
            # The derivative of the error with respect to the 'i'th weight
            dErrdWeight[i] = (amounts[i] * dErrdOutput)

            # weights[i] -= math.tanh(learningRate*dErrdWeight[i])
            # weights[i] -= sigmoid(learningRate*dErrdWeight[i])
            weights[i] -= (learningRate*dErrdWeight[i])

    print "------------------------------------------------"
    print "The quantities of items purchased are:"
    print amounts
    print "The actual prices of items are:"
    print prices
    print "The estimated prices of the items are:"
    print weights
    print "------------------------------------------------"

def sigmoid(x):
    return 1/(1+math.exp(-x))

main()
