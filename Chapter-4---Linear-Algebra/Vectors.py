# ----- VECTORS ----- #
    # are points in some finite-dimensional space

height_weight_age = [70,                            # inches
                     170,                           # pounds
                     40]                            # years
grades = [95,                                       # exam 1
          80,                                       # exam 2
          75,                                       # exam 3
          62]                                       # exam 4


#addition:
def vector_add(v, w):
    """adds corresponding elements"""
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]
#subtracting:
def vector_subtract(v, w):
    """subtracts corresponding elements"""
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]

# adding them componentwise: meaning vector [9, 3] + [5, 4] = [14, 7]
def vector_sum(vectors):
    """sums all corresponding elements"""
    result = vectors[0]                                         # start with first vector
    for vector in vectors[1:]:                                  # then loop over the others
        result = vector_add(result, vector)                     # and add them to the result
    return result

# if you think about it, we are just reducing the list of vectors using vector_add, which means we can rewrite this more briefly using higher-order functions
def vector_sum(vectors):
    return reduce(vector_add, vectors)

# or even: 
vector_sum = partial (reduce, vector_add)

# another way:
def scalar_multiply(c, v):
    """c is a number, v is a vector"""
    return [c * v_i for v_i in v]

# componentwise means of a list of same-sized vectors
def vector_mean(vectors):
    """compute the vector whose ith element is the mean of the ith elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

# dot product - the sum of their componentwise products
def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))

# vector sum of squares
def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

# use that to compute its magnitute (or length)
import math
def magnitude(v):
    return math.sqrt(sum_of_squares(v))

# we now have all the information we need to compute the distance between two vectors
def squared_distance(v, w):
    """(v_1 - w_1) ** 2 + ... + (v_n - v_w) ** 2"""
    return sum_of_squares(vector_subtract(v, w))
def distance(v, w):
    return math.sqrt(squared_distance(v, w))

# same as:
def distance(v, w):
    return magnitude(vector_subtract(v, w))
