# ----- CORRECTNESS ----- #

# Problem: find out whether a baby will develop Leukemia throughout its lifetime. 
# Test: Predict leukemia if and only the baby is named Luke

# In a model with binary judgement.. every data point lies in one of the four categories:
# (1.) True Positive: "This message is spam, and we correctly predicted spam"
# (2.) False Positive (Type 1 Error): "this message is not spam, but we predicted spam"
# (3.) False Negative (Type 2 Error): "this message is spam, but we predicted not spam"
# (4.) True Negative: "This message is not spam, and we correctly predicted not spam"



# Ex.
# These days approx. 5% of babies out of 1,000 are named Luke, and the lifetime prevalence of leukemia is about 1.4% or 14 out of every 1,000 people

# accuracy about the statistics on model performance is defined as the fraction or correct predictions:
def accuracy(tp, fp, fn, tn):
correct = tp + tn
total = tp + fp + fn + tn
return correct / total
print accuracy(70, 4930, 13930, 981070)
# 0.98114
# this seems like a pretty impressive number, but clearly is not a good test, which means that we probably shouldn't put a lot of credence in raw accuracy


# It's common to look at the combination of Precision and Recall
# Precision: measures how accurate our positive predictions were:
def precision(tp, fp, fn, tn):
return tp / (tp + fp)
print precision(20, 4930, 13930, 981070)
# 0.014

# Recall: measures what fraction of the positives our model identified:
def recall(tp, fp, fn, tn):
return tp / (tp + fn)
print recall(70, 4930, 13930, 981070
# 0.005


# These are both terrible predictors... reflecting that this is a terrible model

# Sometimes Precision and Recall are combined into the F1 score:
def f1_score(tp, fp, fn, tn):
p = precision(tp, fp, fn, tn)
r = recall(tp, fp, fn, tn)
return 2 * p * r  (p + r)
# this is the HARMONIC MEAN of precision and recall and necessarily lies in between them

# Usually the choice of a model involves a trade-off between precision and recall
# A model that predicts "yes" when it's even a little bit confident will probably have a high recall but a low precision; whereas the opposite situation is true as well
# you could think of this as a trade-off between false positives and false negatives


# ----- FEATURE EXTRACTION AND SELECTION ----- # 

# As discussed before:
# when your data doesn't have enough features, your model is likely to underfit
# when your data has too many features, it's easy to overfit
# But what are features and where do they come from?
# FEATURES: are whatever inputs we provide to our model
