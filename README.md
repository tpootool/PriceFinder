------------------------------------------------------------------------------
WHAT IS THE PURPOSE OF THIS PROJECT
------------------------------------------------------------------------------

This project is meant to be an exercise in developing a simple machine 
learning algorithm by simulating a purchase of various items at different
prices.

------------------------------------------------------------------------------
HOW DOES THE PROGRAM WORK
------------------------------------------------------------------------------

The program generates the amount of individual items purchased as well as the
price of each item.  The machine learning alorithm takes the number of items
purchased and the total price (the amount of items purchased multiplied by 
their respective prices) and attempts to determine the individual price of
each item.  This is done through back propagation until the error function
returns a value below the desired threshold.

------------------------------------------------------------------------------
WHAT CAN THIS PROGRAM BE APPLIED TO
------------------------------------------------------------------------------

An application of this algorithm would be purchasing items from a store and 
not keeping the receipt.  The total cost of the items would be known either 
by looking at the amount of money missing from your wallet or seeing the 
transaction on your monthly statement, however the individual cost of each
item would not be as readily available.  The number of items and amount of
each item purchased would also be known since they would be in your position.

------------------------------------------------------------------------------
HOW ACCURATE IS THIS PROJECT
------------------------------------------------------------------------------

Currently this project does not return the actual values of the prices but
instead finds a reasonable estimate of what they could be with the same total
price as the actual prices and amounts.
