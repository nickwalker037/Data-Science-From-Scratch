# Ex. need description of how many friends your members have that is usable in conversation

# Histogram of friend counts:
friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of Friends")
plt.ylabel("# of People")
plt.show()

# But this chart is still too difficult to slip into conversations.. so do some otha stuff

# Number of data points:
num_points = len(num_friends)                               # 204

# Largest and smallest values
largest_value = max(num_friends)                            #101
smallest_value = min(num_friends)                           #1

#Finding values in specific positions:
sorted_values = sort(num_friends)
smallest_value = sorted_value[0]                            #1
second_smallest_value = sorted_value[1]                     #1
second_largest_value = sorted_values[-2]                    #49


# ----- CENTRAL TENDENCIES ----- #

# Mean:
def mean(x):
    return sum(x) / len(x)
mean(num_friends)                                           #7.333333

# Median:
def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
        # // --> divide with integral result (ignore remainder)

    if n % 2 == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else
        # if even, return the average of the two middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2
median(num_friends)                                         # 6.0


# Cool Trick: if we have n data points and one of them increases by some small amount e, then necessarily the mean will increase by e/n

# Quantile

def quantile(x, p):
    """ returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

quantile(num_friends, 0.10)                                 # 1
quantile(num_friends, 0.25)                                 # 3
quantile(num_friends, 0.75)                                 # 9
quantile(num_friends, 0.90)                                 # 13


# Mode

def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems()
            if count == max_count]
mode(num_friends)                                           # 1 and 6
