# ----- THE BIAS VARIANCE TRADEOFF ----- # 

# is just another way of thinking about the overfitting problem 

# if your model has high bias (which means it performs poorly even on your training data) then one thing to try is adding more features
# if your model has high variance, then you can similarly remove features. But another solution is to obtain more data (if you can)


# holding model complexity constant, the more data you have, the harder it is to overfit
# on the other hand, more data won't help with bias
# if your model doesn't use enough features to capture regularities in the data, throwing more data at it won't help

