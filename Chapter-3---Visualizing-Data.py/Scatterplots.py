# ----- SCATTERPLOTS ----- #

friends = [ 70,  65,  72,  63,  71,  64,  60,  64,  67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

#label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count),               # put the label with its point
                 xytext=(5, -5)                                 # but slightly offset
                 textcoords='offset points')

plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of Friends")
plt.ylabel("Daily Minutes Spent on Site")
plt.show()

# Note: you might get a misleading picture if you let matplotlib choose the scale for you
# plt.axis("equal") is a quick way to fix this











