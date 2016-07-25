# ----- P-HACKING ----- #


# A procedure that erroneously rejects the null hypothesis only 5% of the time will - by definition - 5% of the time erroneously reject the null hypothesis:

def run_experiment():
    """flip a fair coin 1000 times, True = heads, False = tails"""
    return [random.random() < 0.5 for _ in range(1000)]
def reject_fairness(experiment):
    """using the 5% significance level"""
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads > 531
random.seed(0)
experiments = [run_experiment() for _ in range(1000)]
num_rejections = len([experiment
                      for experiment in experiments
                      if reject_fairness(experiment)])
print num_rejections                                                    # 46
# this means if you're setting out to find "significant" results, you usually can (you just have to test enough hypotheses)
#   - remove the right outliers, and you could probably get your p-value below 0.05
#       - this is sometimes called P-hacking
