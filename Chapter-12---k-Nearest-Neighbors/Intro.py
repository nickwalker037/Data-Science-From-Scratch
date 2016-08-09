# k-Nearest Neighbors

# is one of the simplest predictive models there is
    # it only requires:
        # some notion of distance
        # an assumption that points that are close to one another are similar
# but in that, it neglects a lot of info and won't help you understand the drivers of whatever phenomenon you're looking at

# in this case, the data points will be vectors

# to start, we'll need a fn that counts votes

def raw_majority_vote(labels):
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner
