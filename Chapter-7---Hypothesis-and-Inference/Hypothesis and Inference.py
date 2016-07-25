 ----- HYPOTHESIS AND INFERENCE ----- #


# Ex. Coin flip
# Ho: p = 0.5 (probability of heads) ... H1: p != 0.5

def normal_approximation_to_binomial(n, p):
    """finds mu and sigma corresponding to a Binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

# whenever a random variable follows a normal distribution, you can use "normal_cdf" to figure out the probability that its realized value lies within (or outside) a particular interval:

# the normal cdf _is_ the probability variable is below a threshold
normal_probability_below = normal_cdf

# it's above the threshold if it's not below the threshold
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)

# it's between if it's less than hi, but not less than lo
def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normalcdf(lo, mu, sigma)

# it's outside if it's not between
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)


# we can also do the reverse:
#    - find either the nontail region or the (symmetric) interval around the mean that accounts for a certain level of likelihood
#           - Ex. if we want to find an interval centered at the mean and containing 60% probability, then:
#                   - we find the cutoffs where the upper and lower tails each contain 20% of the probability (leaving 60%):
def normal_upper_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z <= z) = probability"""
    return inverse_normal_cdf(probability, mu, sigma)
def normal_lower_bound(probability, mu=0, sigma=1):
    return inverse_normal_cdf(1 - probability, mu, sigma)
def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """ returns the symmetric (about the mean) bounds that contain the specified probability"""
    tail_probability = (1 - probability) / 2
    # upper bound should have tail_probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    # lower bound should have tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    return lower_bound, upper_bound


# Ex. lets say we choose to flip the coin n = 1000 times
# if our hypothesis is true, X should be distributed approximately normally with mean = 50 and st. dev. = 15.8
mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

# here is the test that rejects Ho if X falls outside the bounds:
normal_two_sided_bounds(0.95, mu_0, sigma_0)

# we are often interested in the power of a test, which is the probability of not making a type 2 error (we failt to regect Ho even though it is false)
# we can calculate the power of a test with the example below:
#       - let's check what happens if p is really 0.55, meaning the coin is slightly biased toward heads

#95% bounds based on assumption p is 0.5
lo, hi = normal_two_sided_bounds(0.95, mu=0, sigma=0)

# actual mu and sigma based on p = 0.55
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

# a type 2 error will occur when X is still in our original interval
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability


# if our null hypothesis was that the coin is not biased towards heads ( p <= 0.5 ),
#       then we want a one-sided test that rejects the null hypothesis when X is much larger than 50 but not when X is smaller than 50
hi = normal_upper_bound(0.95, mu_0, sigma_0)
#       - is 526 ( < 531, since we need more probability in the upper tail)
type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power = 1 - type_2_probability                                          # 0.936
# this is a more powerful test, since it no longer rejects Ho when X is below 469 (which is very unlikely to happen if H1 is true)
# and it rejects Ho when X is between 526 and 531 (which is somewhat likely to happen if H1 is true)

