# ----- DISPERSION ----- #

# Range
    # Note: "range" already means something else in Python, so we'll use a different name
    
def data_range(x):
    return max(x) - min(x)
data_range(num_friends)                                     # 99

# Variance
def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]
def variance(x):
    """ assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)
variance(num_friends)                                       # 81.54

# Standard Deviation

def standard_deviation(x):
    return math.sqrt(variance(x))
standard_deviation(num_friends)                             # 9.03

# Outlier problem: if our highest value was 200, our st. dev = 14.89
# to solve the outlier problem with st. dev, we could calculate it using the 25th and 75th percentile values
def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)
interquartile_range(num_friends)                            # 6
