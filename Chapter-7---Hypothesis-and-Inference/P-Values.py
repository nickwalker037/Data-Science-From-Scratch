# ----- P-VALUES ----- #

# instead of choosing bounds based on some probability cutoff, we compute the probability - assuming Ho is observed - that we would see a value at least as extreme as the one we observed
# two-sided test:
def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        # if x is greater than the mean, the tail is what's greater than x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # if x is less than the mean, the tail is what's less than x
        return 2 * normal_probability_below(x, mu, sigma)
# Ex. if we were to see 530 heads, we would compute:
two_sided_p_value(529.5, mu_0, sigma_0)                                 # 0.062
#           - why did we use 529.5?
#               - called a con‐ tinuity correction.
#                   - It reflects the fact that normal_probability_between(529.5, 530.5, mu_0, sigma_0) is a better estimate of the probability of seeing 530 heads than normal_probability_between(530, 531, mu_0, sigma_0) is
#                   - Correspondingly, normal_probability_above(529.5, mu_0, sigma_0) is a better estimate of the probability of seeing at least 530 heads
# One way to see why this is a sensible estimate:
extreme_value_count = 0
for _ in range(100000):
    num_heads = sum(1 if random.random() < 0.5 else                     # count number of heads
                    for _ in range(1000))                               # in 1000 flips
    if num_heads >= 530 or num_heads <= 470:                            # and count how often the number is 'extreme'
        extreme_value_count += 1
print extreme_value_count / 100000                                      # 0.062
# Since the p-value is greater than our 5% significance, we don't reject the null
# if we instead saw 532 heads, the p-value would be:
two_sided_p_value(531.5, mu_0, sigma_0)                                 # 0.0463
#       - this value is smaller than the 5% significance, so we would reject the null

upper_p_value = normal_probability_above
lower_p_value = normal_probability_below

# for our one-sided test, if we saw 525 heads, the computation would be:
upper_p_value(524.5, mu_0, sigma_0)                                     # 0.061 --> which means we fail to reject the null
# if we saw 527 heads:
upper_p_value(526.5, mu_0, sigma_0)                                     # 0.047 --> reject the null at a 5% level of significance
