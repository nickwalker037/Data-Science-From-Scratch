# ----- matplotlib ----- #
    # works well for simple bar charts, line charts, and scatterplots, but not elaborate interactive visualizations for the web

from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

#create a line chart, years on x-axis, gdp on y-axis
plt.plot(year, gdp, color='green', marker='o', linestyle='solid')

#add a title
plt.title("Nominal GDP")

#add a label to the y-axis
plt.ylabel("Billions of $")
plt.show()



# ----- BAR CHARTS ----- #
    # is a good choice when you want to show how some quantity varies among some discrete set of items

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# bars are by default width 0.8, so we'll add 0.1 to the left coordinates so that each bar is centered
xs = [i + 0.1 for i, _ in enumerate(movies)]

# plot bars with left x-coordinatese [xs], heights [num_oscars]
plt.bar(xs, num_oscars)

plt.ylabel("# of Academy Awards")
plt.xlabel("My Favorite Movies (That I've never heard of)")

# label x-axis with movie names at bar centers
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

plt.show


# ----- HISTOGRAMS ----- #

grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x - 4 for x in histogram.keys()],                      # shift each bar to the left by 4 -- ex. this makes the "80" bar have sides at 76 and 84, which means is centered at 80
        histogram.values(),                                     # give each bar its correct height
        8)                                                      # give each bar a width of 8 -- this leaves a small gap between bars since our bucket width is 10


plt.axis([-5, 105, 0, 5])                                       # x-axis from -5 to 105
                                                                # y-axis from 0 to 5

plt.xticks([10 * i for i in range(11)])                         # x-axis labels at 0, 10, ..., 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()


# ----- LINE CHARTS ----- #

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

# we can make multiple calls to plt.plot to show multiple series on the same chart
plt.plot(xs, variance, 'g-', label='variance')                  # green solid line
plt.plot(xs, bias_squared, 'r-.', label='bias^2')               # red dot-dashed line
plt.plot(xs, total_error, 'b:' label='total error')             # blue dotted line

# b/c we've assigned labels to each series we can get a legend for free
# loc=9 means "top center"
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()


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











