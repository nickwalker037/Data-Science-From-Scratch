# ----- OVERFITTING AND UNDERFITTING ----- #

# Overfitting - producing a model that performs well on the data you train it on but generalizes poorly to any new data
# - this could involve learning noise in the data
# - or it could involve learning to identify specific inputs rather than whatever factors are actually predictive for the desired output


# Underfitting - producing a model that doesn't perform well even on the training data
# - typically when this happens you can simply decide your model isn't good enough and keep looking for a better one


# so how do we avoid this?
    # - use different data to train the model and to test the model
        # - simplest way to do this:
            # - split your data set
                # - so for ex. you 2/3 of the data to train the model and measure the model's performance with the remaining 1/4
def split_data(data, prob):
  """split data into fractions [prob, 1 - prob]"""
  results = [], []
  for row in data:
    results[0 if random.random() < prob else 1].append(row)
  return results


# Often, we'll have a matrix X of input variables and a vector Y of output variables
# - in that case, we need to make sure to put corresponding values together in either the training data or the test data:

def train_test_split(x, y, test_pct):
  data = zip(x, y)                                                    # pair corresponding values
  train, test = split_data(data, 1 - test_pct)                          # split the data set of pairs
  x_train, y_train = zip(*train)
  x_test, y_test = zip(*test)
  return x_train, x_test, y_train, y_test

# so that you might do something like:
model = SomeKindOfModel()
x_train, x_test, y_train, y_test = train_test_split(xs, ys, 0.33)
model.train(x_train, y_train)
performance = model.test(x_test, y_test)

# if the model was overfit to the training data, then it will hopefully perform really poorly on the (completely separate) data set
# if it performs well on the test data, then you can be more confident that it's fitting rather than overfitting
    # HOWEVER, there are a couple of ways that this could go wrong..
        # (1.) there are common patterns in the test and train data that wouldn't generalize to a larger data set
            # - Ex. dataset = user activity. 
            # - in this case, users will appear in both the training data and the test data, so certain models may learn to identify users rather than discover relationships involving attributes
        # (2.) if you use the test/train split not just to judge a model but to also choose from among many models
            # - this is a big problem b/c it makes the test set function as a second training set
                # - in this situation, split the data up into 3 parts:
                    # - a training set for building models
                    # - a validation set for choosing among trained models
                    # - a test set for judging the final model
