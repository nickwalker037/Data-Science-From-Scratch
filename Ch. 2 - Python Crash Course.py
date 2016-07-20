# Whitespace formatting -- uses indentation instead of curly braces (like many other languages)

for i in [1, 2, 3, 4, 5]:
  print(i)
  for j in [1, 2, 3, 4, 5]:
    print(j)
    print(i + j)
  print(i)
print("done looping home boy")

# Good practice to make code easier to read:

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

easier_to_read_list_of_lists = [ [1, 2, 3],
                                 [4, 5, 6],
                                 [7, 8, 9] ]

# be careful when importing the entire content of a module into your namespace
# this is b/c you may inadvertently overwrite variables you've already defined

#match = 10
#from re import *
#print match

#ahhhh!!!!!! re has a match function so it doesn't print the value you assigned


# ----- sets ----- #
    #--> data structure that represents a collection of distinct elements

s = set()
s.add(1)            # s is now { 1 }
s.add(2)            # s is now { 1, 2 }
s.add(2)            # s is still { 1, 2 }
x = len(s)          # equals 2
print(x)
y = 2 in s          # equals True
z = 3 in s          # equals False


#Use sests for 2 main reasons
    # (1.) "in" is a very fast operation on sets, and makes sets more appropriate than lists when you have a large collection of items that you want to use for a membership test

#stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]
#"zip" in stopwords_list                             # False, but have to check every element
#stopwords_set = set(stopwords_list)
#"zip" in stopwords_set                              # Very fast to check


    # (2.) is to find the "distinct" items in a collection

item_list = [1, 2, 3, 1, 2, 3]                      
num_items = len(item_list)                          # 6
item_set = set(item_list)                           # {1, 2, 3}
num_distinct_items = len(item_set)                  # 3
distinct_item_list = list(item_set)                 # {1, 2, 3}


# ------ Control Flow ------ #
    # you can control actions conditionally using if:

if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "i'd be able to buckle my shoe"
else:
    message = "when all else fails use else (if you so decide to include it)"

#ternary if-then-else statements:
parity = "even" if x % 2 == 0 else "odd"






#note: Python uses the value "None" to indicate a nonexistent value, instead of "null"

# ----- THE NOT SO BASICS ----- #

# ----- Sorting ----- #

x = [4, 2, 1, 3]
y = sorted(x)                                       # is [1, 2, 3, 4], but x is left unchanged
x.sort()                                            # now x is [1, 2, 3, 4]

#sort the list by absolute value from largest to smallest
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)   # is [-4, 3, -2, 1]
print(x)

#sort the words and counts from highest count to lowest
#wc = sorted(word_counts.items(),
#            key=lambda (word, count): count,        #change code over to python 3.5
#            reverse=True)
#print wc

# ----- List Comprehensions ----- #
    # is the Pythonic way to transform a list into another list, by choosing only certain elements, or by transforming elements, or both

even_numbers = [x for x in range(5) if x % 2 == 0]   # [0, 2, 4]
squares =      [x * x for x in range(5)]             # [0, 1, 4, 9, 16]
even_squares = [x * x for x in even_numbers]         # [0, 4, 16]

#you can also turn lists into dictionaries or sets

square_dict = { x : x * x for x in range(5) }        
print(square_dict)                                   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16 }

square_set = { x * x for x in [1, -1] }              # 1

#if you don't need the value from the list, it's conventional to use an underscore as the variable:
zeroes = [0 for _ in even_numbers]                   # has the same length as even_numbers

# A list comprehension can include multiple for s:
pairs = [(x, y)
         for x in range(10)
         for y in range(10)]                          #100 pairs: (0,0) (0,1) ... (9,8) (9,9)


# ----- Randomness ----- #

import random

four_uniform_randoms = [random.random() for _ in range(4)]
print(four_uniform_randoms)                          # Ex. [0.3220256806253545, 0.2424912926797519, 0.6635336754238194, 0.819261195924264]

# random.shuffle() randomly reorders the elements of a list
up_to_ten = range(10)
random.shuffle(up_to_ten)
print(up_to_ten)

# random.choice() will randomly pick one element from a list
my_best_friend = random.choice(["Alice", "Bob", "Charlie"])     # "Bob" for me

# random.sample(variable name, sample size) will randomly choose a sample of elements without replacements (duplicates)
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)             # [16, 36, 10, 6, 25, 9]

# to choose a sample of elements WITH replacement, you can just make multiple calls to random.choice
four_with_replacement = [random.choice(range(10))
                         for _ in range(4)]

# ----- Object-Oriented Programming ----- #

# Python allows you to define classes that encapsulate data and the functions that operate on them
# member functions - given an instance of "Set", these allow you to add items to it, remove items from it, and check whether it contains a certain value

#by convention, we give classes PascalCase names
class Set:
    # these are the member functions
    # every one takes a first parameter "self" (another convention)
    # that refefrs to the particular Set object being used
    def _init_(self, values=none):
        """This is the constructor. It gets called when you create a new Set. You would use it like:
        s1 = Set()                   # empty set
        s2 = Set([1, 2, 2, 3])       # initialize with values"""
        self.dict()                     # each instance of Set has its own dict property
        if values is not None:
            for value in values:
                self.add(value)
    def _repr_(self):
        """this is the string representation of a Set object if you type it at the Python prompt or pass it to str()"""

    #we'll represent membership by being a key in self.dict with value True
    def add(self, value):
        self.dict[value] = True

    # value is in the Set if it's a key in the dictionary
    def contains(self, value):
        return value in self.dict
    def remove(self, value):
        del self.dict[value]

# Use example:

s = Set([1,2,3])
s.add(4)
print(s.contains(4))                        #True
s.remove(3)
print(s.contains(3))                        #False



# ----- enumerate ----- #

# allows you to iterate over a list and use both its elements and their indexes:
# produces tuples (index, element)

for i, document in enumerate(documents):
    do_something(i, document)

#similarly, if we want just the indexes:

for i in range(len(documents)): do_something(i) -----> not pythonic
for i, _ in enumerate(documents): do_something(i) ---> pythonic!!!


# ----- zip and Argument Unpacking ----- #

# allows you to transform multiple lists into a single list of tuples of corresponding elements

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zip(list1, list2)                           #output: [('a', 1), ('b', 2), ('c', 3)]

# if lists are different lengths, zip stops as soon as the first list ends

# can also unzip lists:

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
# the asterisk performs argument unpacking, which uses the elements of pairs as individual arguments to zip
# this returns: [('a','b','c'), ('1','2','3')]


# ----- args and kwargs ------ #

# create a function that takes "f" as some input and with any imput returns a value twice that of f
def doubler(f):
    def g(x):
        return 2 * f(x)
    return g

#this works in some cases:
def f1(x):
    return x + 1

g = doubler(f1)
print(g(3))










