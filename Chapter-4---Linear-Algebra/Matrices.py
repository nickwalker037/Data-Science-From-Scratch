# ----- Matrices ----- #

# we will represent these as lists of lists. If A is a matrix, then A[i][j] is the element in the ith row and the jth column

A = [[1, 2, 3],
     [4, 5, 6]]
B = [[1, 2],
     [3, 4],
     [5, 6]]

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]] if A else 0                    # number of elements in the first row
    return num_rows, num_cols

def get_row(A, i):
    return A[i]                                         # A[i] is already the ith row

def get_column(A, j):
    return [A_i[j]                                      # jth element of row A_i
            for A_i in A]                               # for each row A_i

# Creating a matrix given its shape and a function for generalizing its elements using a nested list comprehension:
def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix whose (i,j)th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j)                             # given i, create a list
             for j in range(num_cols)]                  # [entry_fn(i, 0), ... ]
            for i in range(num_rows)]                   # create one list for each i

# given this function, we could make a 5x5 identity matrix (with 1s on the diagonal and 0s elsewhere)
def is_diagonal(i, j):
    """1's on the 'diagonal', 0's everywhere else"""
    return i if i == j else 0

identity_matrix = make_matrix(5, 5, is_diagonal)

# [[1, 0, 0, 0, 0],
#  [0, 1, 0, 0, 0],
#  [0, 0, 1, 0, 0],
#  [0, 0, 0, 1, 0],
#  [0, 0, 0, 0, 1]]

# Reasons we would use a matrix:
# (1.) to represent a data set consisting of multiple vectors, simply by considering each vector as a row of the matrix
            # Ex. if you had the heights, weights, and ages of 1,000 people... you could put them in a 1,000 x 3 matrix:
data = [[70, 170, 40],
        [65, 120, 26],
        [77, 250, 19],
        # ....
        ]
# (2.) we can use an n x k matrix to represent a linear function that maps k-dimensional vectors to n-dimensional vectors
# (3.) matrices can be used to represent binary relationships
            # Recall that before we had:
 friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

            # We could also represent this as:
#       user    0  1  2  3  4  5  6  7  8  9 
friendships = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # user 0
               [1, 0, 1, 1, 0, 0, 0, 0, 0, 0], # user 1
               [1, 1, 0, 1, 0, 0, 0, 0, 0, 0], # user 2
               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0], # user 3
               [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # user 4
               [0, 0, 0, 0, 1, 0, 1, 1, 0, 0], # user 5
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 6
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 7
               [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], # user 8
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]] # user 9
# the matrix representation makes it much quicker to check whether two nodes are connected
        # you just have to do a matrix lookup instead of (potentially) inspecting every edge
friendships[0][2] == 1                          # True, 0 and 2 are friends!! wahhhooooooo!!!
friendships[0][8] == 1                          # False, 0 and 8 aren't friends :( .... yet!!!!

# To find the connection a node has, you only need to inspect the column (or the row) corresponding to that node:
friends_of_five = [i                                                        # only need
                   for i, is_friend in enumerate(friendships[5])            # to look at
                   if is_friend]                                            # one row
