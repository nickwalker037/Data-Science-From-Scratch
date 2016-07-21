# Correlation
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0                                            # if no variation, correlation is zero
correlation(num_friends, daily_minutes)                     # 0.25

# calculating it without the outlier:
outlier = num_friends.index(100)                            # index of outlier

num_friends_good = [x
                    for i, x in enumerate(num_friends)
                    if i != outlier]
daily_minutes_good = [x
                      for i, x in enumerate(daily_minutes)
                      if i != outlier]
correlation(num_friends_good, daily_minutes_good)           #0.57
    # without the outlier, there is much stronger correlation

# Simpson's Paradox: 
        # correlations can be misleading when confounding variables (an extraneous variable that correlates with both the independent and dep. variable) are ignored

# Ex. if being on the west coast vs. east coast has correlation with the amount of friends you have
        # THE ONLY WAY TO AVOID THIS IS BY KNOWING YO DATAAAAAA ... and doing what you can to make sure you've checked for possible confounding factors


# Other Correlational Caveats

# a correlation of zero incicates there's no linear relationship between the 2 variables... HOWEVER..... these two have zero correlation....

x = [-2, -1, 0, 1, 2]
y = [2, 1, 0, -1, -2]

# BUT they certainly have a relationship (they are abs. values of one another)
        # what they don't have is a relationship in which knowing how x_i compares to mean(x) gives us information about how y_i compares to mean(y)
                # this is what correlation tests for

# In addition, it doesn't tell you anything about how large the relationship is...

x = [-2, -1, 0, 1, 2]
y = [99.98, 99.99, 100, 100.01, 100.02]

# these are perfectly correlated, but it's quite possible that this relationship isn't all that interesting
