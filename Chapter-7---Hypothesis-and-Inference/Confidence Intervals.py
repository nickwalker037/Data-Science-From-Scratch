# ----- CONFIDENCE INTERVALS ----- #


# Ex. if we observe 525 heads out of 1,000 flips, then we estimate p = 0.525.... but how confident can we be about this estimate?
#       - if we knew the exact value of p, the central limit theorem tells us that the average of those Bernoulli variables should be approximately normal, with mean p and std. dev.:
math.sqrt(p * (1 - p) / 1000)

# here we don't know p, so instead we use our estimate:
p_hat = 525 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)                           # 0.0158

# here, we conclude that we are "95% confident" that the following interval contains the true parameter p:
normal_two_sided_bounds(0.95, mu, sigma)                                # [ 0.4940, 0.5560 ]
