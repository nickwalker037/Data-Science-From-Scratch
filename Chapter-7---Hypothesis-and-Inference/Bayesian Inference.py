# ----- BAYESIAN INFERENCE ----- #

# this approach involves treating the unknown parameters as random variables
# you start with a prior distribution for the parameters and then use the observed data and Bayes's Theorem to get an updated posterior distribution for the parameters
#       - so rather than making probability judgements about the tests, you make probability judgements about the parameters themselves
# Ex. when the unknown parameter is a probability (as in our coin-flipping ex.), we often use a prior from the Beta Distribution, which puts all its possible balues between 0 and 1:
def B(alpha, beta):
    """a normalizing constant so that the total probability is 1"""
    return math.gamma(apha) * math.gamma(beta) / math.gamma(alpha + beta)
def beta_pdf(x, alpha, beta):
    if x < 0 or x > 1:                                                  # no weight outside of [0, 1]
        return 0
    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / B(alpha + beta)
# generally speaking, the dist. centers its weight at:
alpha / (alpha + beta)
# and the larger the alpha and beta are, the "tighter" the distribution is
# Ex.
#   - if alpha and beta are both 1, it’s just the uniform distribution (centered at 0.5, very dispersed)
#   - if alpha is much larger than beta, most of the weight is near 1
#   - if alpha is much smaller than beta, most of the weight is near zero
